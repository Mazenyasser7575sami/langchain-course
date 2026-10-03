import os
from dotenv import load_dotenv
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from openai.types.audio.transcription_create_params import ChunkingStrategy

load_dotenv()

if __name__ == '__main__':
    print("Ingesting...")
    print(os.environ['PINECONE_API_KEY'])
    loader=UnstructuredLoader('./mediumblog1.txt',chuncking_strategy='basic',max_charachters=1000000)
    document=loader.load()
    print('splitting')
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    print("ingesting...")
    PineconeVectorStore.from_documents(
        texts, embeddings, index_name=os.environ["INDEX_NAME"]
    )
    print("finish")


