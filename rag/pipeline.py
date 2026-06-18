from rag.chunking import chunk_text
from rag.embeddings import get_embedding_model
from rag.vector_store import create_index


def build_rag_pipeline(transcript_text):
    """
    Build complete RAG pipeline from transcript.

    Returns:
        {
            "chunks": chunks,
            "model": embedding_model,
            "index": faiss_index
        }
    """

    # Step 1: Chunking
    chunks = chunk_text(transcript_text)

    # Step 2: Embedding Model
    model = get_embedding_model()

    # Step 3: Generate Embeddings
    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    # Step 4: Build FAISS Index
    index = create_index(embeddings)

    return {
        "chunks": chunks,
        "model": model,
        "index": index
    }