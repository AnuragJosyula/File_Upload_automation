from pydantic import BaseModel

class ScanResult(BaseModel):
    status: str
    signature: str | None = None
