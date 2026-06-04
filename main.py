from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

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


@app.get("/test2")
def test2():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = "https://www.mercadolibre.com.uy"

    r = requests.get(url, headers=headers)

    return {
        "status_code": r.status_code,
        "largo_html": len(r.text)
    }
