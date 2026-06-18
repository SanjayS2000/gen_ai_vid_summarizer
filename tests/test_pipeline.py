from transcript import get_transcript
from rag.chunking import chunk_text
from rag.embeddings import create_embeddings
from rag.vector_store import create_index

from rag.vector_store import create_index
from rag.retrieval import search_chunks
from rag.embeddings import get_embedding_model

from rag.qa import answer_question

url = input("Enter YouTube URL: ")

data = get_transcript(url)

print(f"\nTranscript Length: {len(data['text'])}")

#====================== chunking ======================
chunks = chunk_text(data["text"])

print(f"Chunks Created: {len(chunks)}")

print("\nFirst Chunk Preview:")
print(chunks[0][:300])

for i, chunk in enumerate(chunks):
    if "12%" in chunk:
        print(f"\nFOUND IN CHUNK {i}")
        print(chunk[:500])

#====================== embedding =======================
embeddings = create_embeddings(chunks)

print(f"Embedding Shape: {embeddings.shape}")

print("\nEmbedding Dimension:")
print(embeddings.shape[1])

#======================== FAISS ====================
print("\n[STEP 4] Building FAISS Index...")

index = create_index(embeddings)

print(
    f"Vectors Stored: {index.ntotal}"
)

print(f"Index Dimension: {index.d}")

print("\n[STEP 5] Retrieval Test")

query = input(
    "\nAsk a question about the video: "
)

model = get_embedding_model()

results = search_chunks(
    query=query,
    model=model,
    index=index,
    chunks=chunks,
    top_k=10
)

for i, chunk in enumerate(results, start=1):
    print(f"\nMatch #{i}")
    print(chunk[:300])

#=====================step 6===================================
print("\n[DEBUG] Context Sent To Gemini")

context = "\n\n".join(results)

print(context[:1000])

print("\n[STEP 6] Gemini Answer")

answer = answer_question(
    question=query,
    retrieved_chunks=results
)

print("\nAnswer:")
print(answer)

print("\nPipeline Success!")