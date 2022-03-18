from flask import Flask, render_template
from deepgram import Deepgram
import os
import asyncio
from aiohttp import web
from aiohttp_wsgi import WSGIHandler
from helpers._constants import KEYWORDS
from typing import Dict, Callable
from helpers.actions import make_move
import logging
import sys

# Initializing the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


app = Flask("aioflask")

dg_client = Deepgram(os.getenv("DEEPGRAM_API_KEY"))
logging.info("ws deepgram client created successfully")


async def process_audio(fast_socket: web.WebSocketResponse):
    async def get_transcript(data: Dict) -> None:
        if "channel" in data:
            transcript = data["channel"]["alternatives"][0]["transcript"]

            if transcript:
                # this is the place where we initiate the commands
                make_move(transcript)
                await fast_socket.send_str(transcript)

    deepgram_socket = await connect_to_deepgram(get_transcript)

    return deepgram_socket


async def connect_to_deepgram(
    transcript_received_handler: Callable[[Dict], None]
) -> str:
    try:
        socket = await dg_client.transcription.live(
            {
                "interim_results": False,
                "language": "en-IN",
                "keywords": KEYWORDS,
            }
        )
        socket.registerHandler(
            socket.event.CLOSE, lambda c: print(f"Connection closed with code {c}.")
        )
        socket.registerHandler(
            socket.event.TRANSCRIPT_RECEIVED, transcript_received_handler
        )

        return socket
    except Exception as e:
        raise Exception(f"Could not open socket: {e}")


@app.route("/")
def index():
    return render_template("index.html")


async def socket(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    deepgram_socket = await process_audio(ws)

    while True:
        data = await ws.receive_bytes()
        deepgram_socket.send(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    aio_app = web.Application()
    wsgi = WSGIHandler(app)
    aio_app.router.add_route("*", "/{path_info: *}", wsgi.handle_request)
    aio_app.router.add_route("GET", "/listen", socket)
    logging.info("Started the server. Listining....")
    web.run_app(aio_app, port=5555)
