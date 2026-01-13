# Hard Brake Detector (FastAPI + ML + Docker)

An end-to-end demo project that shows how to:
- package an ML inference pipeline behind an API,
- expose a simple web UI,
- and run the same app locally or in a Docker container (cloud-ready).

This is a **toy version** of a real telematics event detector (hard braking) using engineered features and a saved scikit-learn model artifact.

---

## What it does

**Input:** window-level features (derived from mobile sensors / GPS conceptually)  
**Output:**  
- `hard_brake` (0/1)
- `confidence` (probability for hard braking)

The API supports the payload key `frac_below_-3` (dash included) via Pydantic aliasing.

---

## Architecture

- **Frontend:** a minimal HTML/CSS/JS page served by FastAPI at `/`
- **Backend:** FastAPI service with `/predict` and `/health`
- **Model:** scikit-learn pipeline loaded from `brake_model.joblib`
- **Production server:** Gunicorn + Uvicorn workers (in Docker)

Endpoints:
- `GET /` → web UI
- `GET /docs` → Swagger UI
- `GET /health` → health check
- `POST /predict` → inference

---

## Run locally (Python)

```bash
pip install -r requirements.txt
uvicorn app:app --reload --reload-dir .

