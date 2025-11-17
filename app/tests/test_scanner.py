import pytest
from app.scanner import scan_bytes

def test_scan_clean_bytes(monkeypatch):
    class DummyClient:
        def ping(self): pass
        def scan_stream(self, data):
            return None
    monkeypatch.setattr("app.scanner.get_clamd_client", lambda: DummyClient())
    res = scan_bytes(b"hello")
    assert res["status"] == "clean"
