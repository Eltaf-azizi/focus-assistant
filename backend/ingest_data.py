import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import gdown


# Download .env file from gdrive
file_id = ""
url = f""
output = ".env" # Change the filename as needed


gdown.download(url, output, quit=False)



# Load environment variables
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "db")



# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API not found in .env")



# Load Documents
documents = []