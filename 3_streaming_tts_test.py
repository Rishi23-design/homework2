import os
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI client
client = AsyncOpenAI(api_key=api_key)

# Voices and effects to cycle through
voices = ["alloy", "onyx", "echo", "fable"]
effects = [
    {"speed": 1.0, "pitch": 1.0},    # Normal
    {"speed": 0.9, "pitch": 1.2},    # Lower speed, higher pitch
    {"speed": 1.1, "pitch": 0.8},    # Higher speed, lower pitch
    {"speed": 0.7, "pitch": 1.5},    # Slow and high pitch
]

# Input text (customize as desired)
input_text = (
    "Welcome to an exploration of voice and effects using OpenAI Text-to-Speech. "
    "Each voice and setting brings unique character and clarity. "
    "Let's experience the difference between alloy, onyx, echo, and fable."
)

# Create output directory
os.makedirs("tts_outputs", exist_ok=True)

import asyncio

async def main():
    # Generate audio for all combinations
    for voice in voices:
        for effect in effects:
            # Descriptive filename
            filename = f"tts_outputs/{voice}_speed{effect['speed']}_pitch{effect['pitch']}.mp3"
            print(f"Generating {filename}...")
            response = await client.audio.speech.create(
                model="gpt-4o-mini-tts",
                input=input_text,
                voice=voice,
                speed=effect["speed"],
                # pitch=effect["pitch"],
            )
            # Save to file
            with open(filename, "wb") as f:
                f.write(response.content)

    print("All TTS files generated! Listen to tts_outputs/ for results.")

if __name__ == "__main__":
    asyncio.run(main())