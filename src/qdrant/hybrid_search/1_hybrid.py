# https://qdrant.tech/documentation/tutorials/hybrid-search-fastembed/
# wget https://storage.googleapis.com/generall-shared-data/startups_demo.json
# pip install "qdrant-client[fastembed]>=1.8.2"
# pip install fastapi uvicorn

# Import client library
from qdrant_client import QdrantClient
client = QdrantClient(":memory:")

#client = QdrantClient(url="http://localhost:6333")

client.set_model("sentence-transformers/all-MiniLM-L6-v2")
# comment this line to use dense vectors only
client.set_sparse_model("prithivida/Splade_PP_en_v1")

# Create Collections
client.recreate_collection(
    collection_name="startups",
    vectors_config=client.get_fastembed_vector_params(),
    # comment this line to use dense vectors only
    sparse_vectors_config=client.get_fastembed_sparse_vector_params(),  
)


# Import Json
import json

payload_path = "startups_demo.json"
metadata = []
documents = []

with open(payload_path) as fd:
    for line in fd:
        obj = json.loads(line)
        documents.append(obj.pop("description"))
        metadata.append(obj)

# Encode Data
client.add(
    collection_name="startups",
    documents=documents,
    metadata=metadata,
    parallel=0,  # Use all available CPU cores to encode data. 
    # Requires wrapping code into if __name__ == '__main__' block
)



# Monitoring Progress
from tqdm import tqdm
client.add(
    collection_name="startups",
    documents=documents,
    metadata=metadata,
    ids=tqdm(range(len(documents))),
)
