import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

# ================= SETUP =================
BASE_DIR = Path(__file__).resolve().parent

_loader_path = BASE_DIR / "loaders" / "loader.lua"
if not _loader_path.exists():
    raise RuntimeError(f"loader.lua not found at: {_loader_path}")

LOADER_TEXT = _loader_path.read_text(encoding="utf-8")

# ================= APP =================
app = FastAPI(title="NextHub Legacy Redirect")

@app.get("/script/loader.lua", response_class=PlainTextResponse)
async def serve_loader():
    return LOADER_TEXT

# ================= ENTRY POINT =================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
    )