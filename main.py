import os
from dotenv import load_dotenv
from app.rag import index_pdfs, get_context
from app.llm_router import generate_math_problem

# Explicitly load environment variables from your local .env file
load_dotenv()

def run_integration_test():
    print("Starting JEE Adv RAG integration Test...")

    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY is missing from your .env file")
        return

    print("\n[Step 1/3] Indexing Mathematics source PDFs from 'data/'...")
    index_status = index_pdfs()
    print(f"Status: {index_status}")
    
    # 3. Simulate a specific JEE Advanced Query Topic
    test_topic = "Complex Numbers geometry and triangle inequalities"
    print(f"\n[Step 2/3] Fetching LaTeX-split context for topic: '{test_topic}'...")
    
    retrieved_chunks = get_context(test_topic, k=2)
    
    if not retrieved_chunks:
        print("Warning: No chunks found. Make sure you dropped a valid math PDF into your './data/' folder.")
        print("Proceeding with empty context to test LLM baseline capabilities...")
    else:
        print(f"Successfully retrieved {len(retrieved_chunks)} relevant chunks.")
        for idx, chunk in enumerate(retrieved_chunks, 1):
            print(f"--- Ingested Context Snippet {idx} ---")
            print(chunk.page_content[:200].replace('\n', ' ') + "...")

    # 4. Route Context to OpenRouter Models
    # Available mapped models in router: 'gemini-flash-lite', 'qwen', 'kimi'
    selected_engine = "qwen" 
    print(f"\n[Step 3/3] Prompting model engine variant: '{selected_engine}' via OpenRouter...")
    
    try:
        generated_result = generate_math_problem(
            model_choice=selected_engine,
            topic=test_topic,
            context_documents=retrieved_chunks
        )

        print('----------------------------------------------')        
        print("\n\nLLM RESPONSE OUTPUT:\n")
        print(generated_result)
        print('----------------------------------------------')
        
    except Exception as e:
        print(f"\nExecution Failed during generation pipeline loop: {str(e)}")

if __name__ == "__main__":
    run_integration_test()