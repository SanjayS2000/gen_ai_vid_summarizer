from rag.chunking import chunk_text

sample_text = """
This is a sample transcript.
""" * 1000

chunks = chunk_text(sample_text)

print("Chunks:", len(chunks))
print(chunks[0][:100])