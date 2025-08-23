# About The Project

## What a URL Shortener Actually Is?

The primary goal is to map a short code (like u.cz/abc123) to a long URL (like https://very-long…). There are concepts called `hot path` and `cold path`:  

- **hot path (read):** client hits `GET /{code}` → service looks up code → long_url → returns an HTTP redirect (usually 302/307) to the long URL.
- **cold path (write):** client calls `POST /shorten` with the long URL → service validates → generates a unique code → stores `{code, long_url, metadata}`.

The overall shape of traffic is read-heavy (90–99% reads), latency-sensitive on the redirect path. The core design idea is to keep the hot path `O(1)` by making `code` as the primary key.


## Basic Concepts We'll Use

- code generation: counter+base62, random base62, or distributed ID (Snowflake) then base62.
- capacity: base62^6 ≈ 56.8B, ^7 ≈ 3.5T, ^8 ≈ 218T.
- redirect status: 302/307 (temporary) is safer to avoid client caching; 301 (permanent) is fine if links never change.
- storage: start with in-memory dict → SQLite → Postgres; add Redis cache later.
- observability: logs + metrics + traces from day 1 (keep it simple first).
- abuse & safety: URL validation, rate limit, domain allow/block lists, malware checks (later).