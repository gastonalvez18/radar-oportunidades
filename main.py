from fastapi import FastAPI

app = FastAPI(title="Radar de Oportunidades")

@app.get("/")
def home():
    return {
        "status": "online",
        "project": "Radar de Oportunidades"
    }
