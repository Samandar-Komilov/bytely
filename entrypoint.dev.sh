#!/bin/sh

alembic upgrade head
uvicorn app.main:app --port 8000 --reload