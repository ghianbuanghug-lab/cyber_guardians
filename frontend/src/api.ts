/**
 * api.ts — CyberGuardian v1.3
 * Centralized API calls to Flask backend.
 * For Replit: set REACT_APP_API_URL=https://your-backend.repl.co/api in Replit Secrets
 * For local dev: leave unset — proxy in package.json handles it automatically
 */

const BASE = process.env.REACT_APP_API_URL || '/api';

function getHeaders(): Record<string, string> {
  const token = localStorage.getItem('cg_token');
  return {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  };
}

async function request<T>(method: string, path: string, body?: unknown): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method,
    headers: getHeaders(),
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || 'Request failed');
  return data as T;
}

// ── Token auto-refresh ────────────────────────────────────────────────────────
// Silently refreshes token every 20 hours so active players never get logged out.
let _refreshTimer: ReturnType<typeof setTimeout> | null = null;

export function scheduleTokenRefresh() {
  if (_refreshTimer) clearTimeout(_refreshTimer);
  _refreshTimer = setTimeout(async () => {
    try {
      const data = await request<{ token: string }>('POST', '/auth/refresh');
      localStorage.setItem('cg_token', data.token);
      scheduleTokenRefresh(); // reschedule for next cycle
    } catch {
      // Token fully expired — user will see the login screen naturally
    }
  }, 20 * 60 * 60 * 1000); // 20 hours
}

export function clearTokenRefresh() {
  if (_refreshTimer) { clearTimeout(_refreshTimer); _refreshTimer = null; }
}

// ── Auth ──────────────────────────────────────────────────────────────────────
export const auth = {
  register: (username: string, password: string, email?: string) =>
    request<{ token: string; user: User }>('POST', '/auth/register', { username, password, email }),
  login: (username: string, password: string) =>
    request<{ token: string; user: User }>('POST', '/auth/login', { username, password }),
  refresh: () => request<{ token: string }>('POST', '/auth/refresh'),
};

// ── User ──────────────────────────────────────────────────────────────────────
export const user = {
  profile:     () => request<{ user: User; progress: Progress }>('GET', '/user/profile'),
  leaderboard: () => request<{ leaderboard: LeaderboardEntry[] }>('GET', '/user/leaderboard'),
};

// ── Room 1 — Knowledge Quiz ───────────────────────────────────────────────────
export const room1 = {
  /** Fetch all available categories for the category filter UI */
  categories: () => request<{ categories: string[] }>('GET', '/room1/categories'),

  /** Start a quiz. Pass category='all' (default) or a specific category name */
  start: (category = 'all') =>
    request<{ session_id: number; questions: Question[]; category: string }>
      ('POST', '/room1/start', { category }),

  submit: (session_id: number, answers: Record<string, number>) =>
    request<Room1Result>('POST', '/room1/submit', { session_id, answers }),
};

// ── Room 2 — Password Lab ────────────────────────────────────────────────────
export const room2 = {
  checkPassword:   (password: string) =>
    request<PasswordAnalysis>('POST', '/room2/check-password', { password }),
  crackSimulation: (password: string) =>
    request<CrackResult>('POST', '/room2/crack-simulation', { password }),
};

// ── Room 3 — Access Control Arena ────────────────────────────────────────────
export const room3 = {
  scenarios: () => request<{ scenarios: Scenario[] }>('GET', '/room3/scenarios'),

  /** is_sos=true applies the 1.5× XP bonus for SOS challenge decisions */
  decide: (scenario_id: number, decision: 'grant' | 'deny', is_sos = false) =>
    request<DecisionResult>('POST', '/room3/decide', { scenario_id, decision, is_sos }),

  complete: (score: number, total: number) =>
    request<{ badges: string[]; new_badges: string[]; mentor: MentorFeedback }>
      ('POST', '/room3/complete', { score, total }),
};

// ── SOS Boss Challenge ────────────────────────────────────────────────────────
export const sos = {
  /** Returns 5 hardest scenarios + 90-second time limit */
  scenarios: () =>
    request<{ scenarios: Scenario[]; time_limit: number; sos_bonus: string }>
      ('GET', '/sos/scenarios'),

  /** Record SOS result — awards SOS Survivor / SOS Elite badges */
  complete: (score: number, total: number, time_used: number) =>
    request<SOSResult>('POST', '/sos/complete', { score, total, time_used }),
};

// ── Results ───────────────────────────────────────────────────────────────────
export const results = {
  final: () => request<FinalResults>('GET', '/results/final'),
};

// ══════════════════════════════════════════════════════════════════════════════
//  TYPES
// ══════════════════════════════════════════════════════════════════════════════

export interface User {
  id: number;
  username: string;
  email?: string;
}

export interface Progress {
  xp: number;
  hearts: number;
  level: number;
  streak: number;
  room1_completed: number;
  room2_completed: number;
  room3_completed: number;
  sos_completed: number;
  room1_score: number;
  room2_score: number;
  room3_score: number;
  sos_score: number;
  total_score: number;
  badges: string[];
}

export interface Question {
  id: number;
  question: string;
  options: string[];
  explain: string;
  category?: string;
  difficulty?: 'easy' | 'medium' | 'hard';
}

export interface Room1Result {
  score: number;
  total: number;
  percentage: number;
  xp_earned: number;
  results: QuestionResult[];
  mentor: MentorFeedback;
  new_badges?: string[];
  category_stats?: Record<string, { correct: number; total: number }>;
}

export interface QuestionResult {
  question: string;
  options: string[];
  your_answer: number;
  correct_answer: number;
  correct: boolean;
  explain: string;
  category?: string;
}

export interface PasswordAnalysis {
  score: number;
  label: string;
  color: string;
  crack_time: string;
  crack_seconds: number;
  crack_attempts: string;   // e.g. "3.52e+18"
  entropy: number;
  entropy_label: 'Low' | 'Medium' | 'High';
  patterns_found: string[];
  suggestions: string[];
  checks: {
    length: boolean;
    uppercase: boolean;
    lowercase: boolean;
    numbers: boolean;
    special: boolean;
    no_patterns: boolean;
    not_common: boolean;
  };
}

export interface CrackResult {
  analysis: PasswordAnalysis;
  simulation: {
    steps: SimStep[];
    cracked: boolean;
    method: string | null;
  };
  xp_earned: number;
  mentor: MentorFeedback;
  new_badges?: string[];
}

export interface SimStep {
  phase: string;
  detail?: string;
  attempted?: string[];
  patterns?: string[];
  combinations?: string;
  success: boolean;
  found?: string;
}

export interface Scenario {
  id: number;
  type: 'email' | 'access_request';
  title: string;
  sender: string;
  subject: string;
  body: string;
  attachments: string[];
  threat_type: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  clues: string[];
  xp: number;
}

export interface DecisionResult {
  correct: boolean;
  correct_decision: 'grant' | 'deny';
  explanation: string;
  clues: string[];
  threat_type: string;
  severity: string;
  xp_earned: number;
  mistake_type?: 'false_negative' | 'false_positive';
  mistake_label?: string;
}

export interface SOSResult {
  score: number;
  total: number;
  percentage: number;
  time_used: number;
  badges: string[];
  new_badges: string[];
  mentor: MentorFeedback;
}

export interface MentorFeedback {
  feedback: string;
  tip: string;
}

export interface FinalResults {
  username: string;
  xp: number;
  level: number;
  hearts: number;
  streak: number;
  badges: string[];
  all_badges?: string[];
  badge_definitions?: Record<string, string>;
  room_scores: { room1: number; room2: number; room3: number; sos: number };
  rooms_completed: { room1: boolean; room2: boolean; room3: boolean; sos: boolean };
  total_score: number;
  mentor_feedback: Array<{ room: string; feedback: string; tip: string }>;
}

export interface LeaderboardEntry {
  username: string;
  xp: number;
  level: number;
  total_score: number;
  badges: string;
}
