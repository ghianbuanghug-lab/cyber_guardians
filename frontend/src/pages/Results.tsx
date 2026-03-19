// pages/Results.tsx - Final Results & Certificate
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { results, FinalResults } from '../api';
import { LoadingScreen, Badge, MentorCard } from '../components/UI';

export default function ResultsPage() {
  const navigate = useNavigate();
  const [data, setData] = useState<FinalResults | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [revealed, setRevealed] = useState(false);

  useEffect(() => {
    results.final()
      .then(d => { setData(d); setLoading(false); setTimeout(() => setRevealed(true), 200); })
      .catch(e => { setError(e.message); setLoading(false); });
  }, []);

  if (loading) return <LoadingScreen message="COMPILING FINAL REPORT..." />;
  if (!data || error) {
    return (
      <div className="min-h-screen bg-cyber-dark flex items-center justify-center">
        <div className="text-center">
          <div className="text-cyber-red font-mono text-sm mb-4">{error || 'No data found'}</div>
          <button onClick={() => navigate('/')} className="btn-cyber">← DASHBOARD</button>
        </div>
      </div>
    );
  }

  const allComplete = data.rooms_completed.room1 && data.rooms_completed.room2 && data.rooms_completed.room3;
  const xpPct = Math.min((data.xp % 100), 100);

  const roomCards = [
    { label: 'ROOM 01', name: 'Knowledge Test', icon: '🧠', score: data.room_scores.room1, max: 20, done: data.rooms_completed.room1, color: 'cyber-blue' },
    { label: 'ROOM 02', name: 'Password Lab', icon: '🔐', score: data.room_scores.room2, max: 100, done: data.rooms_completed.room2, color: 'cyber-green' },
    { label: 'ROOM 03', name: 'Access Control', icon: '🛡️', score: data.room_scores.room3, max: 5, done: data.rooms_completed.room3, color: 'cyber-purple' },
  ];

  return (
    <div className="min-h-screen bg-cyber-dark cyber-grid p-4 py-10">
      <div className="max-w-3xl mx-auto">

        {/* Header */}
        <div className={`text-center mb-10 transition-all duration-700 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
          <div className="text-6xl mb-4 animate-float">{allComplete ? '🏆' : '📊'}</div>
          <div className="font-mono text-xs text-cyber-blue tracking-widest mb-2">CYBERGUARDIAN TRAINING REPORT</div>
          <h1 className="font-display text-4xl font-black text-white">
            {allComplete ? 'CONGRATULATIONS' : 'PROGRESS REPORT'}
          </h1>
          <p className="text-gray-400 font-display text-lg mt-2 tracking-wider">
            AGENT: <span className="text-cyber-blue glow-blue">{data.username.toUpperCase()}</span>
          </p>
        </div>

        {/* Certificate (if all complete) */}
        {allComplete && (
          <div className={`mb-8 transition-all duration-700 delay-100 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
            <div className="relative border-2 border-cyber-yellow rounded-lg p-8 text-center overflow-hidden">
              {/* Corner decorations */}
              <div className="absolute top-2 left-2 w-6 h-6 border-t-2 border-l-2 border-cyber-yellow" />
              <div className="absolute top-2 right-2 w-6 h-6 border-t-2 border-r-2 border-cyber-yellow" />
              <div className="absolute bottom-2 left-2 w-6 h-6 border-b-2 border-l-2 border-cyber-yellow" />
              <div className="absolute bottom-2 right-2 w-6 h-6 border-b-2 border-r-2 border-cyber-yellow" />

              <div className="font-mono text-xs text-cyber-yellow/60 tracking-widest mb-4">CERTIFICATE OF COMPLETION</div>
              <div className="font-display text-2xl font-black text-cyber-yellow glow-yellow mb-2">
                CERTIFIED CYBER GUARDIAN
              </div>
              <p className="text-gray-300 text-sm mb-4">
                This certifies that <span className="text-white font-bold">{data.username}</span> has successfully completed
                all CyberGuardian Security Awareness training modules.
              </p>
              <div className="text-3xl">🛡️ 🧠 🔐</div>
              <div className="font-mono text-xs text-gray-600 mt-4">
                Total XP: {data.xp} | Level: {data.level} | Score: {data.total_score}
              </div>
            </div>
          </div>
        )}

        {/* Stats Grid */}
        <div className={`grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8 transition-all duration-700 delay-200 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
          {[
            { icon: '⚡', label: 'Total XP', value: data.xp, color: 'text-cyber-blue' },
            { icon: '🏆', label: 'Level', value: data.level, color: 'text-cyber-yellow' },
            { icon: '❤️', label: 'Hearts', value: data.hearts, color: 'text-cyber-red' },
            { icon: '📊', label: 'Total Score', value: data.total_score, color: 'text-cyber-green' },
          ].map(stat => (
            <div key={stat.label} className="cyber-panel rounded-lg p-4 border border-cyber-border text-center">
              <div className="text-2xl mb-1">{stat.icon}</div>
              <div className={`font-display text-2xl font-black ${stat.color}`}>{stat.value}</div>
              <div className="font-mono text-xs text-gray-500 mt-1 tracking-wider">{stat.label}</div>
            </div>
          ))}
        </div>

        {/* XP Progress */}
        <div className={`cyber-panel rounded-lg p-5 border border-cyber-border mb-6 transition-all duration-700 delay-300 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
          <div className="flex justify-between font-mono text-xs text-gray-400 mb-2">
            <span>LEVEL {data.level} PROGRESS</span>
            <span className="text-cyber-blue">{data.xp} / {(data.level + 1) * 100} XP</span>
          </div>
          <div className="h-3 bg-gray-800 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-cyber-blue to-cyber-green rounded-full transition-all duration-1000"
              style={{ width: `${xpPct}%` }}
            />
          </div>
        </div>

        {/* Room Performance */}
        <div className={`grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8 transition-all duration-700 delay-400 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
          {roomCards.map(room => (
            <div
              key={room.label}
              className={`cyber-panel rounded-lg p-5 border text-center ${room.done ? `border-${room.color}/40` : 'border-gray-800 opacity-50'}`}
            >
              <div className="text-3xl mb-2">{room.icon}</div>
              <div className={`font-mono text-xs text-${room.color} tracking-wider mb-1`}>{room.label}</div>
              <div className="font-body text-sm text-gray-400 mb-3">{room.name}</div>
              {room.done ? (
                <>
                  <div className={`font-display text-xl font-black text-${room.color}`}>
                    {room.score}/{room.max}
                  </div>
                  <div className="font-mono text-xs text-gray-500">BEST SCORE</div>
                  <div className="mt-3 h-1.5 bg-gray-800 rounded-full overflow-hidden">
                    <div
                      className={`h-full bg-${room.color} rounded-full`}
                      style={{ width: `${Math.min((room.score / room.max) * 100, 100)}%` }}
                    />
                  </div>
                </>
              ) : (
                <div className="font-mono text-xs text-gray-600">NOT COMPLETED</div>
              )}
            </div>
          ))}
        </div>

        {/* Badges — show all 8, highlight earned ones */}
        <div className={`cyber-panel rounded-lg p-6 border border-cyber-border mb-8 transition-all duration-700 delay-500 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
          <div className="flex justify-between items-center mb-4">
            <div className="font-display text-sm text-gray-400 tracking-widest">BADGE COLLECTION</div>
            <div className="font-mono text-xs text-cyber-yellow">{data.badges.length} / {data.all_badges?.length ?? 8} earned</div>
          </div>
          <div className="grid grid-cols-2 gap-3">
            {(data.all_badges ?? data.badges).map(b => {
              const earned = data.badges.includes(b);
              const desc = data.badge_definitions?.[b] ?? '';
              return (
                <div key={b} className={`rounded-lg p-3 border flex items-center gap-3 ${earned ? 'border-cyber-yellow/50 bg-cyber-yellow/5' : 'border-gray-800 bg-black/20 opacity-40'}`}>
                  <div className="text-xl">{earned ? '🏅' : '🔒'}</div>
                  <div>
                    <div className={`font-display text-xs font-bold ${earned ? 'text-cyber-yellow' : 'text-gray-600'}`}>{b}</div>
                    {desc && <div className="font-mono text-xs text-gray-600 mt-0.5">{desc}</div>}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Mentor Feedback */}
        {data.mentor_feedback.length > 0 && (
          <div className={`mb-8 transition-all duration-700 delay-600 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
            <div className="font-display text-sm text-gray-400 tracking-widest mb-4">MENTOR FEEDBACK SUMMARY</div>
            <div className="space-y-4">
              {data.mentor_feedback.slice(0, 3).map((f, i) => (
                <MentorCard key={i} feedback={f.feedback} tip={f.tip} show={true} />
              ))}
            </div>
          </div>
        )}

        {/* CTA */}
        <div className={`flex flex-wrap gap-3 justify-center transition-all duration-700 delay-700 ${revealed ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
          <button
            onClick={() => navigate('/')}
            className="btn-cyber"
          >
            ← DASHBOARD
          </button>
          {!data.rooms_completed.room1 && (
            <button onClick={() => navigate('/room1')} className="btn-cyber btn-cyber-green">
              START ROOM 01
            </button>
          )}
          {data.rooms_completed.room1 && !data.rooms_completed.room2 && (
            <button onClick={() => navigate('/room2')} className="btn-cyber btn-cyber-green">
              START ROOM 02
            </button>
          )}
          {data.rooms_completed.room2 && !data.rooms_completed.room3 && (
            <button onClick={() => navigate('/room3')} className="btn-cyber btn-cyber-green">
              START ROOM 03
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
