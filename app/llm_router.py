import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_math_problem(model_choice: str, topic: str, context_documents: list) -> str:
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

    client = OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    try:
        completion = client.chat.completions.create(
            model = model_choice,
            messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
            ],
            max_tokens=8192
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"