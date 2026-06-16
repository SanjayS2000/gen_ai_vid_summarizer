import os
import re
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def clean_transcript(text: str) -> str:
    """Clean transcript before sending to the LLM."""

    # Remove music symbols
    text = re.sub(r"[♪♫]+", " ", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def summarize(transcript: str):

    transcript = clean_transcript(transcript)

    prompt = f"""
You are an expert YouTube video summarizer.

Produce:
- Executive Summary
- Key Takeaways
- Main Topics
- Important Insights

If the transcript appears to be lyrics or entertainment content,
summarize its themes instead of treating it as a tutorial.

Transcript:

{transcript[:30000]}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except Exception:
            if attempt == 2:
                raise

            time.sleep(2)