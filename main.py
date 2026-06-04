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

    data = r.json()

    resultados = []

    for item in data.get("results", [])[:20]:

        resultados.append({
            "titulo": item.get("title"),
            "precio": item.get("price"),
            "link": item.get("permalink")
        })

    return resultados
