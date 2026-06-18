import numpy as np


# def search_chunks(
#     query,
#     model,
#     index,
#     chunks,
#     top_k=5
# ):
#     """
#     Retrieve the most relevant chunks
#     for a given query.
#     """

#     query_embedding = model.encode(
#         [query],
#         convert_to_numpy=True
#     )

#     distances, indices = index.search(
#         query_embedding.astype(np.float32),
#         top_k
#     )

#     results = []

#     for idx in indices[0]:
#         print(f"Retrieved Chunk: {idx}")

#         if idx < len(chunks):
#             results.append(chunks[idx])

#     return results

def search_chunks(
    query,
    model,
    index,
    chunks,
    top_k=10
):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        query_embedding.astype(np.float32),
        top_k
    )

    print("\nRetrieved Chunks:")
    print(indices[0])

    print("\nDistances:")
    print(distances[0])

    results = []

    for idx in indices[0]:

        print(f"Retrieved Chunk: {idx}")

        if idx < len(chunks):
            results.append(chunks[idx])

    return results