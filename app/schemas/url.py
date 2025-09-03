from pydantic import BaseModel


class URLShortenIn(BaseModel):
    url: str
