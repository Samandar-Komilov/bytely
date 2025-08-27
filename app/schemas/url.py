from pydantic import BaseModel, HttpUrl


class URLShortenIn(BaseModel):
    url: str