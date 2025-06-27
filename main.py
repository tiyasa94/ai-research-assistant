from services.arxiv_api import fetch_research_articles
from summarize_papers_with_llm import summarize_papers_with_llm
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("🔍 AI Research Paper Assistant")
    print("-------------------------------")
    
    # Step 1: Get research topic
    topic = input("Enter a research topic (e.g., game theory and agents): ").strip()
    print(f"\n📥 Fetching recent papers on: {topic} ...")
    
    # Step 2: Fetch papers and summaries
    paper_ids, paper_summaries = fetch_research_articles(query=topic, limit=10)
    paper_context = "\n\n".join(paper_summaries)
    
    print(f"✅ Fetched {len(paper_ids)} papers.\n")
    
    # Step 3: Get user question
    user_question = input("Ask your question based on the papers: ").strip()
    print("\n🤖 Generating answer using OpenRouter LLM...\n")
    
    # Step 4: Generate LLM answer
    response = summarize_papers_with_llm(query=user_question, topic=topic)
    print("💡 Answer:\n")
    print(response)

    # Step 6: User feedback loop
    feedback = input("\n👍 Did you like the answer? (y/n): ").strip().lower()
    if feedback == 'y':
        with open("feedback_log.txt", "a") as f:
            f.write(f"Topic: {topic}\nQuestion: {user_question}\nAnswer: {response}\n---\n")
        print("✅ Feedback saved!")

if __name__ == "__main__":
    main()
