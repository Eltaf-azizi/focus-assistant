import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
import gdown



# Download .env file from gdrive
file_id = ""
url = f""
output = ".env" # Change the filename as needed

gdown.download(url, output, quiet=False)


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "db")


# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API keu not found in .env")



# Load Stored vector database
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vector_db = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
retriever = vector_db.as_retriever()




# Use GPT-3.5 for answer generation
llm = ChatOpenAI(model_name="gpt-turbo-3.5", openai_api_key=OPENAI_API_KEY)


# Create Retrieval-augmented Generation (RAG) Chain
