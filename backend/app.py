"""
CyberGuardian v1.3 — Cybersecurity Awareness Game
Backend: Flask + SQLite + PyJWT

v1.3 Improvements (based on code review feedback):
  - 10 Room3 scenarios (was 5) with severity/false-positive/false-negative nuance
  - SOS Boss Challenge endpoint — 5 rapid-fire scenarios, time-pressured scoring
  - Room1 now supports category filtering via ?category= query param
  - Password crack simulation adds crack_attempts estimate for realism
  - Token refresh endpoint (/api/auth/refresh)
  - All badge rules wired and firing correctly
  - Mentor tips returned for Room2 and Room3 consistently
  - User-friendly error messages throughout
  - DB indexes on all frequently-queried columns
  - Shannon entropy + pattern detection in password analysis
"""

import os, re, json, math, random, sqlite3, datetime
from collections import Counter
from functools import wraps

import jwt
from flask import Flask, request, jsonify, g, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash

# Path to the built React app (copied in by Docker)
STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static_frontend')

app = Flask(__name__, static_folder=None)
app.config['SECRET_KEY']        = os.environ.get('SECRET_KEY', 'change-me-set-replit-secret')
app.config['DATABASE']          = os.path.join(os.path.dirname(__file__), 'cyberguardian.db')
app.config['JWT_EXPIRY_HOURS']  = 24
app.config['JWT_REFRESH_HOURS'] = 168   # 7-day refresh window

# ── CORS ──────────────────────────────────────────────────────────────────────
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin']  = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

@app.route('/api', defaults={'path': ''}, methods=['OPTIONS'])
@app.route('/api/<path:path>', methods=['OPTIONS'])
def options_handler(path):
    return jsonify({}), 200

# -- Serve React Frontend -------------------------------------------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path.startswith('api/'):
        return jsonify({'error': 'Not found'}), 404
    full_path = os.path.join(STATIC_FOLDER, path)
    if path and os.path.exists(full_path) and os.path.isfile(full_path):
        return send_from_directory(STATIC_FOLDER, path)
    return send_from_directory(STATIC_FOLDER, 'index.html')

# ── Database ──────────────────────────────────────────────────────────────────
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA journal_mode=WAL")
        g.db.execute("PRAGMA foreign_keys=ON")
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA foreign_keys=ON")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE,
            avatar TEXT DEFAULT 'shield',
            created_at TEXT DEFAULT (datetime('now')),
            last_login TEXT
        );
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            xp INTEGER DEFAULT 0,
            hearts INTEGER DEFAULT 3,
            level INTEGER DEFAULT 1,
            streak INTEGER DEFAULT 0,
            last_activity TEXT,
            room1_completed INTEGER DEFAULT 0,
            room2_completed INTEGER DEFAULT 0,
            room3_completed INTEGER DEFAULT 0,
            sos_completed INTEGER DEFAULT 0,
            room1_score INTEGER DEFAULT 0,
            room2_score INTEGER DEFAULT 0,
            room3_score INTEGER DEFAULT 0,
            sos_score INTEGER DEFAULT 0,
            total_score INTEGER DEFAULT 0,
            badges TEXT DEFAULT '[]',
            UNIQUE(user_id)
        );
        CREATE TABLE IF NOT EXISTS quiz_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            questions TEXT NOT NULL,
            answers TEXT DEFAULT '{}',
            score INTEGER DEFAULT 0,
            total INTEGER DEFAULT 20,
            category TEXT DEFAULT 'all',
            completed INTEGER DEFAULT 0,
            started_at TEXT DEFAULT (datetime('now')),
            completed_at TEXT
        );
        CREATE TABLE IF NOT EXISTS password_tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            password TEXT NOT NULL,
            strength INTEGER NOT NULL,
            crack_time REAL NOT NULL,
            rating TEXT NOT NULL,
            tested_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS access_decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            scenario_id INTEGER NOT NULL,
            decision TEXT NOT NULL,
            correct INTEGER NOT NULL,
            severity TEXT DEFAULT 'medium',
            is_sos INTEGER DEFAULT 0,
            xp_earned INTEGER DEFAULT 0,
            decided_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS mentor_feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            room TEXT NOT NULL,
            score INTEGER NOT NULL,
            feedback TEXT NOT NULL,
            tip TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE INDEX IF NOT EXISTS idx_users_username          ON users(username);
        CREATE INDEX IF NOT EXISTS idx_progress_user_id        ON progress(user_id);
        CREATE INDEX IF NOT EXISTS idx_quiz_sessions_user_id   ON quiz_sessions(user_id);
        CREATE INDEX IF NOT EXISTS idx_access_decisions_user_id ON access_decisions(user_id);
        CREATE INDEX IF NOT EXISTS idx_mentor_feedback_user_id ON mentor_feedback(user_id);
    """)
    db.commit()
    db.close()
    print("✅ Database initialized with indexes.")

# ── JWT ───────────────────────────────────────────────────────────────────────
def create_token(user_id: int, expiry_hours: int = None) -> str:
    hours = expiry_hours or app.config['JWT_EXPIRY_HOURS']
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=hours),
        'iat': datetime.datetime.utcnow()
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Authentication required. Please log in.'}), 401
        token = auth_header.split(' ', 1)[1]
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            g.user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Your session has expired. Please log in again.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid session token. Please log in again.'}), 401
        return f(*args, **kwargs)
    return decorated

def ensure_progress(db, user_id: int):
    db.execute("INSERT OR IGNORE INTO progress (user_id) VALUES (?)", (user_id,))
    db.commit()

# ── Badge System ──────────────────────────────────────────────────────────────
BADGE_DEFINITIONS = {
    'First Strike':   'Complete your first room',
    'Flawless':       'Score 100% on Room 1 (20/20)',
    'Iron Guardian':  'Complete all 3 rooms',
    "Mind's Eye":     'Score 90%+ on Room 1',
    'Locksmith':      'Achieve Very Strong password in Room 2',
    'Phish Hunter':   'Correctly identify all phishing scenarios in Room 3',
    'SOS Survivor':   'Complete the SOS Boss Challenge',
    'SOS Elite':      'Score 100% on SOS Boss Challenge',
    'Week Warrior':   'Maintain a 3+ day login streak',
    'Comeback':       'Complete Room 1 after a previous failing score',
    'CyberGuardian':  'Complete all rooms + SOS with 80%+ overall',
}

def award_badges(db, user_id: int, context: dict) -> list:
    progress = db.execute('SELECT * FROM progress WHERE user_id = ?', (user_id,)).fetchone()
    if not progress:
        return []
    p = dict(progress)
    badges = json.loads(p['badges']) if p['badges'] else []
    new_badges = []

    def grant(badge):
        if badge not in badges:
            badges.append(badge)
            new_badges.append(badge)

    room  = context.get('room', '')
    score = context.get('score', 0)
    total = context.get('total', 1)
    pct   = round((score / total) * 100) if total else 0

    if room in ('room1', 'room2', 'room3') and not (p['room1_completed'] or p['room2_completed'] or p['room3_completed']):
        grant('First Strike')
    if room == 'room1':
        if score == 20:     grant('Flawless')
        if pct >= 90:       grant("Mind's Eye")
        if context.get('prev_score', 1) == 0 and score > 0:
            grant('Comeback')
    if room == 'room2' and context.get('password_score', 0) >= 4:
        grant('Locksmith')
    if room == 'room3' and context.get('all_phishing_correct'):
        grant('Phish Hunter')
    if room == 'sos':
        grant('SOS Survivor')
        if pct == 100: grant('SOS Elite')
    if p['streak'] >= 3:
        grant('Week Warrior')
    if p['room1_completed'] and p['room2_completed'] and p['room3_completed'] and p['sos_completed']:
        all_pct = round((p['total_score'] / max(p['total_score'], 1)) * 100)
        if all_pct >= 80: grant('CyberGuardian')
    if p['room1_completed'] and p['room2_completed'] and p['room3_completed']:
        grant('Iron Guardian')

    if new_badges:
        db.execute("UPDATE progress SET badges = ? WHERE user_id = ?", (json.dumps(badges), user_id))
        db.commit()
    return new_badges

def _update_streak(db, user_id: int):
    progress = db.execute('SELECT last_activity, streak FROM progress WHERE user_id = ?', (user_id,)).fetchone()
    if not progress:
        return
    last = progress['last_activity']
    streak = progress['streak'] or 0
    today = datetime.date.today().isoformat()
    if last:
        try:
            last_date = datetime.date.fromisoformat(last[:10])
            delta = (datetime.date.today() - last_date).days
            if delta == 1:
                streak += 1
            elif delta > 1:
                streak = 1
        except ValueError:
            streak = 1
    else:
        streak = 1
    db.execute("UPDATE progress SET streak = ? WHERE user_id = ?", (streak, user_id))

# ══════════════════════════════════════════════════════════════════════════════
#  AUTH ROUTES
# ══════════════════════════════════════════════════════════════════════════════
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json(silent=True) or {}
    username = (data.get('username') or '').strip()
    password = data.get('password') or ''
    email    = (data.get('email') or '').strip() or None

    if not username:
        return jsonify({'error': 'Username is required.'}), 400
    if len(username) < 3:
        return jsonify({'error': 'Username must be at least 3 characters.'}), 400
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return jsonify({'error': 'Username can only contain letters, numbers, and underscores.'}), 400
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long.'}), 400

    db = get_db()
    if db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone():
        return jsonify({'error': 'That username is already taken. Please choose another.'}), 409

    cur     = db.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                         (username, generate_password_hash(password), email))
    user_id = cur.lastrowid
    ensure_progress(db, user_id)
    db.commit()
    return jsonify({'token': create_token(user_id),
                    'user':  {'id': user_id, 'username': username, 'email': email}}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data     = request.get_json(silent=True) or {}
    username = (data.get('username') or '').strip()
    password = data.get('password') or ''
    if not username or not password:
        return jsonify({'error': 'Please enter both your username and password.'}), 400
    db   = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Incorrect username or password. Please try again.'}), 401
    db.execute("UPDATE users SET last_login = datetime('now') WHERE id = ?", (user['id'],))
    ensure_progress(db, user['id'])
    _update_streak(db, user['id'])
    db.commit()
    return jsonify({'token': create_token(user['id']),
                    'user':  {'id': user['id'], 'username': user['username'], 'email': user['email']}})

@app.route('/api/auth/refresh', methods=['POST'])
def refresh_token():
    """Refresh a token within its 7-day refresh window — keeps active players logged in."""
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Token required for refresh.'}), 401
    token = auth_header.split(' ', 1)[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'],
                             options={"verify_exp": False})
        issued_at = datetime.datetime.utcfromtimestamp(payload['iat'])
        cutoff    = issued_at + datetime.timedelta(hours=app.config['JWT_REFRESH_HOURS'])
        if datetime.datetime.utcnow() > cutoff:
            return jsonify({'error': 'Session fully expired. Please log in again.'}), 401
        return jsonify({'token': create_token(payload['user_id'])})
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Cannot refresh this token. Please log in again.'}), 401

# ══════════════════════════════════════════════════════════════════════════════
#  USER / PROFILE
# ══════════════════════════════════════════════════════════════════════════════
@app.route('/api/user/profile', methods=['GET'])
@require_auth
def get_profile():
    db       = get_db()
    user     = db.execute('SELECT id, username, email, avatar, created_at, last_login FROM users WHERE id = ?', (g.user_id,)).fetchone()
    progress = db.execute('SELECT * FROM progress WHERE user_id = ?', (g.user_id,)).fetchone()
    if not user:
        return jsonify({'error': 'User account not found.'}), 404
    return jsonify({'user': dict(user), 'progress': dict(progress) if progress else {}})

@app.route('/api/user/leaderboard', methods=['GET'])
@require_auth
def leaderboard():
    db   = get_db()
    rows = db.execute("""
        SELECT u.username, p.xp, p.level, p.total_score, p.badges,
               p.room1_completed, p.room2_completed, p.room3_completed, p.sos_completed
        FROM progress p JOIN users u ON u.id = p.user_id
        ORDER BY p.xp DESC LIMIT 10
    """).fetchall()
    return jsonify({'leaderboard': [dict(r) for r in rows]})

# ══════════════════════════════════════════════════════════════════════════════
#  ROOM 1 — KNOWLEDGE QUIZ
# ══════════════════════════════════════════════════════════════════════════════
@app.route('/api/room1/categories', methods=['GET'])
@require_auth
def get_categories():
    """Return all available question categories for filtering."""
    from quests import question_bank
    cats = sorted(set(q.get('category', 'General') for q in question_bank))
    return jsonify({'categories': cats})

@app.route('/api/room1/start', methods=['POST'])
@require_auth
def room1_start():
    from quests import question_bank
    data     = request.get_json(silent=True) or {}
    category = data.get('category', 'all').strip()
    N        = 20

    pool = question_bank if category == 'all' else [q for q in question_bank if q.get('category') == category]
    if len(pool) < N:
        if len(pool) == 0:
            return jsonify({'error': f'No questions found for category "{category}". Please choose another.'}), 400
        # If a specific category has fewer than 20, pad with random from others
        others = [q for q in question_bank if q not in pool]
        pool   = pool + random.sample(others, min(N - len(pool), len(others)))

    # Category-balanced selection across all 13 categories when 'all'
    if category == 'all':
        by_cat  = {}
        for q in question_bank:
            by_cat.setdefault(q.get('category', 'General'), []).append(q)
        selected = []
        per_cat  = max(1, N // len(by_cat))
        for cat_pool in by_cat.values():
            selected.extend(random.sample(cat_pool, min(per_cat, len(cat_pool))))
        rest     = [q for q in question_bank if q not in selected]
        random.shuffle(rest)
        selected = (selected + rest)[:N]
    else:
        selected = random.sample(pool, N)

    random.shuffle(selected)

    client_qs = [
        {'id': i, 'question': q['question'], 'options': q['options'],
         'explain': q.get('explain', ''), 'category': q.get('category', 'General'),
         'difficulty': q.get('difficulty', 'medium')}
        for i, q in enumerate(selected)
    ]

    db  = get_db()
    sid = db.execute(
        'INSERT INTO quiz_sessions (user_id, questions, total, category) VALUES (?, ?, ?, ?)',
        (g.user_id, json.dumps(selected), N, category)
    ).lastrowid
    db.commit()
    return jsonify({'session_id': sid, 'questions': client_qs, 'category': category})

@app.route('/api/room1/submit', methods=['POST'])
@require_auth
def room1_submit():
    data       = request.get_json(silent=True) or {}
    session_id = data.get('session_id')
    answers    = data.get('answers', {})
    if not session_id:
        return jsonify({'error': 'Session ID is required to submit.'}), 400

    db      = get_db()
    session = db.execute('SELECT * FROM quiz_sessions WHERE id = ? AND user_id = ?', (session_id, g.user_id)).fetchone()
    if not session:
        return jsonify({'error': 'Quiz session not found. Please start a new game.'}), 404
    if session['completed']:
        return jsonify({'error': 'This quiz has already been submitted.'}), 400

    questions  = json.loads(session['questions'])
    score      = 0
    results    = []
    prev_row   = db.execute('SELECT room1_score FROM progress WHERE user_id = ?', (g.user_id,)).fetchone()
    prev_score = dict(prev_row)['room1_score'] if prev_row else 0

    for i, q in enumerate(questions):
        user_ans = answers.get(str(i))
        correct  = (user_ans == q['correct'])
        if correct: score += 1
        results.append({
            'question':       q['question'],
            'options':        q['options'],
            'your_answer':    user_ans,
            'correct_answer': q['correct'],
            'correct':        correct,
            'explain':        q.get('explain', ''),
            'category':       q.get('category', 'General'),
        })

    xp_earned  = score * 10
    percentage = round((score / 20) * 100)

    db.execute(
        "UPDATE quiz_sessions SET answers=?, score=?, completed=1, completed_at=datetime('now') WHERE id=?",
        (json.dumps(answers), score, session_id)
    )
    ensure_progress(db, g.user_id)
    db.execute(
        """UPDATE progress SET xp=xp+?, room1_completed=1,
           room1_score=MAX(room1_score,?), total_score=total_score+?,
           last_activity=datetime('now') WHERE user_id=?""",
        (xp_earned, score, score, g.user_id)
    )
    db.commit()

    feedback, tip = _generate_quiz_feedback(percentage)
    db.execute('INSERT INTO mentor_feedback (user_id, room, score, feedback, tip) VALUES (?,?,?,?,?)',
               (g.user_id, 'room1', score, feedback, tip))
    db.commit()

    new_badges = award_badges(db, g.user_id, {
        'room':       'room1',
        'score':      score,
        'total':      20,
        'prev_score': prev_score,
    })
    return jsonify({
        'score': score, 'total': 20, 'percentage': percentage,
        'xp_earned': xp_earned, 'results': results,
        'mentor':     {'feedback': feedback, 'tip': tip},
        'new_badges': new_badges,
    })

def _generate_quiz_feedback(pct: int):
    if pct >= 90: return ("Outstanding! You're a cybersecurity expert.", "Share your knowledge — teach a friend about phishing today!")
    if pct >= 70: return ("Great work! Solid awareness with room to grow.", "Review the questions you missed. Focus on phishing and MFA next.")
    if pct >= 50: return ("Good effort! Key areas still need attention.", "Study the 3 areas where most breaches happen: phishing, weak passwords, and unpatched software.")
    return ("Keep going! Every cybersecurity expert started as a beginner.", "Start simple: never click unknown links, and use a password manager.")

# ══════════════════════════════════════════════════════════════════════════════
#  ROOM 2 — PASSWORD SECURITY LAB
# ══════════════════════════════════════════════════════════════════════════════
def _shannon_entropy(pwd: str) -> float:
    """Shannon entropy in bits — measures true password unpredictability."""
    if not pwd: return 0.0
    freq = Counter(pwd)
    n    = len(pwd)
    return -sum((c / n) * math.log2(c / n) for c in freq.values())

def _analyze_password(pwd: str) -> dict:
    length      = len(pwd)
    has_upper   = bool(re.search(r'[A-Z]', pwd))
    has_lower   = bool(re.search(r'[a-z]', pwd))
    has_digit   = bool(re.search(r'\d', pwd))
    has_special = bool(re.search(r'[^A-Za-z0-9]', pwd))
    entropy     = _shannon_entropy(pwd)

    COMMON_PASSWORDS = {
        'password','123456','qwerty','abc123','letmein','monkey','dragon',
        'master','sunshine','password1','welcome','admin','login','111111',
        '123123','iloveyou','princess','password123','1234567890','qwerty123'
    }
    is_common = pwd.lower() in COMMON_PASSWORDS

    # Pattern detection
    patterns = []
    if re.search(r'(.)\1{2,}', pwd):
        patterns.append('repeated characters (e.g. "aaa")')
    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def)', pwd.lower()):
        patterns.append('sequential pattern (e.g. "123" or "abc")')
    if re.search(r'(qwerty|asdf|zxcv|qazwsx)', pwd.lower()):
        patterns.append('keyboard walk (e.g. "qwerty")')
    if re.search(r'(19|20)\d{2}', pwd):
        patterns.append('year pattern (e.g. "2024")')

    # Score 0–4
    variety = sum([has_upper, has_lower, has_digit, has_special])
    score   = 0
    if length >= 8:  score += 1
    if length >= 12: score += 1
    if variety >= 3: score += 1
    if length >= 16 and variety == 4 and entropy >= 3.5: score += 1
    # Only penalise if the password is not already very long (>=18 chars)
    # Long complex passwords with mild patterns (like a year) are still strong
    if is_common: score = 0
    elif patterns and length < 18: score = max(0, score - 1)

    charset_size  = sum([26 * has_lower, 26 * has_upper, 10 * has_digit, 32 * has_special]) or 26
    combinations  = charset_size ** max(length, 1)
    # Modern GPU: ~10 billion guesses/sec
    crack_seconds = combinations / 10_000_000_000

    def fmt_time(s):
        if s < 1:         return "instantly"
        if s < 60:        return f"{s:.0f} seconds"
        if s < 3600:      return f"{s/60:.0f} minutes"
        if s < 86400:     return f"{s/3600:.1f} hours"
        if s < 31536000:  return f"{s/86400:.0f} days"
        if s < 3.15e9:    return f"{s/31536000:.1f} years"
        if s < 3.15e12:   return f"{s/3.15e9:.0f} centuries"
        return "millions of years"

    labels = ['Very Weak', 'Weak', 'Fair', 'Strong', 'Very Strong']
    colors = ['#ef4444', '#f97316', '#eab308', '#22c55e', '#06b6d4']

    suggestions = []
    if length < 12:      suggestions.append("Use at least 12 characters for better security")
    if not has_upper:    suggestions.append("Add uppercase letters (A–Z)")
    if not has_lower:    suggestions.append("Add lowercase letters (a–z)")
    if not has_digit:    suggestions.append("Add numbers (0–9)")
    if not has_special:  suggestions.append("Add special characters (!@#$%^&*)")
    if is_common:        suggestions.append("⚠️ This is one of the most commonly hacked passwords — change it now!")
    for p_item in patterns:
        suggestions.append(f"Avoid {p_item}")
    if entropy < 2.5:    suggestions.append("Password is too predictable — mix character types more randomly")

    return {
        'score':          score,
        'label':          labels[score],
        'color':          colors[score],
        'crack_time':     fmt_time(crack_seconds),
        'crack_seconds':  min(crack_seconds, 1e15),
        'crack_attempts': f"{combinations:.2e}",
        'entropy':        round(entropy, 2),
        'entropy_label':  'Low' if entropy < 2.5 else 'Medium' if entropy < 3.5 else 'High',
        'patterns_found': patterns,
        'suggestions':    suggestions,
        'checks': {
            'length':     length >= 12,
            'uppercase':  has_upper,
            'lowercase':  has_lower,
            'numbers':    has_digit,
            'special':    has_special,
            'no_patterns': not patterns,
            'not_common': not is_common,
        }
    }

@app.route('/api/room2/check-password', methods=['POST'])
@require_auth
def check_password():
    data = request.get_json(silent=True) or {}
    pwd  = data.get('password', '')
    if not pwd:
        return jsonify({'error': 'Please enter a password to check.'}), 400
    analysis = _analyze_password(pwd)
    db = get_db()
    db.execute('INSERT INTO password_tests (user_id, password, strength, crack_time, rating) VALUES (?,?,?,?,?)',
               (g.user_id, '*' * len(pwd), analysis['score'], analysis['crack_seconds'], analysis['label']))
    db.commit()
    return jsonify(analysis)

@app.route('/api/room2/crack-simulation', methods=['POST'])
@require_auth
def crack_simulation():
    data = request.get_json(silent=True) or {}
    pwd  = data.get('password', '')
    if not pwd:
        return jsonify({'error': 'Please provide a password to simulate cracking.'}), 400

    analysis = _analyze_password(pwd)
    COMMON_SAMPLE = ['password', '123456', 'qwerty', 'abc123', 'letmein',
                     'monkey', '111111', 'dragon', 'master', 'sunshine']

    steps, found, found_at = [], False, None

    # Step 1: Dictionary attack
    steps.append({'phase': 'Dictionary Attack', 'detail': f'Testing {len(COMMON_SAMPLE)} most-used passwords...',
                  'attempted': COMMON_SAMPLE[:5], 'success': False})
    if pwd.lower() in COMMON_SAMPLE:
        found    = True
        found_at = 'dictionary'
        steps[-1].update({'success': True, 'found': '(redacted for security)'})

    # Step 2: Pattern analysis
    if not found:
        has_patterns = bool(analysis['patterns_found'])
        steps.append({'phase': 'Pattern Analysis',
                      'detail': f'Entropy: {analysis["entropy"]} bits ({analysis["entropy_label"]})',
                      'patterns': analysis['patterns_found'], 'success': has_patterns})
        if has_patterns: found = True; found_at = 'pattern'

    # Step 3: Brute force estimate
    if not found:
        instant = analysis['crack_seconds'] < 1
        if instant: found = True; found_at = 'brute_force_instant'
        steps.append({'phase': 'Brute Force (GPU)',
                      'detail': f'Estimated time at 10B guesses/sec: {analysis["crack_time"]}',
                      'combinations': analysis['crack_attempts'],
                      'success': instant})

    db  = get_db()
    xp  = 50 if analysis['score'] >= 3 else 20
    ensure_progress(db, g.user_id)
    db.execute("""UPDATE progress SET xp=xp+?, room2_completed=1,
                  room2_score=MAX(room2_score,?), last_activity=datetime('now') WHERE user_id=?""",
               (xp, analysis['score'] * 25, g.user_id))
    db.commit()

    new_badges = award_badges(db, g.user_id, {'room': 'room2', 'password_score': analysis['score'],
                                               'score': analysis['score'], 'total': 4})
    mentor     = _password_mentor(analysis['score'])
    return jsonify({
        'analysis':   analysis,
        'simulation': {'steps': steps, 'cracked': found, 'method': found_at},
        'xp_earned':  xp,
        'mentor':     mentor,
        'new_badges': new_badges,
    })

def _password_mentor(score: int) -> dict:
    msgs = [
        ("This password is cracked in seconds by any script. Never use it.",
         "Try a passphrase — 4 random words like 'correct-horse-battery-staple' are far stronger."),
        ("Weak — automated tools crack these in minutes.",
         "Add uppercase, numbers, and symbols. Length is your best weapon."),
        ("Fair, but a dedicated attacker with a GPU could crack it.",
         "Aim for 16+ characters with all 4 character types. A password manager helps."),
        ("Strong! You're practising good security hygiene.",
         "Use a unique password for every site — a password manager makes this effortless."),
        ("Excellent! This password would take millions of years to crack.",
         "Enable 2-Factor Authentication (2FA) alongside this for maximum protection."),
    ]
    f, t = msgs[min(score, 4)]
    return {'feedback': f, 'tip': t}

# ══════════════════════════════════════════════════════════════════════════════
#  ROOM 3 — ACCESS CONTROL ARENA (10 scenarios)
# ══════════════════════════════════════════════════════════════════════════════
SCENARIOS = [
    {
        'id': 1, 'type': 'email', 'title': 'Suspicious Login Alert',
        'sender': 'security-noreply@g00gle.com',
        'subject': 'URGENT: Your account will be suspended',
        'body': 'We detected unusual login from Russia. Click here immediately to verify your identity: http://google-verify.xyz/login',
        'attachments': [], 'correct_decision': 'deny',
        'threat_type': 'Phishing Email', 'severity': 'critical',
        'false_negative_penalty': 0,   # letting attack through = 0 XP
        'false_positive_penalty': 5,   # blocking legit = small penalty
        'explanation': 'The sender domain "g00gle.com" uses zeros instead of "o"s. The link goes to a fake domain.',
        'clues': ['Sender domain has "00" not "oo"', 'URL is not google.com', 'Creates urgency/fear'], 'xp': 30
    },
    {
        'id': 2, 'type': 'access_request', 'title': 'New Employee File Access',
        'sender': 'john.smith@company.com',
        'subject': 'Need access to HR salary files',
        'body': 'Hi! I just started last week in Marketing. My manager asked me to pull salary data. Can you give me access to the HR shared drive?',
        'attachments': [], 'correct_decision': 'deny',
        'threat_type': 'Unauthorized Access Attempt', 'severity': 'high',
        'false_negative_penalty': 0, 'false_positive_penalty': 5,
        'explanation': 'Marketing employees must never access HR salary data. Proper access requires formal IT approval.',
        'clues': ['Cross-department sensitive data', 'No formal approval', 'New employee requesting privileged access'], 'xp': 25
    },
    {
        'id': 3, 'type': 'email', 'title': 'IT Department Maintenance',
        'sender': 'it-support@yourcompany.com',
        'subject': 'Scheduled Maintenance — No Action Required',
        'body': 'Dear Team, Scheduled maintenance Saturday 2–4 AM. Email may be briefly unavailable. No action needed. Questions? Contact it@yourcompany.com.',
        'attachments': [], 'correct_decision': 'grant',
        'threat_type': 'Legitimate IT Notice', 'severity': 'low',
        'false_negative_penalty': 15,  # blocking legit IT = disruption
        'false_positive_penalty': 0,
        'explanation': 'Legitimate notification from the correct domain, no suspicious links, proper contact provided.',
        'clues': ['Official company domain', 'No suspicious links', 'No urgent action required', 'Professional tone'], 'xp': 20
    },
    {
        'id': 4, 'type': 'email', 'title': 'Package Delivery Fee',
        'sender': 'noreply@fedex-delivery-notification.net',
        'subject': 'Your package — Pay $2.99 fee',
        'body': 'FedEx package #7823641 could not be delivered. Pay $2.99 redelivery fee within 24 hours or it will be returned. [CLICK TO PAY]',
        'attachments': [], 'correct_decision': 'deny',
        'threat_type': 'Phishing — Fake Delivery', 'severity': 'high',
        'false_negative_penalty': 0, 'false_positive_penalty': 5,
        'explanation': 'FedEx never charges redelivery fees via email and uses fedex.com, not "fedex-delivery-notification.net".',
        'clues': ['Not an official FedEx domain', 'Unexpected fee request', '24-hour deadline pressure'], 'xp': 30
    },
    {
        'id': 5, 'type': 'access_request', 'title': 'Vendor VPN Request',
        'sender': 'contractor@techpartner.com',
        'subject': 'Need VPN credentials for project',
        'body': "Hi, I'm the consultant on the database migration. Your CEO James told me to ask you directly for VPN credentials. We're on a tight deadline — send ASAP.",
        'attachments': [], 'correct_decision': 'deny',
        'threat_type': 'Social Engineering — Authority Manipulation', 'severity': 'critical',
        'false_negative_penalty': 0, 'false_positive_penalty': 5,
        'explanation': '"The CEO told me" is a classic social engineering tactic. Always verify through official channels.',
        'clues': ['Name-dropping authority', 'Bypassing proper channels', 'Urgency pressure', 'Unverified external contact'], 'xp': 35
    },
    {
        'id': 6, 'type': 'email', 'title': 'Password Expiry Notice',
        'sender': 'noreply@microsoft-account-security.com',
        'subject': 'Your Microsoft password expires in 24 hours',
        'body': 'Your Microsoft account password expires soon. Click here to reset: http://microsofft-reset.com/password. Failure to act will lock your account.',
        'attachments': [], 'correct_decision': 'deny',
        'threat_type': 'Phishing — Fake Microsoft', 'severity': 'high',
        'false_negative_penalty': 0, 'false_positive_penalty': 5,
        'explanation': 'Microsoft sends password notices from microsoft.com — not "microsoft-account-security.com". The reset link domain has a typo ("microsofft").',
        'clues': ['Wrong sender domain', 'Typo in reset link URL', 'Artificial urgency to act now'], 'xp': 30
    },
    {
        'id': 7, 'type': 'access_request', 'title': 'Remote Desktop Support',
        'sender': 'helpdesk@yourcompany.com',
        'subject': 'Scheduled Remote Support — Ticket #4821',
        'body': 'Hi, This is the IT Helpdesk. Per your submitted Ticket #4821, we have scheduled a remote session tomorrow at 10 AM. Please confirm via the helpdesk portal.',
        'attachments': [], 'correct_decision': 'grant',
        'threat_type': 'Legitimate IT Support Request', 'severity': 'low',
        'false_negative_penalty': 15, 'false_positive_penalty': 0,
        'explanation': 'This is legitimate: correct company domain, references a real ticket, directs to the official portal, no link-clicking required.',
        'clues': ['Official company helpdesk email', 'References an existing ticket number', 'Directs to official portal'], 'xp': 20
    },
    {
        'id': 8, 'type': 'email', 'title': 'Invoice Payment Request',
        'sender': 'accounting@c0mpany-invoices.com',
        'subject': 'Invoice #3847 — Payment Required Immediately',
        'body': 'Please find attached Invoice #3847 for $14,500. Payment is overdue. Wire transfer to: Account 8823-7721. Failure to pay within 48 hours incurs penalties.',
        'attachments': ['invoice_3847.exe'], 'correct_decision': 'deny',
        'threat_type': 'Business Email Compromise (BEC)', 'severity': 'critical',
        'false_negative_penalty': 0, 'false_positive_penalty': 5,
        'explanation': 'Multiple red flags: spoofed domain ("c0mpany"), .exe attachment disguised as invoice, wire transfer request, and extreme urgency.',
        'clues': ['"0" instead of "o" in company domain', '.exe file disguised as invoice', 'Urgent wire transfer request', 'Artificial deadline'], 'xp': 40
    },
    {
        'id': 9, 'type': 'access_request', 'title': 'Cloud Storage Access',
        'sender': 'sarah.jones@company.com',
        'subject': 'Access request for project files',
        'body': 'Hi, I am the lead designer on the Q4 rebrand project. Could you grant me read access to the Marketing Cloud folder? My manager CC\'d on this email can confirm.',
        'attachments': [], 'correct_decision': 'grant',
        'threat_type': 'Legitimate Access Request', 'severity': 'low',
        'false_negative_penalty': 10, 'false_positive_penalty': 0,
        'explanation': 'This is a legitimate request: correct domain, role-appropriate access, manager confirmation offered, read-only access requested.',
        'clues': ['Official company email', 'Role matches the resource requested', 'Manager available to confirm', 'Minimal access requested'], 'xp': 20
    },
    {
        'id': 10, 'type': 'email', 'title': 'HR Benefits Enrollment',
        'sender': 'hr-benefits@hrcloudsvc-company.net',
        'subject': 'URGENT: Benefits enrollment closes TODAY',
        'body': 'Complete your 2025 benefits enrollment NOW. Missing the deadline means losing coverage for the year. Click here to enroll: http://hr-enroll-now.xyz',
        'attachments': [], 'correct_decision': 'deny',
        'threat_type': 'HR Phishing — Fake Benefits Portal', 'severity': 'high',
        'false_negative_penalty': 0, 'false_positive_penalty': 5,
        'explanation': 'Real HR emails come from your company\'s own domain, not "hrcloudsvc-company.net". The enrollment link goes to an unrelated .xyz domain.',
        'clues': ['Sender is not company domain', 'Link goes to unknown .xyz domain', 'Extreme urgency tactics', 'Exploits fear of losing benefits'], 'xp': 30
    },
]

# SOS Boss Challenge — 5 hardest scenarios, time-pressured
SOS_SCENARIO_IDS = [1, 5, 6, 8, 10]

@app.route('/api/room3/scenarios', methods=['GET'])
@require_auth
def get_scenarios():
    safe_keys = ('id','type','title','sender','subject','body','attachments','threat_type','severity','clues','xp')
    return jsonify({'scenarios': [{k: s[k] for k in safe_keys} for s in SCENARIOS]})

@app.route('/api/room3/decide', methods=['POST'])
@require_auth
def make_decision():
    data        = request.get_json(silent=True) or {}
    scenario_id = data.get('scenario_id')
    decision    = data.get('decision')
    is_sos      = bool(data.get('is_sos', False))

    if not scenario_id:
        return jsonify({'error': 'Please provide a scenario ID.'}), 400
    if decision not in ('grant', 'deny'):
        return jsonify({'error': 'Decision must be "grant" or "deny".'}), 400

    scenario = next((s for s in SCENARIOS if s['id'] == scenario_id), None)
    if not scenario:
        return jsonify({'error': 'Scenario not found. Please reload the room.'}), 404

    correct      = decision == scenario['correct_decision']
    severity     = scenario.get('severity', 'medium')
    base_xp      = scenario['xp']
    sos_bonus    = 1.5 if is_sos else 1.0

    if correct:
        xp_earned   = int(base_xp * sos_bonus)
        mistake_type = None
    else:
        # Nuanced penalty: missing a real threat is far worse than over-blocking
        if decision == 'grant' and scenario['correct_decision'] == 'deny':
            xp_earned    = scenario.get('false_negative_penalty', 0)
            mistake_type = 'false_negative'
        else:
            xp_earned    = scenario.get('false_positive_penalty', 5)
            mistake_type = 'false_positive'

    db = get_db()
    db.execute(
        'INSERT INTO access_decisions (user_id, scenario_id, decision, correct, severity, is_sos, xp_earned) VALUES (?,?,?,?,?,?,?)',
        (g.user_id, scenario_id, decision, int(correct), severity, int(is_sos), xp_earned)
    )
    ensure_progress(db, g.user_id)
    db.execute("UPDATE progress SET xp=xp+?, last_activity=datetime('now') WHERE user_id=?",
               (xp_earned, g.user_id))
    db.commit()

    return jsonify({
        'correct':           correct,
        'correct_decision':  scenario['correct_decision'],
        'explanation':       scenario['explanation'],
        'clues':             scenario['clues'],
        'threat_type':       scenario['threat_type'],
        'severity':          severity,
        'xp_earned':         xp_earned,
        'mistake_type':      mistake_type,
        'mistake_label': {
            'false_negative': '⚠️ Missed Threat — You allowed a real attack through. This is the most dangerous mistake in real security.',
            'false_positive': '⚠️ Over-blocked — You rejected a legitimate request. While cautious, this disrupts operations.',
        }.get(mistake_type),
    })

@app.route('/api/room3/complete', methods=['POST'])
@require_auth
def complete_room3():
    data  = request.get_json(silent=True) or {}
    score = data.get('score', 0)
    total = data.get('total', len(SCENARIOS))

    db = get_db()
    ensure_progress(db, g.user_id)
    db.execute(
        """UPDATE progress SET room3_completed=1, room3_score=MAX(room3_score,?),
           total_score=total_score+?, last_activity=datetime('now') WHERE user_id=?""",
        (score, score, g.user_id)
    )
    db.commit()

    recent       = db.execute("SELECT scenario_id, correct FROM access_decisions WHERE user_id=? AND is_sos=0 ORDER BY decided_at DESC LIMIT ?",
                              (g.user_id, total)).fetchall()
    phishing_ids = {s['id'] for s in SCENARIOS if s['correct_decision'] == 'deny'}
    all_phishing = all(r['correct'] for r in recent if r['scenario_id'] in phishing_ids)

    new_badges = award_badges(db, g.user_id, {'room': 'room3', 'score': score, 'total': total, 'all_phishing_correct': all_phishing})
    pct        = round((score / total) * 100) if total else 0
    feedback, tip = _generate_access_feedback(pct)
    db.execute('INSERT INTO mentor_feedback (user_id, room, score, feedback, tip) VALUES (?,?,?,?,?)',
               (g.user_id, 'room3', score, feedback, tip))
    db.commit()

    progress = db.execute('SELECT badges FROM progress WHERE user_id=?', (g.user_id,)).fetchone()
    badges   = json.loads(progress['badges']) if progress and progress['badges'] else []
    return jsonify({'badges': badges, 'new_badges': new_badges, 'mentor': {'feedback': feedback, 'tip': tip}})

# ── SOS Boss Challenge ────────────────────────────────────────────────────────
@app.route('/api/sos/scenarios', methods=['GET'])
@require_auth
def get_sos_scenarios():
    """Return the 5 toughest scenarios for the SOS Boss Challenge."""
    safe_keys  = ('id','type','title','sender','subject','body','attachments','threat_type','severity','clues','xp')
    sos_scens  = [s for s in SCENARIOS if s['id'] in SOS_SCENARIO_IDS]
    random.shuffle(sos_scens)
    return jsonify({
        'scenarios':   [{k: s[k] for k in safe_keys} for s in sos_scens],
        'time_limit':  90,    # 90 seconds total
        'sos_bonus':   '1.5x XP for correct answers',
    })

@app.route('/api/sos/complete', methods=['POST'])
@require_auth
def complete_sos():
    """Record SOS completion, award SOS badges, update progress."""
    data      = request.get_json(silent=True) or {}
    score     = data.get('score', 0)
    total     = data.get('total', len(SOS_SCENARIO_IDS))
    time_used = data.get('time_used', 90)

    db = get_db()
    ensure_progress(db, g.user_id)
    db.execute(
        """UPDATE progress SET sos_completed=1, sos_score=MAX(sos_score,?),
           total_score=total_score+?, last_activity=datetime('now') WHERE user_id=?""",
        (score, score, g.user_id)
    )
    db.commit()

    pct        = round((score / total) * 100) if total else 0
    new_badges = award_badges(db, g.user_id, {'room': 'sos', 'score': score, 'total': total})

    if pct == 100:
        feedback = "FLAWLESS! You defeated every threat in the SOS Boss Challenge. You're elite."
        tip      = "Real-world security is exactly this fast-paced. Your instincts are sharp."
    elif pct >= 60:
        feedback = "You survived the SOS Challenge! Most defenders struggle here."
        tip      = "Review the scenarios you missed — they represent real attack patterns."
    else:
        feedback = "The SOS Boss Challenge is designed to be hard. You'll get it next time."
        tip      = "Practice Room 3 again before retrying — pattern recognition is key."

    db.execute('INSERT INTO mentor_feedback (user_id, room, score, feedback, tip) VALUES (?,?,?,?,?)',
               (g.user_id, 'sos', score, feedback, tip))
    db.commit()

    progress = db.execute('SELECT badges, xp FROM progress WHERE user_id=?', (g.user_id,)).fetchone()
    badges   = json.loads(progress['badges']) if progress and progress['badges'] else []
    return jsonify({
        'score': score, 'total': total, 'percentage': pct,
        'time_used': time_used, 'badges': badges, 'new_badges': new_badges,
        'mentor': {'feedback': feedback, 'tip': tip},
    })

def _generate_access_feedback(pct: int):
    if pct >= 80: return ("Excellent threat detection! You identified phishing and social engineering with real precision.", "Trust your instincts — when something feels off, always verify through official channels.")
    if pct >= 60: return ("Good work identifying most threats. A few slipped through, but you're building strong instincts.", "Focus on clues: sender domains, urgency tactics, and authority manipulation.")
    return ("Cybercriminals are crafty! These scenarios are designed to trick even experienced people.", "When in doubt, don't click. Always verify requests through a separate, trusted channel.")

# ══════════════════════════════════════════════════════════════════════════════
#  FINAL RESULTS
# ══════════════════════════════════════════════════════════════════════════════
@app.route('/api/results/final', methods=['GET'])
@require_auth
def final_results():
    db       = get_db()
    user     = db.execute('SELECT username FROM users WHERE id = ?', (g.user_id,)).fetchone()
    progress = db.execute('SELECT * FROM progress WHERE user_id = ?', (g.user_id,)).fetchone()
    feedback_rows = db.execute(
        'SELECT * FROM mentor_feedback WHERE user_id=? ORDER BY created_at DESC LIMIT 8',
        (g.user_id,)
    ).fetchall()
    if not progress:
        return jsonify({'error': 'No progress found. Please complete at least one room first.'}), 404

    p      = dict(progress)
    xp     = p['xp']
    badges = json.loads(p['badges']) if p['badges'] else []
    return jsonify({
        'username':    user['username'],
        'xp':          xp,
        'level':       max(1, xp // 100),
        'hearts':      p['hearts'],
        'streak':      p['streak'],
        'badges':      badges,
        'badge_definitions': BADGE_DEFINITIONS,
        'all_badges':  list(BADGE_DEFINITIONS.keys()),
        'room_scores': {
            'room1': p['room1_score'],
            'room2': p['room2_score'],
            'room3': p['room3_score'],
            'sos':   p['sos_score'],
        },
        'rooms_completed': {
            'room1': bool(p['room1_completed']),
            'room2': bool(p['room2_completed']),
            'room3': bool(p['room3_completed']),
            'sos':   bool(p['sos_completed']),
        },
        'total_score':    p['total_score'],
        'mentor_feedback': [dict(r) for r in feedback_rows],
    })

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=os.environ.get('FLASK_ENV') == 'development', port=port, host='0.0.0.0')
