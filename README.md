# CyberGuardian Q'S v1.2 — Web-Based Gamified Cybersecurity Education Game

## What's New in v1.2
- ✅ Shannon entropy calculation for realistic password scoring
- ✅ Pattern detection (keyboard walks, sequential, repeated chars)
- ✅ Crack time in human units: seconds → minutes → centuries → millions of years
- ✅ Category-balanced quiz selection across all 13 cybersecurity categories
- ✅ DB indexes on `users(username)` and `progress(user_id)` for performance
- ✅ Token refresh endpoint (`POST /api/auth/refresh`) — no forced mid-game logouts
- ✅ Badge award system fully implemented (7 badge types)
- ✅ Room 3 severity-based scoring: false negatives penalized heavier than false positives
- ✅ User-friendly error messages throughout
- ✅ Min password 8 chars + alphanumeric username validation on register

## Setup Instructions

### Backend (Flask)
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Backend runs on port 8080 (or `PORT` env var on Replit).

### Frontend (React + TypeScript)
```bash
cd frontend
npm install --legacy-peer-deps
npm start
```

### Replit Secrets
Set these in Replit Secrets tab:
- `SECRET_KEY` — any random string (e.g. `openssl rand -hex 32`)
- `REACT_APP_API_URL` — your backend Replit URL + `/api`

## Game Structure
| Room | Name | What You Learn |
|------|------|---------------|
| 01 | Knowledge Test Chamber | 20 MCQ across 13 cybersecurity categories |
| 02 | Password Security Lab | Entropy, patterns, crack time simulation |
| 03 | Access Control Arena | GRANT/DENY real-world scenarios with severity scoring |
| SOS | Security Override Sequence | Final boss challenge — all skills combined |
