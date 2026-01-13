from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import joblib
import numpy as np

artifact = joblib.load("brake_model.joblib")
model = artifact["model"]

app = FastAPI(title="Hard Brake Detector")

# Serve the /static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

class WindowFeatures(BaseModel):
    ax_min: float
    ax_mean: float
    ax_std: float
    gyro_var_sum: float
    speed_mean: float
    frac_below_neg3: float = Field(..., validation_alias="frac_below_-3")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(x: WindowFeatures):
    X = np.array([[x.ax_min, x.ax_mean, x.ax_std, x.gyro_var_sum, x.speed_mean, x.frac_below_neg3]], dtype=float)
    prob = float(model.predict_proba(X)[0, 1])
    pred = int(prob >= 0.5)
    return {"hard_brake": pred, "confidence": prob}

