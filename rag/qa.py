import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def answer_question(question, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer cannot be found in the context,
say:

"I could not find this information in the video."

Context:
{context}

Question:
{question}

Answer:
"""

    for attempt in range(3):
        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except Exception as e:

            print(f"Gemini Error: {e}")

            if attempt == 2:
                return (
                    "Gemini API is currently unavailable. "
                    "Please try again later."
                )

            time.sleep(5)