from transcript import get_transcript
from rag.pipeline import build_rag_pipeline

url = input("Enter YouTube URL: ")

data = get_transcript(url)

rag_data = build_rag_pipeline(data["text"])

print("\nPipeline Built Successfully")

print("Chunks:", len(rag_data["chunks"]))
print("Index Size:", rag_data["index"].ntotal)