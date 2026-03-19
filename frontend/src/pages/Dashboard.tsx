// pages/Dashboard.tsx
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { user as userApi, Progress } from '../api';
import { HUD, LoadingScreen, Badge } from '../components/UI';

export default function Dashboard() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [progress, setProgress] = useState<Progress | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    userApi.profile().then(data => {
      setProgress(data.progress);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, []);

  if (loading) return <LoadingScreen message="LOADING AGENT PROFILE..." />;

  const xp = progress?.xp ?? 0;
  const hearts = progress?.hearts ?? 5;
  const level = Math.max(1, Math.floor(xp / 100));
  const streak = progress?.streak ?? 0;
  const badges: string[] = progress?.badges ? JSON.parse(progress.badges as any) : [];

  const rooms = [
    {
      id: 1,
      num: 'ROOM 01',
      name: 'Knowledge Test',
      desc: 'Test your cybersecurity knowledge with 20 questions from our 300-question bank.',
      icon: '🧠',
      color: 'cyber-blue',
      border: 'border-cyber-blue/40',
      glow: 'hover:shadow-cyber',
      score: progress?.room1_score ?? 0,
      maxScore: 20,
      completed: !!progress?.room1_completed,
      route: '/room1',
      badge: 'Questions',
    },
    {
      id: 2,
      num: 'ROOM 02',
      name: 'Password Lab',
      desc: 'Learn to create strong passwords and simulate real password cracking attacks.',
      icon: '🔐',
      color: 'cyber-green',
      border: 'border-cyber-green/40',
      glow: 'hover:shadow-cyber-green',
      score: progress?.room2_score ?? 0,
      maxScore: 100,
      completed: !!progress?.room2_completed,
      route: '/room2',
      badge: 'Strength',
    },
    {
      id: 3,
      num: 'ROOM 03',
      name: 'Access Control',
      desc: 'Identify phishing attempts and social engineering attacks in real-world scenarios.',
      icon: '🛡️',
      color: 'cyber-purple',
      border: 'border-cyber-purple/40',
      glow: 'hover:shadow-cyber-purple',
      score: progress?.room3_score ?? 0,
      maxScore: 5,
      completed: !!progress?.room3_completed,
      route: '/room3',
      badge: 'Decisions',
    },
  ];

  const allComplete = rooms.every(r => r.completed);

  return (
    <div className="min-h-screen bg-cyber-dark cyber-grid">
      <HUD xp={xp} hearts={hearts} level={level} streak={streak} username={user?.username ?? ''} />

      <div className="pt-20 px-4 pb-8 max-w-6xl mx-auto">
        {/* Welcome */}
        <div className="py-10 text-center">
          <div className="font-mono text-xs text-cyber-green/60 tracking-widest mb-2">
            ▶ AGENT AUTHENTICATED
          </div>
          <h1 className="font-display text-4xl font-black text-white mb-2">
            WELCOME BACK,{' '}
            <span className="text-cyber-blue glow-blue">{user?.username?.toUpperCase()}</span>
          </h1>
          <p className="text-gray-400 font-body text-sm">
            Complete all 3 training rooms to earn your CyberGuardian certification
          </p>
        </div>

        {/* Stats row */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-10">
          {[
            { label: 'Total XP', value: xp, icon: '⚡', color: 'text-cyber-blue' },
            { label: 'Level', value: level, icon: '🏆', color: 'text-cyber-yellow' },
            { label: 'Hearts', value: hearts, icon: '♥', color: 'text-cyber-red' },
            { label: 'Badges', value: badges.length, icon: '🎖️', color: 'text-cyber-purple' },
          ].map(stat => (
            <div key={stat.label} className="cyber-panel rounded-lg p-4 border border-cyber-border text-center">
              <div className="text-2xl mb-1">{stat.icon}</div>
              <div className={`font-display text-2xl font-black ${stat.color}`}>{stat.value}</div>
              <div className="font-mono text-xs text-gray-500 mt-1 tracking-wider">{stat.label}</div>
            </div>
          ))}
        </div>

        {/* Rooms */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          {rooms.map((room) => (
            <div
              key={room.id}
              onClick={() => navigate(room.route)}
              className={`cyber-panel rounded-lg p-6 border ${room.border} cursor-pointer transition-all duration-300 room-card cyber-card`}
            >
              {/* Room header */}
              <div className="flex items-start justify-between mb-4">
                <div>
                  <div className={`font-mono text-xs text-${room.color} tracking-widest mb-1`}>
                    {room.num}
                  </div>
                  <div className="font-display text-lg font-bold text-white">{room.name}</div>
                </div>
                <div className="text-4xl animate-float" style={{ animationDelay: `${room.id * 0.3}s` }}>
                  {room.icon}
                </div>
              </div>

              {/* Description */}
              <p className="text-gray-400 text-sm leading-relaxed mb-5">{room.desc}</p>

              {/* Score bar */}
              {room.completed && (
                <div className="mb-4">
                  <div className="flex justify-between font-mono text-xs text-gray-500 mb-1">
                    <span>BEST SCORE</span>
                    <span className={`text-${room.color}`}>
                      {room.score}/{room.maxScore} {room.badge}
                    </span>
                  </div>
                  <div className="progress-bar">
                    <div
                      className="progress-fill"
                      style={{ width: `${Math.min((room.score / room.maxScore) * 100, 100)}%` }}
                    />
                  </div>
                </div>
              )}

              {/* CTA */}
              <div className={`flex items-center justify-between pt-4 border-t border-cyber-border`}>
                <span className={`font-mono text-xs ${room.completed ? 'text-cyber-green' : `text-${room.color}`}`}>
                  {room.completed ? '✅ COMPLETED' : '▶ START MISSION'}
                </span>
                <span className="text-gray-600 text-lg">→</span>
              </div>
            </div>
          ))}
        </div>

        {/* Completion CTA */}
        {allComplete && (
          <div className="cyber-panel rounded-lg p-6 border border-cyber-yellow/40 text-center mb-10 bg-cyber-yellow/5">
            <div className="text-4xl mb-3">🏆</div>
            <div className="font-display text-xl font-bold text-cyber-yellow glow-yellow mb-2">
              ALL MISSIONS COMPLETE!
            </div>
            <p className="text-gray-400 text-sm mb-4">View your full training report and achievements</p>
            <button
              onClick={() => navigate('/results')}
              className="btn-cyber"
              style={{ borderColor: '#ffd700', color: '#ffd700' }}
            >
              ▶ VIEW FINAL REPORT
            </button>
          </div>
        )}

        {/* Badges */}
        {badges.length > 0 && (
          <div className="cyber-panel rounded-lg p-6 border border-cyber-border">
            <div className="font-display text-sm text-gray-400 tracking-widest mb-4">EARNED BADGES</div>
            <div className="flex flex-wrap gap-4">
              {badges.map(b => <Badge key={b} name={b} />)}
            </div>
          </div>
        )}

        {/* Logout */}
        <div className="text-center mt-8">
          <button
            onClick={logout}
            className="font-mono text-xs text-gray-600 hover:text-gray-400 transition-colors"
          >
            [ LOGOUT ]
          </button>
        </div>
      </div>
    </div>
  );
}
