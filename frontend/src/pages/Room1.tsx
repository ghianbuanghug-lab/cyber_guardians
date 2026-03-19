// pages/Room1.tsx - Knowledge Quiz
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { room1, Question, Room1Result } from '../api';
import { LoadingScreen, MentorCard, RoomProgress, XPPopup, CyberButton, Alert } from '../components/UI';

type Phase = 'intro' | 'quiz' | 'results';

export default function Room1() {
  const navigate = useNavigate();
  const [phase, setPhase] = useState<Phase>('intro');
  const [questions, setQuestions] = useState<Question[]>([]);
  const [sessionId, setSessionId] = useState<number | null>(null);
  const [currentQ, setCurrentQ] = useState(0);
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [selected, setSelected] = useState<number | null>(null);
  const [showExplain, setShowExplain] = useState(false);
  const [result, setResult] = useState<Room1Result | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [showXP, setShowXP] = useState(false);
  const [timeLeft, setTimeLeft] = useState(30);
  const [timerActive, setTimerActive] = useState(false);

  useEffect(() => {
    if (!timerActive || phase !== 'quiz') return;
    if (timeLeft <= 0) { handleSkip(); return; }
    const t = setTimeout(() => setTimeLeft(prev => prev - 1), 1000);
    return () => clearTimeout(t);
  }, [timeLeft, timerActive, phase]);

  const startQuiz = async () => {
    setLoading(true); setError('');
    try {
      const data = await room1.start();
      setQuestions(data.questions); setSessionId(data.session_id);
      setPhase('quiz'); setCurrentQ(0); setAnswers({});
      setSelected(null); setTimeLeft(30); setTimerActive(true);
    } catch (e: any) { setError(e.message); }
    finally { setLoading(false); }
  };

  const handleAnswer = (idx: number) => {
    if (selected !== null) return;
    setSelected(idx); setTimerActive(false); setShowExplain(true);
    setAnswers(prev => ({ ...prev, [String(currentQ)]: idx }));
  };

  const handleSkip = () => { setTimerActive(false); setShowExplain(true); setSelected(-1); };

  const nextQuestion = () => {
    if (currentQ < questions.length - 1) {
      setCurrentQ(q => q + 1); setSelected(null);
      setShowExplain(false); setTimeLeft(30); setTimerActive(true);
    } else { submitQuiz(); }
  };

  const submitQuiz = async () => {
    setLoading(true);
    try {
      const data = await room1.submit(sessionId!, answers);
      setResult(data); setPhase('results');
      setShowXP(true); setTimeout(() => setShowXP(false), 3000);
    } catch (e: any) { setError(e.message); }
    finally { setLoading(false); }
  };

  if (loading) return <LoadingScreen message="INITIALIZING KNOWLEDGE TEST..." />;

  const q = questions[currentQ];
  const progress = ((currentQ + (selected !== null ? 1 : 0)) / 20) * 100;
  const timerPct = (timeLeft / 30) * 100;

  if (phase === 'intro') {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid flex items-center justify-center p-4">
        <div className="max-w-xl w-full">
          <RoomProgress current={1} />
          <div className="cyber-panel rounded-lg p-8 border border-cyber-blue/40 text-center">
            <div className="text-6xl mb-6 animate-float">🧠</div>
            <div className="font-mono text-xs text-cyber-blue tracking-widest mb-2">ROOM 01</div>
            <h2 className="font-display text-3xl font-black text-white mb-4">KNOWLEDGE TEST</h2>
            <p className="text-gray-400 leading-relaxed mb-6">
              You will be tested on <span className="text-cyber-blue font-bold">20 cybersecurity questions</span> from
              our 300+ question bank. You have <span className="text-cyber-yellow font-bold">30 seconds</span> per question.
            </p>
            <div className="grid grid-cols-2 gap-4 mb-8 text-left">
              {[
                { icon: '❓', label: '20 Questions', sub: 'Random selection' },
                { icon: '⏱️', label: '30 sec each', sub: 'Timer per question' },
                { icon: '⭐', label: '10 XP each', sub: 'Correct answer' },
                { icon: '📊', label: 'Detailed review', sub: 'After submission' },
              ].map(item => (
                <div key={item.label} className="border border-cyber-border rounded p-3 bg-cyber-panel/50">
                  <div className="text-lg mb-1">{item.icon}</div>
                  <div className="font-mono text-xs text-cyber-blue">{item.label}</div>
                  <div className="font-mono text-xs text-gray-500">{item.sub}</div>
                </div>
              ))}
            </div>
            {error && <Alert type="error" message={error} />}
            <div className="flex gap-3 justify-center">
              <CyberButton onClick={() => navigate('/')} variant="red">← BACK</CyberButton>
              <CyberButton onClick={startQuiz} variant="blue">▶ BEGIN TEST</CyberButton>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (phase === 'quiz' && q) {
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={1} />
          <div className="mb-6">
            <div className="flex justify-between font-mono text-xs text-gray-500 mb-2">
              <span>QUESTION {currentQ + 1} of {questions.length}</span>
              <span className={timeLeft <= 10 ? 'text-cyber-red animate-pulse' : 'text-cyber-blue'}>⏱ {timeLeft}s</span>
            </div>
            <div className="progress-bar mb-2"><div className="progress-fill" style={{ width: `${progress}%` }} /></div>
            <div className="h-1 bg-gray-800 rounded-full overflow-hidden">
              <div className={`h-full rounded-full transition-all duration-1000 ${timeLeft <= 10 ? 'bg-cyber-red' : 'bg-cyber-yellow'}`} style={{ width: `${timerPct}%` }} />
            </div>
          </div>
          <div className="cyber-panel rounded-lg p-6 border border-cyber-blue/30 mb-6">
            <div className="font-mono text-xs text-cyber-blue/60 tracking-widest mb-3">CYBERSECURITY QUESTION</div>
            <h3 className="font-body text-lg text-white leading-relaxed">{q.question}</h3>
          </div>
          <div className="space-y-3 mb-6">
            {q.options.map((opt, i) => {
              let style = 'border-cyber-border text-gray-300 hover:border-cyber-blue/60 cursor-pointer';
              if (selected !== null) {
                style = i === selected && selected >= 0
                  ? 'border-cyber-blue/60 bg-cyber-blue/10 text-white cursor-default'
                  : 'border-gray-700 text-gray-500 cursor-default opacity-60';
              }
              return (
                <button key={i} onClick={() => handleAnswer(i)} disabled={selected !== null}
                  className={`w-full text-left border rounded-lg p-4 transition-all duration-200 ${style} font-body text-sm leading-relaxed`}>
                  <span className="font-mono text-cyber-blue/60 mr-3">{String.fromCharCode(65 + i)}.</span>{opt}
                </button>
              );
            })}
          </div>
          {showExplain && q.explain && (
            <div className="cyber-panel rounded-lg p-4 border border-cyber-yellow/30 bg-cyber-yellow/5 mb-6">
              <div className="font-mono text-xs text-cyber-yellow tracking-wider mb-2">💡 EXPLANATION</div>
              <p className="text-gray-300 text-sm leading-relaxed">{q.explain}</p>
            </div>
          )}
          {selected !== null && (
            <CyberButton onClick={nextQuestion} fullWidth variant="blue" disabled={loading}>
              {currentQ < questions.length - 1 ? '▶ NEXT QUESTION' : '▶ SUBMIT ANSWERS'}
            </CyberButton>
          )}
        </div>
      </div>
    );
  }

  if (phase === 'results' && result) {
    const pct = result.percentage;
    const grade = pct >= 90 ? 'S' : pct >= 75 ? 'A' : pct >= 60 ? 'B' : pct >= 45 ? 'C' : 'D';
    const gradeColor = ({ S: 'cyber-blue', A: 'cyber-green', B: 'cyber-yellow', C: 'cyber-orange', D: 'cyber-red' } as Record<string,string>)[grade];
    return (
      <div className="min-h-screen bg-cyber-dark cyber-grid p-4 pt-8">
        <XPPopup xp={result.xp_earned} show={showXP} />
        <div className="max-w-2xl mx-auto">
          <RoomProgress current={1} />
          <div className="cyber-panel rounded-lg p-8 border border-cyber-blue/40 text-center mb-6">
            <div className="font-mono text-xs text-cyber-blue tracking-widest mb-4">ROOM 01 COMPLETE</div>
            <div className={`font-display text-8xl font-black text-${gradeColor} mb-2`}>{grade}</div>
            <div className="font-display text-3xl font-bold text-white mb-1">{result.score} / {result.total}</div>
            <div className="font-mono text-lg text-cyber-blue">{pct}% ACCURACY</div>
            <div className="mt-4 inline-block bg-cyber-yellow/10 border border-cyber-yellow/40 rounded px-4 py-2">
              <span className="font-display text-cyber-yellow font-bold">+{result.xp_earned} XP EARNED</span>
            </div>
          </div>
          <MentorCard feedback={result.mentor.feedback} tip={result.mentor.tip} show={true} />
          {result.new_badges && result.new_badges.length > 0 && (
            <div className="cyber-panel rounded-lg p-5 border border-cyber-yellow/50 bg-cyber-yellow/5 mb-6 text-center">
              <div className="text-3xl mb-2">🏆</div>
              <div className="font-display text-sm font-bold text-cyber-yellow mb-3">BADGE{result.new_badges.length > 1 ? 'S' : ''} UNLOCKED!</div>
              <div className="flex justify-center gap-3 flex-wrap">
                {result.new_badges.map((b: string) => (
                  <div key={b} className="bg-cyber-yellow/20 border border-cyber-yellow rounded-lg px-4 py-2">
                    <div className="font-display text-xs text-cyber-yellow">{b}</div>
                  </div>
                ))}
              </div>
            </div>
          )}
          {result.category_stats && Object.keys(result.category_stats).length > 0 && (
            <div className="cyber-panel rounded-lg p-5 border border-cyber-border mb-6">
              <div className="font-display text-xs text-gray-400 tracking-widest mb-4">PERFORMANCE BY CATEGORY</div>
              <div className="space-y-3">
                {Object.entries(result.category_stats).map(([cat, stats]) => {
                  const catPct = Math.round((stats.correct / stats.total) * 100);
                  return (
                    <div key={cat}>
                      <div className="flex justify-between font-mono text-xs mb-1">
                        <span className="text-gray-400">{cat}</span>
                        <span className={catPct >= 70 ? 'text-cyber-green' : catPct >= 50 ? 'text-cyber-yellow' : 'text-cyber-red'}>{stats.correct}/{stats.total}</span>
                      </div>
                      <div className="h-1.5 bg-gray-800 rounded-full overflow-hidden">
                        <div className={`h-full rounded-full transition-all duration-500 ${catPct >= 70 ? 'bg-cyber-green' : catPct >= 50 ? 'bg-cyber-yellow' : 'bg-cyber-red'}`} style={{ width: `${catPct}%` }} />
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
          <div className="space-y-3 mb-6">
            <div className="font-display text-sm text-gray-400 tracking-widest">ANSWER REVIEW</div>
            {result.results.map((r, i) => (
              <div key={i} className={`cyber-panel rounded-lg p-4 border ${r.correct ? 'border-cyber-green/30' : 'border-cyber-red/30'}`}>
                <div className="flex items-start gap-3">
                  <span className={`text-lg flex-shrink-0 ${r.correct ? 'text-cyber-green' : 'text-cyber-red'}`}>{r.correct ? '✓' : '✗'}</span>
                  <div>
                    <p className="text-sm text-white mb-2">{r.question}</p>
                    {!r.correct && <p className="font-mono text-xs text-cyber-red/80 mb-1">Your answer: {r.your_answer >= 0 ? r.options[r.your_answer] : 'Timed out'}</p>}
                    <p className={`font-mono text-xs ${r.correct ? 'text-cyber-green/80' : 'text-cyber-green'}`}>✓ Correct: {r.options[r.correct_answer]}</p>
                    {r.explain && <p className="text-xs text-gray-500 mt-2 leading-relaxed">{r.explain}</p>}
                  </div>
                </div>
              </div>
            ))}
          </div>
          <div className="flex gap-3 mt-4">
            <CyberButton onClick={() => navigate('/')} variant="red" fullWidth>← DASHBOARD</CyberButton>
            <CyberButton onClick={() => navigate('/room2')} variant="green" fullWidth>ROOM 02 →</CyberButton>
          </div>
        </div>
      </div>
    );
  }

  return <LoadingScreen />;
}
