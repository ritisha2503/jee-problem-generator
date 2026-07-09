import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate_math_problem(model_choice: str, topic: str, context_documents: list) -> str:
    """
    Directly routes to Google AI Studio's production endpoints to bypass 
    congested third-party proxy rate limits.
    """
    context_str = "\n---\n".join([doc.page_content for doc in context_documents])
    
    system_prompt = (
        "You are an elite IIT-JEE Advanced Mathematics Professor. Your task is to generate a completely new, "
        "highly challenging, conceptually deep problem inspired by the structural complexity of the provided context. "
        "Do not copy the reference questions. Synthesize a brand new problem.\n\n"
        "Formatting constraints:\n"
        "1. Write everything using clean Markdown and flawless LaTeX notation for equations.\n"
        "2. Break your output into two clear, distinct sections: '### PROBLEM' and '### STEP-BY-STEP SOLUTION'.\n"
        "3. Ensure the solution contains clear algebraic or geometric verification steps."
    )
    
    user_prompt = f"Target Topic: {topic}\n\nReference Material/Context:\n{context_str}"
    
    try:
        # Initialize the native Google GenAI client
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # We target gemini-2.5-flash (optimized for ultra-fast RAG task handling)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7
            )
        )
        return response.text

    except Exception as e:
        return f"Direct Gemini SDK Error: {str(e)}"