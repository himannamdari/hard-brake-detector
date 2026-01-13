# Hard Brake Detector (FastAPI + ML + Docker)

A minimal end-to-end demo:
- Synthetic telematics-style features
- Trained classifier (hard brake vs not)
- FastAPI backend + simple frontend
- Dockerized deployment

## Run locally (Python)
```bash
pip install -r requirements.txt
uvicorn app:app --reload --reload-dir .

