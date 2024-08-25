import subprocess
import json
import random
import time
import logging

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
logger = logging.getLogger("uvicorn")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """処理時間をヘッダーに付与する"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/run_codon")
async def get_random_nums_by_codon(count: int = 10000) -> JSONResponse:
    """Codonを使った処理を実行"""
    result = subprocess.run(
        ["./codon_bin/random_nums", str(count)], capture_output=True
    )
    json_data = []
    if result.stdout:
        json_data = json.loads(result.stdout.strip(b"\n"))
    return JSONResponse(content=json_data)


@app.get("/run_python")
async def get_random_nums(count: int = 10000) -> JSONResponse:
    """Pythonのみを使った処理を実行"""
    numbers = [random.randint(0, count) for _ in range(count)]

    # バブルソート(Codonと同様の処理)
    for _ in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return JSONResponse(content=numbers)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
