// pages/Room2.tsx - Password Strength Lab
import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { room2, PasswordAnalysis, CrackResult, SimStep } from '../api';
import { RoomProgress, MentorCard, XPPopup, CyberButton, Alert, LoadingScreen } from '../components/UI';

type SubPhase = 'learn' | 'test' | 'crack' | 'results';

const WEAK_EXAMPLES = ['password', '123456', 'qwerty', 'abc123', 'letmein'];
const STRONG_EXAMPLES = ['Tr0ub4dor&3!', 'C0rrect-Horse-B4ttery!', 'X$9mKp#2nLv@Wq'];

const LESSONS = [
  { icon: '📏', title: 'Length Matters Most', body: 'Every extra character multiplies possible combinations exponentially. A 16-character password is astronomically stronger than an 8-character one.', tip: 'Aim for 12+ characters minimum' },
  { icon: '🎭', title: 'Complexity = Variety', body: 'Mix uppercase, lowercase, numbers, and symbols. Using all 4 types increases the "character pool" your password is chosen from.', tip: 'Use Upper + lower + 123 + !@#' },
  { icon: '🚫', title: 'Avoid Common Patterns', body: 'Dictionary attacks and credential stuffing lists contain millions of common passwords. "Password1!" is cracked in seconds.', tip: 'Never use names, dates, or dictionary words' },
  { icon: '🔑', title: 'Uniqueness per Account', body: 'Using the same password everywhere means one breach compromises all your accounts. Use a password manager to generate and store unique passwords.', tip: 'Use a password manager like Bitwarden' },
];

export default function Room2() {
  const navigate = useNavigate();
  const [subPhase, setSubPhase] = useState<SubPhase>('learn');
  const [password, setPassword] = useState('');
  const [analysis, setAnalysis] = useState<PasswordAnalysis | null>(null);
  const [crackResult, setCrackResult] = useState<CrackResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [cracking, setCracking] = useState(false);
  const [error, setError] = useState('');
  const [showXP, setShowXP] = useState(false);
  const [xpAmount, setXpAmount] = useState(0);
  const [crackLog, setCrackLog] = useState<string[]>([]);
  const [testPassword, setTestPassword] = useState('');
  const logRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (logRef.current) logRef.current.scrollTop = logRef.current.scrollHeight;
  }, [crackLog]);

  const checkPassword = async (pwd: string) => {
    if (!pwd) return;
    setLoading(true); setError('');
    try {
      const data = await room2.checkPassword(pwd);
      setAnalysis(data);
    } catch (e: any) { setError(e.message); }
    finally { setLoading(false); }
  };

  useEffect(() => {
    if (subPhase !== 'test') return;
    const t = setTimeout(() => {
      if (password.length > 0) checkPassword(password);
      else setAnalysis(null);
    }, 400);
    return () => clearTimeout(t);
  }, [password, subPhase]);

  function delay(ms: number) { return new Promise(r => setTimeout(r, ms)); }

  const runCrackSim = async () => {
    if (!testPassword) return;
    setCracking(true); setCrackLog([]); setError('');
    const logs = [
      '[*] Initializing CyberGuardian Password Analyzer...',
      '[*] Loading dictionary: 10,000,000 common passwords...',
      '[*] Starting Phase 1: Dictionary Attack...',
    ];
    for (const log of logs) { await delay(400); setCrackLog(prev => [...prev, log]); }
    try {
      const data = await room2.crackSimulation(testPassword);
      for (const step of (data.simulation.steps as SimStep[])) {
        await delay(600);
        setCrackLog(prev => [...prev, `\n[*] ${step.phase}:`]);
        if (step.attempted) {
          for (const attempt of step.attempted) {
            await delay(80);
            setCrackLog(prev => [...prev, `  Trying: ${attempt} ... FAIL`]);
          }
        }
        if (step.success && step.found) {
          await delay(300);
          setCrackLog(prev => [...prev, `  Trying: ${step.found} ... *** MATCH FOUND! ***`]);
        } else if (!step.success) {
          await delay(400);
          setCrackLog(prev => [...prev, `  Detail: ${step.detail || "analyzing..."}`]);
          setCrackLog(prev => [...prev, data.simulation.cracked ? '  Status: CRACKED INSTANTLY' : '  Status: INFEASIBLE - password is strong']);
        }
      }
      await delay(500);
      const final = data.simulation.cracked
        ? `\n[!] RESULT: Password CRACKED via ${data.simulation.method}`
        : '\n[✓] RESULT: Password resisted all attacks — Strength: ' + data.analysis.label;
      setCrackLog(prev => [...prev, final]);
      setCrackResult(data);
      setXpAmount(data.xp_earned);
      setShowXP(true);
      setTimeout(() => setShowXP(false), 3000);
      setSubPhase('results');
    } catch (e: any) { setError(e.message); }
    finally { setCracking(false); }
  };

  const scoreColor = (s: number) =>
    (['text-cyber-red', 'text-cyber-orange', 'text-cyber-yellow', 'text-cyber-green', 'text-cyber-blue'][s]) || 'text-gray-400';

  // ── LEARN ────────────────────────────────────────────────────────────────────
  if (subPhase === 'learn') {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={2} />
          <div className="text-center mb-8">
            <div className="text-5xl mb-4 animate-float">🔐</div>
            <div className="font-mono text-xs text-cyber-green tracking-widest mb-2">ROOM 02</div>
            <h2 className="font-display text-3xl font-black text-white">PASSWORD LAB</h2>
            <p className="text-gray-400 text-sm mt-2">Learn the art of creating unbreakable passwords</p>
          </div>
          <div className="grid grid-cols-1 gap-4 mb-8">
            {LESSONS.map((lesson, i) => (
              <div key={i} className="cyber-panel rounded-lg p-5 border border-cyber-green/20 cyber-card">
                <div className="flex items-start gap-4">
                  <span className="text-3xl flex-shrink-0">{lesson.icon}</span>
                  <div>
                    <h3 className="font-display text-sm font-bold text-cyber-green mb-2">{lesson.title}</h3>
                    <p className="text-gray-400 text-sm leading-relaxed mb-3">{lesson.body}</p>
                    <div className="inline-block bg-cyber-yellow/10 border border-cyber-yellow/30 rounded px-3 py-1">
                      <span className="font-mono text-xs text-cyber-yellow">💡 {lesson.tip}</span>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
          <div className="grid grid-cols-2 gap-4 mb-8">
            <div className="cyber-panel rounded-lg p-4 border border-cyber-red/30">
              <div className="font-mono text-xs text-cyber-red tracking-wider mb-3">✗ WEAK PASSWORDS</div>
              {WEAK_EXAMPLES.map(p => <div key={p} className="font-mono text-xs text-gray-500 py-1 border-b border-gray-800 last:border-0">{p}</div>)}
            </div>
            <div className="cyber-panel rounded-lg p-4 border border-cyber-green/30">
              <div className="font-mono text-xs text-cyber-green tracking-wider mb-3">✓ STRONG PASSWORDS</div>
              {STRONG_EXAMPLES.map(p => <div key={p} className="font-mono text-xs text-gray-300 py-1 border-b border-gray-800 last:border-0 break-all">{p}</div>)}
            </div>
          </div>
          <div className="flex gap-3">
            <CyberButton onClick={() => navigate('/')} variant="red" fullWidth>← BACK</CyberButton>
            <CyberButton onClick={() => setSubPhase('test')} variant="green" fullWidth>▶ TEST A PASSWORD</CyberButton>
          </div>
        </div>
      </div>
    );
  }

  // ── TEST ─────────────────────────────────────────────────────────────────────
  if (subPhase === 'test') {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={2} />
          <div className="text-center mb-8">
            <div className="font-mono text-xs text-cyber-green tracking-widest mb-2">ROOM 02 — STRENGTH ANALYZER</div>
            <h2 className="font-display text-2xl font-black text-white">TEST YOUR PASSWORD</h2>
          </div>
          <div className="cyber-panel rounded-lg p-6 border border-cyber-green/30 mb-6">
            <label className="font-mono text-xs text-gray-400 block mb-2 tracking-wider">ENTER PASSWORD TO ANALYZE</label>
            <input type="text" value={password} onChange={e => setPassword(e.target.value)}
              className="cyber-input rounded text-xl tracking-widest" placeholder="type a password..." autoComplete="off" />
            <p className="font-mono text-xs text-gray-600 mt-2">Password is NOT stored in plain text</p>
          </div>

          {analysis && (
            <div className="cyber-panel rounded-lg p-6 border border-cyber-border mb-6">
              <div className="mb-6">
                <div className="flex justify-between items-center mb-3">
                  <span className="font-mono text-xs text-gray-400">STRENGTH</span>
                  <span className={`font-display text-sm font-bold ${scoreColor(analysis.score)}`}>{analysis.label}</span>
                </div>
                <div className="flex gap-1">
                  {[0,1,2,3,4].map(i => (
                    <div key={i} className={`h-3 flex-1 rounded-sm transition-all duration-300 ${
                      i <= analysis.score
                        ? (['bg-cyber-red','bg-cyber-orange','bg-cyber-yellow','bg-cyber-green','bg-cyber-blue'][analysis.score])
                        : 'bg-gray-800'
                    }`} />
                  ))}
                </div>
              </div>
              <div className="flex items-center gap-3 mb-6 p-4 rounded border border-cyber-border bg-black/30">
                <span className="text-2xl">⏱️</span>
                <div>
                  <div className="font-mono text-xs text-gray-400">ESTIMATED CRACK TIME</div>
                  <div className={`font-display text-lg font-bold ${scoreColor(analysis.score)}`}>{analysis.crack_time}</div>
                  <div className="font-mono text-xs text-gray-600">at 1 billion attempts/second</div>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-2 mb-6">
                {Object.entries({
                  '12+ characters': analysis.checks.length,
                  'Uppercase (A-Z)': analysis.checks.uppercase,
                  'Lowercase (a-z)': analysis.checks.lowercase,
                  'Numbers (0-9)': analysis.checks.numbers,
                  'Special (!@#...)': analysis.checks.special,
                  'Not common': analysis.checks.not_common,
                  'No patterns': (analysis.checks as any).no_patterns ?? true,
                }).map(([label, ok]) => (
                  <div key={label} className={`flex items-center gap-2 text-xs font-mono ${ok ? 'text-cyber-green' : 'text-gray-600'}`}>
                    <span>{ok ? '✓' : '✗'}</span><span>{label}</span>
                  </div>
                ))}
              </div>
              {(analysis as any).entropy_bits !== undefined && (
                <div className="flex items-center gap-3 mb-4 p-3 rounded border border-cyber-border bg-black/20">
                  <span className="text-lg">🔢</span>
                  <div>
                    <div className="font-mono text-xs text-gray-400">ENTROPY</div>
                    <div className={`font-display text-sm font-bold ${(analysis as any).entropy_bits >= 60 ? 'text-cyber-green' : (analysis as any).entropy_bits >= 40 ? 'text-cyber-yellow' : 'text-cyber-red'}`}>
                      {(analysis as any).entropy_bits} bits
                    </div>
                    <div className="font-mono text-xs text-gray-600">
                      {(analysis as any).entropy_bits >= 60 ? 'High randomness' : (analysis as any).entropy_bits >= 40 ? 'Moderate randomness' : 'Low randomness'}
                    </div>
                  </div>
                </div>
              )}
              {analysis.suggestions && analysis.suggestions.length > 0 && (
                <div className="space-y-2">
                  <div className="font-mono text-xs text-cyber-yellow tracking-wider">SUGGESTIONS</div>
                  {analysis.suggestions.map((s: string, i: number) => (
                    <div key={i} className="font-mono text-xs text-gray-400 flex items-center gap-2">
                      <span className="text-cyber-yellow">→</span> {s}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {error && <Alert type="error" message={error} />}

          <div className="flex flex-wrap gap-2 mb-6">
            {[...WEAK_EXAMPLES.slice(0, 2), ...STRONG_EXAMPLES.slice(0, 2)].map(p => (
              <button key={p} onClick={() => setPassword(p)}
                className="font-mono text-xs border border-cyber-border text-gray-500 hover:text-gray-300 hover:border-cyber-blue/40 px-2 py-1 rounded transition-colors">
                {p}
              </button>
            ))}
          </div>
          <div className="flex gap-3">
            <CyberButton onClick={() => setSubPhase('learn')} variant="red">← LESSONS</CyberButton>
            <CyberButton onClick={() => { setTestPassword(password); setSubPhase('crack'); }} variant="green" disabled={!password} fullWidth>
              ▶ RUN CRACK SIMULATION
            </CyberButton>
          </div>
        </div>
      </div>
    );
  }

  // ── CRACK ────────────────────────────────────────────────────────────────────
  if (subPhase === 'crack') {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={2} />
          <div className="text-center mb-6">
            <div className="font-mono text-xs text-cyber-red tracking-widest mb-2">⚠️ CRACK SIMULATION</div>
            <h2 className="font-display text-2xl font-black text-white">PASSWORD CRACKER</h2>
            <p className="text-gray-500 text-xs mt-1 font-mono">Educational simulation only</p>
          </div>
          <div className="bg-black rounded-lg border border-cyber-green/30 mb-6 overflow-hidden">
            <div className="flex items-center gap-2 bg-gray-900 px-4 py-2 border-b border-cyber-green/20">
              <div className="w-3 h-3 rounded-full bg-cyber-red/70" />
              <div className="w-3 h-3 rounded-full bg-cyber-yellow/70" />
              <div className="w-3 h-3 rounded-full bg-cyber-green/70" />
              <span className="font-mono text-xs text-gray-500 ml-2">cyberguardian-cracker v1.0</span>
            </div>
            <div ref={logRef} className="h-64 overflow-y-auto p-4 font-mono text-xs text-cyber-green space-y-0.5">
              {crackLog.length === 0 && !cracking && (
                <div className="text-gray-600">
                  <span className="text-cyber-green">$</span> Ready to analyze: <span className="text-cyber-yellow">{testPassword}</span>
                </div>
              )}
              {crackLog.map((line, i) => (
                <div key={i} className={
                  line.includes('MATCH') || line.includes('CRACKED') ? 'text-cyber-red font-bold' :
                  line.includes('resisted') || line.includes('INFEASIBLE') ? 'text-cyber-green font-bold' :
                  line.includes('RESULT') ? 'text-cyber-yellow font-bold' : 'text-cyber-green/70'
                }>{line}</div>
              ))}
              {cracking && <div className="text-cyber-blue animate-pulse">▌</div>}
            </div>
          </div>
          {!cracking && crackLog.length === 0 && (
            <div className="cyber-panel rounded-lg p-4 border border-cyber-border mb-6">
              <label className="font-mono text-xs text-gray-400 block mb-2">TESTING PASSWORD:</label>
              <input type="text" value={testPassword} onChange={e => setTestPassword(e.target.value)}
                className="cyber-input rounded" placeholder="Enter password to crack test..." />
            </div>
          )}
          {error && <Alert type="error" message={error} />}
          {!cracking && crackLog.length === 0 && (
            <div className="flex gap-3">
              <CyberButton onClick={() => setSubPhase('test')} variant="red">← BACK</CyberButton>
              <CyberButton onClick={runCrackSim} variant="green" fullWidth disabled={!testPassword}>
                ▶ INITIATE CRACK SEQUENCE
              </CyberButton>
            </div>
          )}
        </div>
      </div>
    );
  }

  // ── RESULTS ───────────────────────────────────────────────────────────────────
  if (subPhase === 'results' && crackResult) {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <XPPopup xp={xpAmount} show={showXP} />
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={2} />
          <div className="text-center mb-6">
            <div className="font-mono text-xs text-cyber-green tracking-widest mb-2">ANALYSIS COMPLETE</div>
            <div className="text-5xl mb-3">{crackResult.simulation.cracked ? '💥' : '🛡️'}</div>
            <h2 className="font-display text-2xl font-black text-white">
              {crackResult.simulation.cracked ? 'PASSWORD CRACKED' : 'PASSWORD SECURE'}
            </h2>
          </div>
          <div className={`cyber-panel rounded-lg p-6 border mb-6 ${crackResult.simulation.cracked ? 'border-cyber-red/40' : 'border-cyber-green/40'}`}>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <div className="font-mono text-xs text-gray-400 mb-1">STRENGTH</div>
                <div className={`font-display text-xl font-bold ${scoreColor(crackResult.analysis.score)}`}>{crackResult.analysis.label}</div>
              </div>
              <div>
                <div className="font-mono text-xs text-gray-400 mb-1">CRACK TIME</div>
                <div className={`font-display text-lg font-bold ${crackResult.simulation.cracked ? 'text-cyber-red' : 'text-cyber-green'}`}>{crackResult.analysis.crack_time}</div>
              </div>
            </div>
          </div>
          <MentorCard feedback={crackResult.mentor.feedback} tip={crackResult.mentor.tip} show={true} />
          <div className="mt-6 bg-cyber-yellow/10 border border-cyber-yellow/30 rounded-lg p-4">
            <div className="font-mono text-xs text-cyber-yellow font-bold">+{crackResult.xp_earned} XP EARNED</div>
          </div>
          <div className="flex gap-3 mt-6">
            <CyberButton onClick={() => { setPassword(''); setAnalysis(null); setCrackLog([]); setSubPhase('test'); }} variant="blue">
              ↺ TEST ANOTHER
            </CyberButton>
            <CyberButton onClick={() => navigate('/room3')} variant="green" fullWidth>ROOM 03 →</CyberButton>
          </div>
        </div>
      </div>
    );
  }

  return <LoadingScreen />;
}
