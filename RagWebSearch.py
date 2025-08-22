from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.vectorstores import InMemoryVectorStore


from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


loader = WebBaseLoader(
   web_paths=["https://www.educosys.com/course/genai"]
)
docs = loader.load()

print("came here 1")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)
print("came here 2")

#for split in all_splits:
   #print(split.page_content)
   #print("--------------------------------------------------")  
#print("Number of splits",all_splits.__len__())



vectorstore = Chroma(collection_name="educosys_genai_info", embedding_function=embeddings, persist_directory="./chroma_genai")
print("came here 3")


#vectorstore.add_documents(documents=all_splits)
print("Total Chunks stored in Vectorstore:", vectorstore._collection.count())  # Check total stored chunks

print(vectorstore._collection.count())  # Check total stored chunks