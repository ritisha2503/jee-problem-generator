from app.rag import index_pdfs, get_context

def main():
    print("Hello from rag-jee!")
    
    # 1. Index the PDFs (Only strictly needed the first time, but fine for testing)
    print("\n--- Indexing Source PDFs ---")
    index_status = index_pdfs()
    print(index_status)
    
    # 2. Query the vector database
    query = "What is the formula for the area of a circle?"
    print(f"\n--- Querying Vector DB for: '{query}' ---")
    
    results = get_context(query)
    
    # 3. Print out the retrieved chunks
    if isinstance(results, str):
        print(results)
    elif not results:
        print("No matching context found in the database.")
    else:
        print(f"Retrieved {len(results)} relevant chunks:\n")
        for i, doc in enumerate(results, 1):
            print(f"--- Chunk {i} (Source: {doc.metadata.get('source', 'Unknown')}) ---")
            print(doc.page_content)
            print("-" * 40)

if __name__ == "__main__":
    main()