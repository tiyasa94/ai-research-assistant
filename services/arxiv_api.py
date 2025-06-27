import arxiv
import json
import os
import datetime
import pytz
from typing import List, Tuple

DATA_FOLDER = "papers"
utc = pytz.UTC
cutoff_date = utc.localize(datetime.datetime.now() - datetime.timedelta(days=5 * 365))

def fetch_research_articles(query: str, limit: int = 5) -> Tuple[List[str], List[str]]:
    arxiv_client = arxiv.Client()
    query_config = arxiv.Search(
        query=query,
        max_results=limit,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = arxiv_client.results(query_config)

    topic_dir = os.path.join(DATA_FOLDER, query.lower().replace(" ", "_"))
    os.makedirs(topic_dir, exist_ok=True)
    json_path = os.path.join(topic_dir, "metadata.json")

    try:
        with open(json_path, "r") as f:
            stored_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        stored_data = {}

    collected_ids = []
    summaries = []  # ✅ You missed this

    for result in results:
        if result.published < cutoff_date:
            continue
        paper_id = result.get_short_id()
        collected_ids.append(paper_id)
        summaries.append(result.summary.strip())  # ✅ Add summary
        metadata = {
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "summary": result.summary,
            "pdf_url": result.pdf_url,
            "published": str(result.published.date())
        }
        stored_data[paper_id] = metadata

    with open(json_path, "w") as f:
        json.dump(stored_data, f, indent=2)

    print(f"Metadata saved to: {json_path}")
    return collected_ids, summaries 
