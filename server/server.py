from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
import random

app = FastAPI()

@app.get("/")
async def get():
    return FileResponse("../client/client.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if (data=="requestGenerate"):
            await websocket.send_text(str(random.randrange(1,100)))