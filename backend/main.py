from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ServerMetric(BaseModel):
    server_name: str
    cpu: float
    ram: float
    disk: float

metrics_store = []

@app.get("/")
def root():
    return {"message": "Monitoring SaaS Backend Running"}

@app.post("/metrics")
def receive_metrics(metric: ServerMetric):
    metrics_store.append(metric.dict())
    return {
        "status": "received",
        "data": metric
    }

@app.get("/metrics")
def get_metrics():
    return metrics_store[-20:]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = {
            "cpu": round(random.uniform(10, 90), 2),
            "ram": round(random.uniform(20, 80), 2),
            "disk": round(random.uniform(30, 70), 2),
        }

        await websocket.send_json(data)
        await asyncio.sleep(2)