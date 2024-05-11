import random
from qdrant_client import QdrantClient, models
from langchain_core.documents import Document
from langchain_community.retrievers import(
    QdrantSparseVectorRetriever,
)

def connect():
    client = QdrantClient(location=":memory:")
    return client

def create_collection(client, collection_name):
    client.create_collection (
        collection_name,
        vectors_config={},
        sparse_vectors_config= {
            vector_name: models.SparseVectorParams (
                index=models.SparseIndexParams (
                    on_disk=False,
                )
            )
        },
    )

def demo_encoder(_: str) -> tuple[list[int], list[float]]:
    return (
        sorted(random.sample(range(100), 100)),
        [random.uniform(0.1, 1.0) for _ in range(100)],
    )

def create_vectors(client, collection_name, vector_name):
    vectors = QdrantSparseVectorRetriever(
        client=client,
        collection_name=collection_name,
        sparse_vector_name=vector_name,
        sparse_encoder=demo_encoder,
    )

    docs = [
        Document(
            metadata={
                "title": "Beyond Horizons: AI Chronicles",
                "author": "Dr. Cassandra Mitchell",
            },
            page_content="An in-depth exploration of the fascinating journey of artificial intelligence, narrated by Dr. Mitchell. This captivating account spans the historical roots, current advancements, and speculative futures of AI, offering a gripping narrative that intertwines technology, ethics, and societal implications.",
        ),
        Document(
            metadata={
                "title": "Synergy Nexus: Merging Minds with Machines",
                "author": "Prof. Benjamin S. Anderson",
            },
            page_content="Professor Anderson delves into the synergistic possibilities of human-machine collaboration in 'Synergy Nexus.' The book articulates a vision where humans and AI seamlessly coalesce, creating new dimensions of productivity, creativity, and shared intelligence.",
        ),
        Document(
            metadata={
                "title": "AI Dilemmas: Navigating the Unknown",
                "author": "Dr. Elena Rodriguez",
            },
            page_content="Dr. Rodriguez pens an intriguing narrative in 'AI Dilemmas,' probing the uncharted territories of ethical quandaries arising from AI advancements. The book serves as a compass, guiding readers through the complex terrain of moral decisions confronting developers, policymakers, and society as AI evolves.",
        ),
        Document(
            metadata={
                "title": "Sentient Threads: Weaving AI Consciousness",
                "author": "Prof. Alexander J. Bennett",
            },
            page_content="In 'Sentient Threads,' Professor Bennett unravels the enigma of AI consciousness, presenting a tapestry of arguments that scrutinize the very essence of machine sentience. The book ignites contemplation on the ethical and philosophical dimensions surrounding the quest for true AI awareness.",
        ),
        Document(
            metadata={
                "title": "Silent Alchemy: Unseen AI Alleviations",
                "author": "Dr. Emily Foster",
            },
            page_content="Building upon her previous work, Dr. Foster unveils 'Silent Alchemy,' a profound examination of the covert presence of AI in our daily lives. This illuminating piece reveals the subtle yet impactful ways in which AI invisibly shapes our routines, emphasizing the need for heightened awareness in our technology-driven world.",
        ),
    ]

    vectors.add_documents(docs)
    return vectors

def search_query(client, vectors):
    vectors.invoke (
        "Life and ethical dilemmas of AI",
    )

    print(vectors)

client = connect()
collection_name = "sparse_collection"
vector_name = "sparse_vector"

print('')
create_collection(client, collection_name)

print('')
vectors = create_vectors(client, collection_name, vector_name)

print('')
search_query(client, vectors)
