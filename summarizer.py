import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize(transcript: str) -> str:

    prompt = f"""
You are an expert summarizer.

Generate:
1. Executive Summary
2. Key Takeaways
3. Bullet Points

Transcript:

{transcript[:50000]}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text