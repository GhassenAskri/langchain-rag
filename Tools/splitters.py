from enum import Enum
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



class Splitters:

    documents = None

    @classmethod
    def load(cls, file_path: str):
        cls.documents = TextLoader(file_path).load()
        return cls

    @classmethod
    def splitUsingRecursiveCharacterTextSplitter(cls, size: int, overlap: int):
        if not cls.documents:
            raise ValueError("Documents not loaded. Call load() first.")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=overlap)
        return text_splitter.split_documents(cls.documents)