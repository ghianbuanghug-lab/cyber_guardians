// components/UI.tsx - Shared UI components
import React, { useEffect, useState, ReactNode } from 'react';

// ─── HUD Bar ──────────────────────────────────────────────────────────────────
export function HUD({ xp, hearts, level, streak, username }: {
  xp: number; hearts: number; level: number; streak: number; username: string;
}) {
  return (
    <div className="fixed top-0 left-0 right-0 z-50 bg-cyber-darker border-b border-cyber-blue/20 px-6 py-3">
      <div className="max-w-6xl mx-auto flex items-center justify-between">
        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 relative">
            <div className="absolute inset-0 border-2 border-cyber-blue rotate-45 animate-pulse-slow" />
            <div className="absolute inset-1 border border-cyber-green rotate-45" />
          </div>
          <span className="font-display text-sm font-bold text-cyber-blue tracking-widest">CYBERGUARDIAN</span>
        </div>

        {/* Stats */}
        <div className="flex items-center gap-6">
          {/* Hearts */}
          <div className="flex items-center gap-1">
            {Array.from({ length: 5 }).map((_, i) => (
              <span key={i} className={`text-lg ${i < hearts ? 'text-cyber-red' : 'text-gray-700'}`}>
                {i < hearts ? '♥' : '♡'}
              </span>
            ))}
          </div>

          {/* Streak */}
          <div className="flex items-center gap-1 text-cyber-orange">
            <span>🔥</span>
            <span className="font-mono text-sm font-bold">{streak}</span>
          </div>

          {/* XP */}
          <div className="flex items-center gap-2">
            <div className="w-28 h-2 bg-gray-800 rounded-full overflow-hidden xp-bar">
              <div
                className="h-full bg-gradient-to-r from-cyber-blue to-cyber-green rounded-full transition-all duration-700"
                style={{ width: `${Math.min((xp % 100), 100)}%` }}
              />
            </div>
            <span className="font-mono text-xs text-cyber-blue">{xp} XP</span>
          </div>

          {/* Level */}
          <div className="font-display text-xs font-bold">
            <span className="text-gray-500">LVL </span>
            <span className="text-cyber-yellow glow-yellow">{level}</span>
          </div>

          {/* Username */}
          <div className="font-mono text-xs text-gray-400">
            <span className="text-cyber-green">▶ </span>{username}
          </div>
        </div>
      </div>
    </div>
  );
}

// ─── Mentor Card ──────────────────────────────────────────────────────────────
export function MentorCard({ feedback, tip, show }: {
  feedback: string; tip: string; show: boolean;
}) {
  if (!show) return null;
  return (
    <div className="cyber-panel rounded-lg p-5 border-l-4 border-cyber-purple mt-6 animate-pulse-slow">
      <div className="flex items-start gap-4">
        <div className="flex-shrink-0 w-12 h-12 rounded-full bg-cyber-purple/20 border border-cyber-purple flex items-center justify-center text-2xl">
          🤖
        </div>
        <div>
          <div className="font-display text-xs text-cyber-purple mb-2 tracking-widest">MENTOR FEEDBACK</div>
          <p className="text-gray-200 text-sm leading-relaxed mb-3">{feedback}</p>
          <div className="flex items-start gap-2 bg-cyber-purple/10 rounded p-3">
            <span className="text-cyber-yellow text-sm">💡</span>
            <p className="text-cyber-yellow text-xs leading-relaxed">{tip}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

// ─── XP Popup ─────────────────────────────────────────────────────────────────
export function XPPopup({ xp, show }: { xp: number; show: boolean }) {
  if (!show) return null;
  return (
    <div className="fixed top-24 right-8 z-50 animate-float">
      <div className="bg-cyber-yellow/20 border border-cyber-yellow rounded-lg px-4 py-2 font-display text-cyber-yellow font-bold text-sm glow-yellow">
        +{xp} XP ✨
      </div>
    </div>
  );
}

// ─── Loading Screen ───────────────────────────────────────────────────────────
export function LoadingScreen({ message = 'LOADING...' }: { message?: string }) {
  return (
    <div className="min-h-screen bg-cyber-dark cyber-grid flex items-center justify-center">
      <div className="text-center">
        <div className="relative w-20 h-20 mx-auto mb-6">
          <div className="absolute inset-0 border-2 border-cyber-blue rounded-full animate-spin" />
          <div className="absolute inset-3 border-2 border-cyber-green rounded-full animate-spin" style={{ animationDirection: 'reverse', animationDuration: '0.7s' }} />
          <div className="absolute inset-6 border-2 border-cyber-blue rounded-full animate-spin" style={{ animationDuration: '1.5s' }} />
        </div>
        <p className="font-display text-xs text-cyber-blue tracking-widest animate-pulse">{message}</p>
      </div>
    </div>
  );
}

// ─── Progress Steps ───────────────────────────────────────────────────────────
export function RoomProgress({ current }: { current: number }) {
  const rooms = [
    { num: 1, label: 'KNOWLEDGE TEST', icon: '🧠' },
    { num: 2, label: 'PASSWORD LAB', icon: '🔐' },
    { num: 3, label: 'ACCESS CONTROL', icon: '🛡️' },
  ];
  return (
    <div className="flex items-center justify-center gap-2 mb-8">
      {rooms.map((room, i) => (
        <React.Fragment key={room.num}>
          <div className={`flex items-center gap-2 px-3 py-1.5 rounded border text-xs font-display tracking-wide transition-all
            ${current === room.num ? 'border-cyber-blue bg-cyber-blue/10 text-cyber-blue' :
              current > room.num ? 'border-cyber-green/40 bg-cyber-green/5 text-cyber-green/60' :
              'border-gray-700 text-gray-600'}`}>
            <span>{room.icon}</span>
            <span className="hidden sm:inline">{room.label}</span>
            <span className="sm:hidden">{room.num}</span>
          </div>
          {i < rooms.length - 1 && (
            <div className={`w-8 h-px ${current > room.num + 1 ? 'bg-cyber-green/40' : 'bg-gray-700'}`} />
          )}
        </React.Fragment>
      ))}
    </div>
  );
}

// ─── Badge ────────────────────────────────────────────────────────────────────
export function Badge({ name }: { name: string }) {
  const icons: Record<string, string> = {
    'CyberGuardian': '🛡️',
    'QuizMaster': '🧠',
    'PasswordPro': '🔑',
    'ThreatDetector': '👁️',
  };
  return (
    <div className="flex flex-col items-center gap-2 p-4 bg-cyber-yellow/10 border border-cyber-yellow/40 rounded-lg">
      <span className="text-3xl">{icons[name] || '🏆'}</span>
      <span className="font-display text-xs text-cyber-yellow tracking-wide">{name}</span>
    </div>
  );
}

// ─── Alert ────────────────────────────────────────────────────────────────────
export function Alert({ type, message }: { type: 'error' | 'success' | 'info'; message: string }) {
  const styles = {
    error: 'border-cyber-red/40 bg-cyber-red/10 text-cyber-red',
    success: 'border-cyber-green/40 bg-cyber-green/10 text-cyber-green',
    info: 'border-cyber-blue/40 bg-cyber-blue/10 text-cyber-blue',
  };
  return (
    <div className={`border rounded p-3 text-sm font-mono ${styles[type]}`}>
      {message}
    </div>
  );
}

// ─── Cyber Button ─────────────────────────────────────────────────────────────
export function CyberButton({ children, onClick, variant = 'blue', disabled = false, fullWidth = false, type = 'button' }: {
  children: ReactNode;
  onClick?: () => void;
  variant?: 'blue' | 'green' | 'red' | 'yellow';
  disabled?: boolean;
  fullWidth?: boolean;
  type?: 'button' | 'submit';
}) {
  const colors = {
    blue: 'border-cyber-blue text-cyber-blue hover:bg-cyber-blue/10 hover:shadow-cyber',
    green: 'border-cyber-green text-cyber-green hover:bg-cyber-green/10 hover:shadow-cyber-green',
    red: 'border-cyber-red text-cyber-red hover:bg-cyber-red/10 hover:shadow-cyber-red',
    yellow: 'border-cyber-yellow text-cyber-yellow hover:bg-cyber-yellow/10',
  };
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`border font-display text-xs font-bold tracking-widest uppercase py-3 px-6 transition-all duration-200
        ${colors[variant]} ${fullWidth ? 'w-full' : ''}
        ${disabled ? 'opacity-40 cursor-not-allowed' : 'cursor-pointer hover:-translate-y-0.5'}`}
    >
      {children}
    </button>
  );
}
