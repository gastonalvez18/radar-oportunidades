from fastapi import FastAPI
from playwright.sync_api import sync_playwright

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


@app.get("/playwright")
def playwright_test():

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            page = browser.new_page()

            page.goto("https://www.google.com")

            titulo = page.title()

            browser.close()

            return {
                "ok": True,
                "titulo": titulo
            }

    except Exception as e:

        return {
            "ok": False,
            "error": str(e)
        }
