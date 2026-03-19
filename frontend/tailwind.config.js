/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        cyber: {
          dark:    '#0a0e1a',
          darker:  '#060910',
          panel:   '#111827',
          border:  '#1e293b',
          blue:    '#00d4ff',
          green:   '#00ff88',
          red:     '#ff3366',
          yellow:  '#ffd700',
          purple:  '#8b5cf6',
          orange:  '#ff6b35',
        }
      },
      fontFamily: {
        mono:    ['"Share Tech Mono"', 'monospace'],
        display: ['"Orbitron"', 'sans-serif'],
        body:    ['"Exo 2"', 'sans-serif'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'scan': 'scan 2s linear infinite',
        'glitch': 'glitch 0.5s infinite',
        'float': 'float 3s ease-in-out infinite',
        'blink': 'blink 1s step-end infinite',
      },
      keyframes: {
        scan: {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100vh)' }
        },
        glitch: {
          '0%, 100%': { textShadow: '2px 0 #00d4ff, -2px 0 #ff3366' },
          '33%': { textShadow: '-2px 0 #00d4ff, 2px 0 #ff3366' },
          '66%': { textShadow: '2px 2px #00d4ff, -2px -2px #ff3366' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        blink: {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0' },
        }
      },
      boxShadow: {
        'cyber': '0 0 20px rgba(0, 212, 255, 0.3)',
        'cyber-green': '0 0 20px rgba(0, 255, 136, 0.3)',
        'cyber-red': '0 0 20px rgba(255, 51, 102, 0.3)',
        'cyber-purple': '0 0 20px rgba(139, 92, 246, 0.3)',
      }
    }
  },
  plugins: []
}
