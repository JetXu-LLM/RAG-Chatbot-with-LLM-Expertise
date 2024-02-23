# modules.py
from llama_index.core.storage.storage_context import StorageContext
from llama_index.legacy.vector_stores.milvus import MilvusVectorStore
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from ragchatbot.config import Config
import textwrap

class IndexManager:
    def __init__(self):
        self.vector_store = MilvusVectorStore(dim=Config.get('vector_dim'), collection_name=Config.get('collection_name'))
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        self._initialize_or_connect_index()

    def _initialize_or_connect_index(self):
        documents = SimpleDirectoryReader("../data/").load_data()
        self.index = VectorStoreIndex.from_documents(
            documents, storage_context=self.storage_context
        )

    def load_and_index_documents(self):
        self.query_engine = self.index.as_query_engine()

    def reconnect_to_existing_index(self):
        pass

    def search_in_index(self, top_k=10):
        pass

    def answer_question(self, question):
        response = self.query_engine.query(question)
        return textwrap.fill(str(response), 100)

    def close(self):
        pass