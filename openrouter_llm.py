import os
from openai import OpenAI

def query_openrouter(user_query: str, context: str) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    completion = client.chat.completions.create(
        model="openai/gpt-4o-mini-search-preview",
        messages=[
            {"role": "system", "content": "You are an expert assistant helping users understand academic research papers."},
            {"role": "user", "content": f"User Query: {user_query}\n\nRelevant Research Context:\n{context}"}
        ]
    )

    return completion.choices[0].message.content
