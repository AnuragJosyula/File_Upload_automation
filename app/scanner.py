import os
import pyclamd

CLAMD_HOST = os.getenv("CLAMD_HOST", "clamav")
CLAMD_PORT = int(os.getenv("CLAMD_PORT", 3310))

def get_clamd_client():
    # Connect via TCP, fallback to local socket if needed
    try:
        cd = pyclamd.ClamdNetworkSocket(CLAMD_HOST, CLAMD_PORT)
        cd.ping()
        return cd
    except Exception:
        try:
            cd = pyclamd.ClamdUnixSocket()
            cd.ping()
            return cd
        except Exception as e:
            raise RuntimeError(f"Cannot connect to clamd: {e}")

def scan_bytes(data: bytes) -> dict:
    client = get_clamd_client()
    # scan_stream returns None if clean, or a dict with detection
    result = client.scan_stream(data)
    if result is None:
        return {"status": "clean"}
    # result example: {'stream': ('FOUND', 'Eicar-Test-Signature')}
    key = next(iter(result))
    action, name = result[key]
    return {"status": "infected", "signature": name}
