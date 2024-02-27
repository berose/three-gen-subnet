import argparse
import time

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import Response


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=10006)
    return parser.parse_args()


args = get_args()
app = FastAPI()


@app.post("/generate/")
async def generate(
    prompt: str = Form(),
):
    print(f"INFO: Task received - {prompt}")
    time.sleep(30.0)
    buffer = b"MOCK DATA"
    return Response(content=buffer, media_type="application/octet-stream")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=args.port)
