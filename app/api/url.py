import logging

from fastapi import APIRouter

from app.core.database import in_memory_db
from app.schemas import URLShortenIn

logger = logging.getLogger(__name__)


router = APIRouter(prefix="/urls", tags=["urls"])


@router.post("/shorten")
async def shorten(url: URLShortenIn):
    short_code = str(len(in_memory_db["links"]) + 1)
    in_memory_db["links"][short_code] = url.url
    return {"short_code": short_code}


@router.get("/{short_code}")
async def redirect_url(short_code: str):
    return in_memory_db.get("links", {}).get(short_code, {})
