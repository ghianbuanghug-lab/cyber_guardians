// pages/AuthPage.tsx
import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { Alert, CyberButton } from '../components/UI';

export default function AuthPage() {
  const { login, register } = useAuth();
  const [mode, setMode] = useState<'login' | 'register'>('login');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setError('');
    setLoading(true);
    try {
      if (mode === 'login') {
        await login(username, password);
      } else {
        await register(username, password, email || undefined);
      }
    } catch (e: any) {
      setError(e.message || 'Authentication failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-cyber-dark cyber-grid scanline flex items-center justify-center p-4">
      {/* Background particles */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        {[...Array(20)].map((_, i) => (
          <div
            key={i}
            className="absolute w-1 h-1 bg-cyber-blue/30 rounded-full animate-float"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 3}s`,
              animationDuration: `${2 + Math.random() * 3}s`,
            }}
          />
        ))}
      </div>

      <div className="w-full max-w-md relative z-10">
        {/* Logo */}
        <div className="text-center mb-10">
          <div className="relative inline-block mb-4">
            <div className="w-20 h-20 mx-auto relative">
              <div className="absolute inset-0 border-2 border-cyber-blue rotate-45 animate-pulse-slow" />
              <div className="absolute inset-2 border-2 border-cyber-green rotate-45" />
              <div className="absolute inset-0 flex items-center justify-center text-3xl">🛡️</div>
            </div>
          </div>
          <h1 className="font-display text-3xl font-black text-cyber-blue glow-blue tracking-widest">
            CYBERGUARDIAN
          </h1>
          <p className="font-mono text-xs text-gray-500 mt-2 tracking-wider">
            CYBERSECURITY AWARENESS TRAINING SYSTEM v1.0
          </p>
        </div>

        {/* Card */}
        <div className="cyber-panel rounded-lg p-8 border border-cyber-blue/20 shadow-cyber">
          {/* Tab switcher */}
          <div className="flex mb-8 border border-cyber-blue/20 rounded">
            <button
              onClick={() => { setMode('login'); setError(''); }}
              className={`flex-1 py-2.5 font-display text-xs tracking-widest transition-all
                ${mode === 'login' ? 'bg-cyber-blue/20 text-cyber-blue' : 'text-gray-500 hover:text-gray-300'}`}
            >
              LOGIN
            </button>
            <button
              onClick={() => { setMode('register'); setError(''); }}
              className={`flex-1 py-2.5 font-display text-xs tracking-widest transition-all
                ${mode === 'register' ? 'bg-cyber-blue/20 text-cyber-blue' : 'text-gray-500 hover:text-gray-300'}`}
            >
              REGISTER
            </button>
          </div>

          <div className="space-y-4">
            <div>
              <label className="font-mono text-xs text-gray-400 mb-1.5 block tracking-wider">
                USERNAME
              </label>
              <input
                type="text"
                value={username}
                onChange={e => setUsername(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && handleSubmit()}
                className="cyber-input rounded"
                placeholder="enter_username"
                autoComplete="username"
              />
            </div>

            {mode === 'register' && (
              <div>
                <label className="font-mono text-xs text-gray-400 mb-1.5 block tracking-wider">
                  EMAIL <span className="text-gray-600">(optional)</span>
                </label>
                <input
                  type="email"
                  value={email}
                  onChange={e => setEmail(e.target.value)}
                  className="cyber-input rounded"
                  placeholder="agent@domain.com"
                />
              </div>
            )}

            <div>
              <label className="font-mono text-xs text-gray-400 mb-1.5 block tracking-wider">
                PASSWORD
              </label>
              <input
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && handleSubmit()}
                className="cyber-input rounded"
                placeholder="••••••••••••"
                autoComplete={mode === 'login' ? 'current-password' : 'new-password'}
              />
            </div>

            {error && <Alert type="error" message={error} />}

            <div className="pt-2">
              <CyberButton
                onClick={handleSubmit}
                disabled={loading}
                fullWidth
                variant="blue"
              >
                {loading ? 'AUTHENTICATING...' : mode === 'login' ? '▶ ENTER SYSTEM' : '▶ CREATE AGENT'}
              </CyberButton>
            </div>
          </div>
        </div>

        {/* Footer hint */}
        <p className="text-center font-mono text-xs text-gray-600 mt-6">
          {mode === 'login' ? 'No account? ' : 'Already a guardian? '}
          <button
            onClick={() => { setMode(mode === 'login' ? 'register' : 'login'); setError(''); }}
            className="text-cyber-blue hover:underline"
          >
            {mode === 'login' ? 'Register here' : 'Login here'}
          </button>
        </p>

        {/* Mission briefing */}
        <div className="mt-8 border border-cyber-green/20 rounded p-4 bg-cyber-green/5">
          <p className="font-mono text-xs text-cyber-green/70 text-center">
            ⚡ MISSION BRIEFING: Complete 3 training rooms to earn your CyberGuardian badge
          </p>
        </div>
      </div>
    </div>
  );
}
