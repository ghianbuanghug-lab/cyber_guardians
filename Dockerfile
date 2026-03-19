# ── Stage 1: Build React Frontend ─────────────────────────────────────────────
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend

# Install dependencies first (layer cache)
COPY frontend/package*.json ./
RUN npm install --legacy-peer-deps

# Copy source and build
COPY frontend/ ./

# Tell the React app to use /api as the backend (same origin)
ENV REACT_APP_API_URL=/api
RUN npm run build

# ── Stage 2: Flask Backend ─────────────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask app source
COPY backend/ ./

# Copy the built React app into Flask's static folder
COPY --from=frontend-builder /app/frontend/build ./static_frontend

# Railway sets PORT dynamically
ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]
