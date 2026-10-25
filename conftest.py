"""Register the live-test option and isolate embeddings in offline unit tests."""
import hashlib
import os
import pytest

os.environ.setdefault("OPENROUTER_API_KEY", "offline-test")


def pytest_addoption(parser):
    parser.addoption("--run-llm", action="store_true", default=False)


def pytest_configure(config):
    config.addinivalue_line("markers", "llm: makes real model calls with --run-llm")


@pytest.fixture(autouse=True)
def offline_embeddings(request, monkeypatch):
    import memory
    client = memory.chromadb.Client()
    for collection in client.list_collections():
        client.delete_collection(collection.name)
    if request.node.get_closest_marker("llm") and request.config.getoption("--run-llm"):
        return
    def embed(text):
        digest = hashlib.sha256(text.encode()).digest()
        return [float(byte + 1) / 256 for byte in digest]
    monkeypatch.setattr(memory, "_embed", embed)
