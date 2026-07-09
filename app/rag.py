import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

DB_DIR = './chroma_db'
DATA_DIR = './data'

def index_pdfs():
    '''
    Loads PDFs from data/, splits them by LaTeX rules, and saves to ChromaDB.
    '''
    if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
        return "No PDFs found in 'data/' directory"
    
    documents = []
    for file in os.listdir(DATA_DIR):
        if file.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(DATA_DIR, file))
            documents.extend(loader.load())

    latex_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 500,
        separators = [
            "\n\n",                 # Paragraphs
            "$$",                   # Display math blocks
            "\\[", "\\]",           # Explicit LaTeX block bounds
            "\\begin{equation}", "\\end{equation}",
            "\\begin{align}", "\\end{align}",
            "\n", " "               # Standard text blocks
        ]
    )

    chunks = latex_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model="BAAI/bge-small-en-v1.5")
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    batch_size = 16
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        print(f"Syncing batch {i // batch_size + 1} / {-(-len(chunks) // batch_size)}...")
        vectorstore.add_documents(batch)
    
    return f"Successfully indexed {len(chunks)} chunks from source documents."

def get_context(query: str, k: int = 3):
    '''
    Retrieves relevant formula/problem context based on user query.
    '''
    embeddings = HuggingFaceEmbeddings(model="BAAI/bge-small-en-v1.5")
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)