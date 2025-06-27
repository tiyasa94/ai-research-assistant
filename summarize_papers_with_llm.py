import os
import json
from openrouter_llm import query_openrouter

DATA_FOLDER = "papers"

def summarize_papers_with_llm(query: str, topic: str, max_papers: int = 5) -> str:
    topic_dir = os.path.join(DATA_FOLDER, topic.lower().replace(" ", "_"))
    metadata_path = os.path.join(topic_dir, "metadata.json")

    try:
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
    except Exception as e:
        return f"Error loading metadata for topic '{topic}': {str(e)}"

    context = ""
    for i, (paper_id, meta) in enumerate(metadata.items()):
        if i >= max_papers:
            break
        context += (
            f"Title: {meta['title']}\n"
            f"Authors: {', '.join(meta['authors'])}\n"
            f"Summary: {meta['summary'][:400]}...\n\n"
        )

    if not context:
        return f"No papers found for topic: '{topic}'"

    return query_openrouter(query, context)
