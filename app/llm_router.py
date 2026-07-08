import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_math_problem(model_choice: str, topic: str, context_documents: list) -> str:
    context_str = "\n---\n".join([doc.page_content for doc in context_documents])
    
    # Initialize the single unified OpenRouter client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
    
    # Map your UI dropdown values to OpenRouter's specific free model IDs
    model_mapping = {
        "gemini-flash-lite": "google/gemini-2.5-flash:free",  # active free flash tier
        "qwen": "qwen/qwen3-coder:free",                      # active free qwen variants
        "kimi": "liquid/lfm-2.5-1.2b-thinking:free"           # fallback free complex reasoning model
    }
    
    selected_model_id = model_mapping.get(model_choice, "openrouter/free")

    system_prompt = (
        "You are an elite IIT-JEE Advanced Mathematics Professor. Generate a completely new, "
        "highly challenging problem inspired by the context. Use clean Markdown and LaTeX.\n\n"
        "Separate your output into: '### PROBLEM' and '### STEP-BY-STEP SOLUTION'."
    )
    user_prompt = f"Target Topic: {topic}\n\nContext:\n{context_str}"

    response = client.chat.completions.create(
        model=selected_model_id,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        # Optional OpenRouter ranking headers
        extra_headers={
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "MathGen-RAG",
        }
    )
    return response.choices[0].message.content