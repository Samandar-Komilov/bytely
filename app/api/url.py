import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from prometheus_client import Counter, Histogram

from app.core.database import in_memory_db
from app.schemas import URLShortenIn

logger = logging.getLogger(__name__)


router = APIRouter(prefix="/urls", tags=["urls"])

redirects = Counter("redirect_total", "Redirects served")
shorten_latency = Histogram("shorten_latency_seconds", "Latency for shorten")


@router.post("/shorten")
async def shorten(url: URLShortenIn):
    with shorten_latency.time():
        # simple atomic-ish id: prefer a counter over len(dict)
        next_id = in_memory_db.setdefault("_ctr", 0) + 1
        in_memory_db["_ctr"] = next_id
        code = str(next_id)
        in_memory_db.setdefault("links", {})[code] = url.url
        return {"short_code": code}


@router.get("/{short_code}")
async def redirect_url(short_code: str):
    url = in_memory_db.get("links", {}).get(short_code, {})
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    redirects.inc()
    return RedirectResponse(url=url, status_code=302)
