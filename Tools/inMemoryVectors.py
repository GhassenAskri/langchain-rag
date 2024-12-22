from langchain_community.vectorstores import DocArrayInMemorySearch
from Tools.openai import OpenAI

class InMemoryVectorDb:
    @staticmethod
    def search_from(documents):
        return DocArrayInMemorySearch.from_documents(documents, OpenAI.get_embeddings_model())