import logging

from fastapi import FastAPI

from app.api.url import router as url_router

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


app = FastAPI(title="Bytely - URL Shortener", version="0.1.0")

app.include_router(url_router)


@app.get("/")
async def hello():
    return {"message": "Hello World"}
