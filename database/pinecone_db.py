import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

class VectorStore:
    def __init__(self):
        self.api_key = os.getenv("PINECONE_API_KEY")
        self.environment = os.getenv("PINECONE_ENV", "us-east-1")
        self.index_name = os.getenv("PINECONE_INDEX", "spatial-memory")
        
        if self.api_key:
            self.pc = Pinecone(api_key=self.api_key)
            self._ensure_index()
            self.index = self.pc.Index(self.index_name)
        else:
            self.pc = None
            self.index = None

    def _ensure_index(self):
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=1536, # Standard for text-embedding-3-small or similar
                metric='cosine',
                spec=ServerlessSpec(cloud='aws', region=self.environment)
            )

    def query_spatial_memory(self, query_text: str, top_k: int = 5):
        if not self.index:
            return {"error": "Vector store not configured", "matches": []}
        
        # In a real implementation, we would generate embeddings for query_text here
        # For the demo context, we simulate the structure of a real response
        return self.index.query(
            vector=[0.1] * 1536, # Placeholder for real embedding
            top_k=top_k,
            include_metadata=True
        )

    def store_item(self, item_id: str, vector: list, metadata: dict):
        if self.index:
            self.index.upsert(vectors=[(item_id, vector, metadata)])

vector_store = VectorStore()
