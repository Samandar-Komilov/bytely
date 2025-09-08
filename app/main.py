from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.url import router as url_router

app = FastAPI(title="Bytely - URL Shortener", version="0.1.0")
Instrumentator().instrument(app).expose(app)  # exposes /metrics

app.include_router(url_router)


@app.get("/")
async def hello():
    return {"message": "Hello World"}
