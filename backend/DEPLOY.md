# CyberGuardian — Railway Deployment Guide

## How to Deploy on Railway

### Step 1: Create a GitHub Repository
1. Go to https://github.com and create a **new repository** (e.g. `cyberguardian`)
2. Upload all files from this zip (drag & drop or use GitHub Desktop)

### Step 2: Deploy on Railway
1. Go to https://railway.app and sign in (use GitHub login)
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select your `cyberguardian` repository
4. Railway will auto-detect the `Dockerfile` and start building

### Step 3: Set Environment Variables
In Railway → your project → **Variables**, add:

| Variable | Value |
|---|---|
| `SECRET_KEY` | Any long random string (e.g. `openssl rand -hex 32`) |

> ⚠️ You MUST set `SECRET_KEY` — without it, user logins won't work securely.

### Step 4: Get Your URL
1. In Railway → your project → **Settings** → **Domains**
2. Click **"Generate Domain"**
3. Your game will be live at something like: `cyberguardian-production.up.railway.app`

---

## Project Structure
```
cyberguardian/
├── Dockerfile          ← Railway builds this
├── railway.json        ← Railway config
├── backend/
│   ├── app.py          ← Flask API + serves React frontend
│   ├── quests.py       ← Question bank
│   └── requirements.txt
└── frontend/
    ├── src/            ← React + TypeScript source
    └── package.json
```

## How It Works
- Docker builds the React frontend first (`npm run build`)
- The built files are copied into Flask's static folder
- Flask serves both the game UI **and** the `/api/*` endpoints from one URL
- SQLite database is created automatically on first boot

## Notes
- The database resets when Railway redeploys (SQLite is in-container)
- For persistent data across deploys, add a Railway PostgreSQL plugin
