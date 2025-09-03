from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_shorten_and_redirect():
    # create short link
    resp = client.post("/urls/shorten", json={"url": "https://example.com"})
    assert resp.status_code == 200
    data = resp.json()
    code = data["short_code"]

    # redirect lookup
    resp = client.get(f"/urls/{code}")
    assert resp.status_code == 200
    assert resp.json() == "https://example.com"


def test_dict_lookup_benchmark(benchmark):
    store = {"1": "https://example.com"}

    def lookup():
        return store.get("1")

    result = benchmark(lookup)
    assert result == "https://example.com"
