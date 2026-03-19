// pages/Room3.tsx - Access Control Scenarios
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { room3, Scenario, DecisionResult } from '../api';
import { LoadingScreen, RoomProgress, MentorCard, XPPopup, CyberButton, Alert } from '../components/UI';

type Phase = 'intro' | 'scenario' | 'feedback' | 'complete';

export default function Room3() {
  const navigate = useNavigate();
  const [phase, setPhase] = useState<Phase>('intro');
  const [scenarios, setScenarios] = useState<Scenario[]>([]);
  const [current, setCurrent] = useState(0);
  const [decision, setDecision] = useState<DecisionResult | null>(null);
  const [score, setScore] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [showXP, setShowXP] = useState(false);
  const [xpAmount, setXpAmount] = useState(0);
  const [completionData, setCompletionData] = useState<{ badges: string[] } | null>(null);
  const [finalMentor, setFinalMentor] = useState<{ feedback: string; tip: string } | null>(null);

  useEffect(() => {
    if (phase === 'intro') return;
    room3.scenarios().then(d => setScenarios(d.scenarios)).catch(e => setError(e.message));
  }, [phase]);

  const makeDecision = async (choice: 'grant' | 'deny') => {
    const scenario = scenarios[current];
    setLoading(true);
    setError('');
    try {
      const result = await room3.decide(scenario.id, choice);
      setDecision(result);
      if (result.correct) setScore(s => s + 1);
      setXpAmount(result.xp_earned);
      setShowXP(true);
      setTimeout(() => setShowXP(false), 2000);
      setPhase('feedback');
    } catch (e: any) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  const nextScenario = async () => {
    if (current + 1 < scenarios.length) {
      setCurrent(c => c + 1);
      setDecision(null);
      setPhase('scenario');
    } else {
      // Complete Room 3
      setLoading(true);
      try {
        const finalScore = decision?.correct ? score : score; // already updated
        const data = await room3.complete(score + (decision?.correct ? 0 : 0), scenarios.length);
        setCompletionData(data);
        setFinalMentor(data.mentor);
        setPhase('complete');
      } catch (e: any) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    }
  };

  if (loading && phase !== 'intro') return <LoadingScreen message="ANALYZING THREAT..." />;

  const scenario = scenarios[current];
  const progressPct = scenarios.length > 0 ? ((current) / scenarios.length) * 100 : 0;

  // ── INTRO ────────────────────────────────────────────────────────────────────
  if (phase === 'intro') {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid flex items-center justify-center p-4">
        <div className="max-w-xl w-full">
          <RoomProgress current={3} />
          <div className="cyber-panel rounded-lg p-8 border border-cyber-purple/40 text-center">
            <div className="text-6xl mb-6 animate-float">🛡️</div>
            <div className="font-mono text-xs text-cyber-purple tracking-widest mb-2">ROOM 03</div>
            <h2 className="font-display text-3xl font-black text-white mb-4">ACCESS CONTROL</h2>
            <p className="text-gray-400 leading-relaxed mb-6">
              You are the <span className="text-cyber-purple font-bold">security gatekeeper</span>. Review each scenario — emails, access requests, and communications — then decide: <span className="text-cyber-green font-bold">GRANT ACCESS</span> or <span className="text-cyber-red font-bold">DENY ACCESS</span>.
            </p>

            <div className="grid grid-cols-2 gap-4 mb-8">
              {[
                { icon: '📧', label: '5 Scenarios', sub: 'Real-world threats' },
                { icon: '🎯', label: 'Identify threats', sub: 'Phishing & social eng.' },
                { icon: '⚡', label: 'Up to 35 XP', sub: 'Per correct decision' },
                { icon: '🏆', label: 'Earn badge', sub: 'Complete all rooms' },
              ].map(item => (
                <div key={item.label} className="border border-cyber-border rounded p-3 bg-cyber-panel/50">
                  <div className="text-lg mb-1">{item.icon}</div>
                  <div className="font-mono text-xs text-cyber-purple">{item.label}</div>
                  <div className="font-mono text-xs text-gray-500">{item.sub}</div>
                </div>
              ))}
            </div>

            {error && <Alert type="error" message={error} />}

            <div className="flex gap-3 justify-center">
              <CyberButton onClick={() => navigate('/')} variant="red">← BACK</CyberButton>
              <CyberButton
                onClick={() => { setPhase('scenario'); }}
                variant="blue"
              >
                ▶ BEGIN MISSION
              </CyberButton>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // ── SCENARIO ─────────────────────────────────────────────────────────────────
  if (phase === 'scenario' && scenario) {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <XPPopup xp={xpAmount} show={showXP} />
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={3} />

          {/* Progress */}
          <div className="mb-6">
            <div className="flex justify-between font-mono text-xs text-gray-500 mb-2">
              <span>SCENARIO {current + 1} of {scenarios.length}</span>
              <span className="text-cyber-purple">SCORE: {score}/{current}</span>
            </div>
            <div className="progress-bar">
              <div className="h-full bg-gradient-to-r from-cyber-purple to-cyber-blue rounded-full transition-all" style={{ width: `${progressPct}%` }} />
            </div>
          </div>

          {/* Scenario Title */}
          <div className="cyber-panel rounded-lg p-4 border border-cyber-purple/30 mb-4">
            <div className="flex items-center gap-3 mb-2">
              <span className="text-2xl">{scenario.type === 'email' ? '📧' : '🔑'}</span>
              <div>
                <div className="font-mono text-xs text-cyber-purple tracking-wider">
                  {scenario.type === 'email' ? 'INCOMING EMAIL' : 'ACCESS REQUEST'}
                </div>
                <div className="font-display text-lg font-bold text-white">{scenario.title}</div>
              </div>
            </div>
          </div>

          {/* Email/Request Preview */}
          <div className="bg-gray-900 rounded-lg border border-gray-700 mb-6 overflow-hidden">
            {/* Email header */}
            <div className="bg-gray-800 px-4 py-3 border-b border-gray-700">
              <div className="grid grid-cols-[60px_1fr] gap-2 text-xs font-mono">
                <span className="text-gray-500">FROM:</span>
                <span className="text-cyber-yellow">{scenario.sender}</span>
                <span className="text-gray-500">SUBJ:</span>
                <span className="text-gray-300">{scenario.subject}</span>
              </div>
            </div>
            {/* Body */}
            <div className="p-5">
              <p className="text-gray-300 text-sm leading-relaxed whitespace-pre-line">{scenario.body}</p>
              {scenario.attachments && scenario.attachments.length > 0 && (
                <div className="mt-4 flex flex-wrap gap-2">
                  {scenario.attachments.map((a, i) => (
                    <div key={i} className="bg-gray-800 border border-gray-700 rounded px-3 py-1 font-mono text-xs text-cyber-yellow flex items-center gap-1">
                      <span>📎</span> {a}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Clue hints (subtle) */}
          <div className="font-mono text-xs text-gray-600 mb-6">
            ⚡ Examine the sender, content, and urgency carefully before deciding
          </div>

          {error && <Alert type="error" message={error} />}

          {/* Decision buttons */}
          <div className="grid grid-cols-2 gap-4">
            <button
              onClick={() => makeDecision('deny')}
              disabled={loading}
              className="cyber-panel border-2 border-cyber-red/50 rounded-lg p-5 text-center hover:border-cyber-red hover:bg-cyber-red/10 transition-all duration-200 cursor-pointer group disabled:opacity-40"
            >
              <div className="text-4xl mb-3 group-hover:scale-110 transition-transform">🚫</div>
              <div className="font-display text-sm font-bold text-cyber-red tracking-widest">DENY</div>
              <div className="font-mono text-xs text-gray-500 mt-1">Block this threat</div>
            </button>
            <button
              onClick={() => makeDecision('grant')}
              disabled={loading}
              className="cyber-panel border-2 border-cyber-green/50 rounded-lg p-5 text-center hover:border-cyber-green hover:bg-cyber-green/10 transition-all duration-200 cursor-pointer group disabled:opacity-40"
            >
              <div className="text-4xl mb-3 group-hover:scale-110 transition-transform">✅</div>
              <div className="font-display text-sm font-bold text-cyber-green tracking-widest">GRANT</div>
              <div className="font-mono text-xs text-gray-500 mt-1">Allow this request</div>
            </button>
          </div>
        </div>
      </div>
    );
  }

  // ── FEEDBACK ──────────────────────────────────────────────────────────────────
  if (phase === 'feedback' && decision) {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <XPPopup xp={xpAmount} show={showXP} />
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={3} />

          {/* Result */}
          <div className={`cyber-panel rounded-lg p-6 border mb-6 text-center ${decision.correct ? 'border-cyber-green/50' : 'border-cyber-red/50'}`}>
            <div className="text-5xl mb-3">{decision.correct ? '✅' : '❌'}</div>
            <div className={`font-display text-2xl font-bold mb-1 ${decision.correct ? 'text-cyber-green' : 'text-cyber-red'}`}>
              {decision.correct ? 'CORRECT DECISION' : 'WRONG DECISION'}
            </div>
            <div className="font-mono text-xs text-gray-500">
              Correct action: <span className={decision.correct_decision === 'deny' ? 'text-cyber-red' : 'text-cyber-green'}>
                {decision.correct_decision.toUpperCase()}
              </span>
            </div>
            <div className="mt-3 inline-block bg-cyber-yellow/10 border border-cyber-yellow/30 rounded px-4 py-1">
              <span className="font-display text-cyber-yellow font-bold">+{decision.xp_earned} XP</span>
            </div>
          </div>

          {/* Mistake type — educational nuance */}
          {!decision.correct && (decision as any).mistake_label && (
            <div className="cyber-panel rounded-lg p-4 border border-cyber-orange/40 bg-cyber-orange/5 mb-4">
              <p className="font-mono text-xs text-cyber-orange leading-relaxed">{(decision as any).mistake_label}</p>
            </div>
          )}

          {/* Threat type + severity */}
          <div className="cyber-panel rounded-lg p-4 border border-cyber-red/30 mb-4 flex items-center justify-between">
            <div>
              <div className="font-mono text-xs text-cyber-red tracking-wider mb-1">⚠️ THREAT IDENTIFIED</div>
              <div className="font-display text-base font-bold text-white">{decision.threat_type}</div>
            </div>
            {(decision as any).severity && (
              <div className={`font-mono text-xs px-3 py-1 rounded border uppercase font-bold ${
                (decision as any).severity === 'critical' ? 'border-cyber-red text-cyber-red bg-cyber-red/10' :
                (decision as any).severity === 'high' ? 'border-cyber-orange text-cyber-orange bg-cyber-orange/10' :
                'border-cyber-yellow text-cyber-yellow bg-cyber-yellow/10'
              }`}>{(decision as any).severity}</div>
            )}
          </div>

          {/* Explanation */}
          <div className="cyber-panel rounded-lg p-5 border border-cyber-blue/30 mb-4">
            <div className="font-mono text-xs text-cyber-blue tracking-wider mb-2">ANALYSIS</div>
            <p className="text-gray-300 text-sm leading-relaxed">{decision.explanation}</p>
          </div>

          {/* Clues */}
          <div className="cyber-panel rounded-lg p-5 border border-cyber-yellow/30 mb-6">
            <div className="font-mono text-xs text-cyber-yellow tracking-wider mb-3">🔍 RED FLAGS TO NOTICE</div>
            <div className="space-y-2">
              {decision.clues.map((clue, i) => (
                <div key={i} className="flex items-center gap-2 font-mono text-xs text-gray-300">
                  <span className="text-cyber-yellow">⚡</span>
                  {clue}
                </div>
              ))}
            </div>
          </div>

          {error && <Alert type="error" message={error} />}

          <CyberButton
            onClick={nextScenario}
            variant="blue"
            fullWidth
            disabled={loading}
          >
            {current + 1 < scenarios.length ? '▶ NEXT SCENARIO' : '▶ COMPLETE MISSION'}
          </CyberButton>
        </div>
      </div>
    );
  }

  // ── COMPLETE ──────────────────────────────────────────────────────────────────
  if (phase === 'complete') {
    const pct = Math.round((score / scenarios.length) * 100);
    const badges = completionData?.badges ?? [];
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={3} />

          <div className="cyber-panel rounded-lg p-8 border border-cyber-purple/40 text-center mb-6">
            <div className="text-6xl mb-4 animate-float">🛡️</div>
            <div className="font-mono text-xs text-cyber-purple tracking-widest mb-2">ROOM 03 COMPLETE</div>
            <h2 className="font-display text-3xl font-black text-white mb-2">MISSION ACCOMPLISHED</h2>
            <div className="font-display text-5xl font-black text-cyber-purple mt-4">{score}/{scenarios.length}</div>
            <div className="font-mono text-lg text-gray-400">{pct}% ACCURACY</div>
          </div>

          {finalMentor && (
            <MentorCard feedback={finalMentor.feedback} tip={finalMentor.tip} show={true} />
          )}

          {badges.length > 0 && (
            <div className="cyber-panel rounded-lg p-6 border border-cyber-yellow/40 mt-6 text-center">
              <div className="text-4xl mb-3">🏆</div>
              <div className="font-display text-xl font-bold text-cyber-yellow glow-yellow mb-2">
                {completionData && (completionData as any).new_badges?.length > 0 ? 'NEW BADGES EARNED!' : 'YOUR BADGES'}
              </div>
              <div className="flex justify-center gap-4 flex-wrap">
                {badges.map(b => (
                  <div key={b} className={`border rounded-lg px-6 py-3 ${
                    (completionData as any).new_badges?.includes(b)
                      ? 'bg-cyber-yellow/20 border-cyber-yellow animate-pulse'
                      : 'bg-cyber-yellow/10 border-cyber-yellow/40'
                  }`}>
                    <div className="text-2xl">🛡️</div>
                    <div className="font-display text-xs text-cyber-yellow">{b}</div>
                    {(completionData as any).new_badges?.includes(b) && (
                      <div className="font-mono text-xs text-cyber-green mt-1">NEW!</div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="flex gap-3 mt-6">
            <CyberButton onClick={() => navigate('/')} variant="red" fullWidth>← DASHBOARD</CyberButton>
            <CyberButton onClick={() => navigate('/results')} variant="green" fullWidth>🏆 FINAL REPORT</CyberButton>
          </div>
        </div>
      </div>
    );
  }

  return <LoadingScreen />;
}
