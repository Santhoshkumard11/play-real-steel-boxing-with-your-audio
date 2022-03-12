# deepgram_test.py

from deepgram import Deepgram
import asyncio
import os


# Your Deepgram API Key
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")


async def main():
    dg_client = Deepgram(DEEPGRAM_API_KEY)


asyncio.run(main())
