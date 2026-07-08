import os
from openai import OpenAI
from google import genai
from google.genai import types

def generate_math_problem(model_choice: str, topic: str, context_documents: list) -> str:
    '''
    Generates a math problem based on the given topic and context documents using the specified model.
    '''
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

    # 1. Routing to Gemini Flash-Lite
    if model_choice == "gemini-flash-lite":
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite', # Using current active Flash-Lite production model
            contents=user_prompt,
            config=types.GenerateContentConfig(system_instruction=system_prompt)
        )
        return response.text

    # 2. Routing to Kimi K2.6 via Moonshot/OpenAI SDK compatibility
    elif model_choice == "kimi":
        client = OpenAI(api_key=os.getenv("KIMI_API_KEY"), base_url="https://api.moonshot.cn/v1")
        response = client.chat.completions.create(
            model="kimi-k2.6", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content

    # 3. Routing to Qwen via DashScope/OpenRouter
    elif model_choice == "qwen":
        # Adjust base_url/headers to match your specific API provider endpoint (e.g., OpenRouter or Alibaba DashScope)
        client = OpenAI(api_key=os.getenv("QWEN_API_KEY"), base_url="https://openrouter.ai/api/v1")
        response = client.chat.completions.create(
            model="qwen/qwen-2.5-72b-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
        
    return "Invalid Model Choice Selected."