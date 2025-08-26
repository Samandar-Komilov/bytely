from fastapi import FastAPI


app = FastAPI(
    title="Bytely - URL Shortener", 
    version="0.1.0"
)


@app.get("/")
async def hello():
    return {"message": "Hello World"}