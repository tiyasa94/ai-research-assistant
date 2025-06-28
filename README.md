# AI Research Paper Assistant

An intelligent assistant that fetches **recent arXiv papers**, stores them as **semantic vectors**, and answers your queries using **OpenRouter-powered LLMs** — enhanced with a **feedback loop** for long-term memory and learning.

---

## What This Project Does

🔹 Fetches the latest arXiv papers based on any research topic  
🔹 Stores paper summaries in a **vector database (ChromaDB)**  
🔹 Lets you ask custom questions on those papers  
🔹 Generates answers using **LLMs via OpenRouter**  
🔹 Learns from your feedback — stores useful Q&A for future queries

---

## How It Works (System Flow)

### Step 1: Topic Input  
You provide a research topic like:


### Step 2: Real-time Paper Fetching  
- The app fetches 5–10 recent papers via the **arXiv API**  
- Metadata + summaries are saved in JSON

### Step 3: Vector Storage  
- All summaries are embedded (using OpenRouter embedding model)
- Stored in **ChromaDB** for semantic search

### Step 4: Ask a Question  
You can now ask any question like:


- The app:
  - Retrieves top `k` relevant summaries from ChromaDB
  - Fuses them into a context block
  - Sends the context + question to OpenRouter LLM (like `mistralai/mistral-8b`)

### Step 5: Feedback Loop  
If you like the answer:
- The app logs the **Q&A pair into ChromaDB**
- These become part of memory for future question answering

---

## Tech Stack

| Category            | Tools Used |
|---------------------|------------|
| LLM Backend         | [OpenRouter](https://openrouter.ai/) (`openai/gpt-4o-mini-search-preview`) |
| Paper Fetching      | [arXiv API](https://arxiv.org/help/api/) |
| Vector Store        | [ChromaDB](https://www.trychroma.com/) |
| Embeddings          | OpenRouter |
| Context Fusion      | Custom code (RAG-style) |
| Feedback Storage    | ChromaDB + backup log file |
| Interface           | Command Line (Python CLI) |

---

## Setup Instructions

1. **Clone the Repo**
```bash
git clone https://github.com/tiyasa94/ai-research-assistant.git
cd ai-research-assistant
```
2. **Install Dependencies**
```bash
pip install -r requirements.txt
```
3. **Configure API Key**
   - Create a .env file like this:
   - ```bash
     OPENROUTER_API_KEY=your_api_key_here
     ```

---

## Sample Run
$ python3 main.py

AI Research Paper Assistant
-------------------------------
Enter a research topic (e.g., game theory and agents): AI Agents
📥 Fetching recent papers on: AI Agents ...
✅ Fetched 10 papers.

Ask your question based on the papers: How are agents used in game theory?

🤖 Generating answer using OpenRouter LLM...

💡 Answer:
"Recent papers explore coordination strategies using Nash equilibrium, with multi-agent systems
incorporating reinforcement learning..."

👍 Did you like the answer? (y/n): y
✅ Feedback saved!





   



