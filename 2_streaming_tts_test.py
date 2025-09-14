import asyncio
import os
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

async def main():
    # Read text lines from Rishi_text.txt
    with open('Rishi_text.txt', 'r') as f:
        text_lines = f.read().splitlines()

    # Combine lines for narration (can process line-by-line if preferred)
    narration = " ".join(text_lines)

    # Set up OpenAI async client
    client = AsyncOpenAI(api_key=api_key)

    # Create and stream TTS speech
    stream = await client.audio.speech.create(
        model="gpt-4o-mini-tts",
        input=narration,
        voice="alloy",
        response_format="pcm"
        # stream=True,
    )
    

    # Play on laptop speakers
    await LocalAudioPlayer().play(stream)

asyncio.run(main())