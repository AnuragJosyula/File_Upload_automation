from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from .scanner import scan_bytes
from .schemas import ScanResult

app = FastAPI(title="File Scan Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/scan", response_model=ScanResult)
async def scan_file(file: UploadFile = File(...)):
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty file")
    try:
        result = scan_bytes(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(content=result)
