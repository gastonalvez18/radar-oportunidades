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


@app.get("/iphone")
def buscar_iphone():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = "https://listado.mercadolibre.com.uy/iphone"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    titulos = []

    for h3 in soup.find_all("h3")[:20]:
        titulos.append(h3.get_text())

    return {
        "cantidad": len(titulos),
        "titulos": titulos
    }
