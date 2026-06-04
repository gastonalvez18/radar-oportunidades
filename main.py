from fastapi import FastAPI
import requests

app = FastAPI(title="Radar de Oportunidades")


@app.get("/")
def home():
    return {
        "status": "online",
        "project": "Radar de Oportunidades"
    }


@app.get("/iphone")
def buscar_iphone():

    url = "https://api.mercadolibre.com/sites/MLU/search?q=iphone"

    r = requests.get(url)

    return {
        "status_code": r.status_code,
        "respuesta": r.json()
    }
@app.get("/test")
def test():
    return {
        "ok": True
    }
