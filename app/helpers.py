from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
    StorageContext,
)
import os
from os import environ
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def some_helper_function():
    pass