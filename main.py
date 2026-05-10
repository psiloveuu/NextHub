import os

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pathlib import Path

# ================= SETUP =================
BASE_DIR = Path(__file__).resolve().parent

# ================= APP =================
app = FastAPI(title="NextHub Legacy Redirect")

LOADER_TEXT = (BASE_DIR / "loaders" / "loader.lua").read_text(encoding="utf-8")

@app.get("/script/loader.lua", response_class=PlainTextResponse)
async def serve_loader():
    return LOADER_TEXT

# ================= ENTRY POINT =================
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        workers=2,
        timeout_keep_alive=75,
        backlog=2048,
        limit_concurrency=1000,
        log_level="warning",
        access_log=False,
        loop="uvloop",
    )