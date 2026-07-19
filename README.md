# 🧠 ResearchMind AI

An industry-grade Multi-Agent Research Paper Analysis platform built using **LangGraph**, **LangChain**, **LLMs**, and **Streamlit**.

ResearchMind AI automatically analyzes research papers using multiple AI agents that collaborate to extract metadata, analyze methodology, summarize content, detect hallucinations, verify claims, review quality, calculate confidence, and generate professional reports.

---

## ✨ Features

- 📄 Automatic PDF Research Paper Analysis
- 🤖 Multi-Agent LangGraph Workflow
- 🧠 11 Specialized AI Agents
- 🔍 Fact Checking
- 🚨 Hallucination Detection
- ⭐ Research Quality Review
- 📊 Confidence Scoring
- 📝 Executive, Technical & Beginner Summaries
- 📚 Citation Extraction
- 💡 Research Insights
- 📄 Professional Report Generation
- 📤 Export Reports (Markdown, JSON, PDF)
- 💬 AI Chat with Research Paper
- 🌐 Interactive Streamlit Dashboard

---
# 🏗️ System Architecture

```
                ┌────────────────────┐
                │   Upload PDF       │
                └─────────┬──────────┘
                          │
                          ▼
                PDF Extraction Service
                          │
                          ▼
                  LangGraph Workflow
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   Metadata Agent    Analyzer Agent   Reviewer Agent
                          │
                          ▼
                 Summarizer Agent
                          │
                          ▼
                  Citation Agent
                          │
                          ▼
                  Insight Agent
                          │
                          ▼
               Fact Checker Agent
                          │
                          ▼
            Hallucination Detection
                          │
                          ▼
               Confidence Scoring
                          │
                          ▼
              Report Generator Agent
                          │
                          ▼
                 Exporter Agent
                          │
                          ▼
        Markdown • JSON • PDF Reports
                          │
                          ▼
                Streamlit Dashboard
```

---

## 🧠 AI Agents

| Agent | Responsibility |
|-------|----------------|
| Metadata Agent | Extract paper metadata |
| Analyzer Agent | Analyze methodology and experiments |
| Reviewer Agent | Score research quality |
| Summarizer Agent | Generate summaries |
| Citation Agent | Extract citations |
| Insight Agent | Generate research insights |
| Fact Checker Agent | Verify claims |
| Hallucination Agent | Detect hallucinations |
| Confidence Agent | Calculate confidence |
| Report Generator | Build final report |
| Exporter Agent | Export Markdown, JSON and PDF |

---
# 🛠️ Tech Stack

### AI & LLM
- LangChain
- LangGraph
- OpenRouter API
- GPT Models

### Backend
- Python 3.12
- Pydantic
- RecursiveCharacterTextSplitter

### Frontend
- Streamlit
- Plotly

### Reports
- Markdown
- JSON
- PDF (ReportLab)

### Other
- Logging
- Environment Variables (.env)
- Git

---

# 📂 Project Structure

```
ResearchMind-AI/
│
├── app/
│   ├── agents/
│   ├── config/
│   ├── graph/
│   ├── models/
│   ├── prompts/
│   ├── services/
│   ├── storage/
│   └── ui/
│       ├── components.py
│       ├── styles.py
│       └── streamlit_app.py
│
├── docs/
├── outputs/
├── sample_input/
├── tests/
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---
# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/<your-username>/ResearchMind-AI.git

cd ResearchMind-AI
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Create a `.env` file.

Example:

```env
OPENROUTER_API_KEY=your_api_key
MODEL_NAME=openai/gpt-4.1-mini
TEMPERATURE=0.2

CHUNK_SIZE=1200
CHUNK_OVERLAP=200
```

---

## 5. Run the Backend

```bash
python main.py
```

---

## 6. Run the Streamlit Dashboard

```bash
streamlit run app/ui/streamlit_app.py
```

---

# 📖 Usage

1. Open the Streamlit application.
2. Upload a research paper (PDF).
3. Click **Analyze Paper**.
4. Wait for the multi-agent workflow to complete.
5. Explore:
   - Metadata
   - Analysis
   - Summary
   - Insights
   - Review
   - Fact Check
   - Hallucination Detection
   - Confidence Dashboard
   - Final Report
   - AI Chat
6. Download the generated Markdown, JSON, or PDF report.

---
# 📸 Screenshots

> Add screenshots after deployment.

Suggested screenshots:

- Dashboard
- Workflow Progress
- Analytics Dashboard
- AI Chat
- Final Report
- Confidence Dashboard

---

# 🔮 Future Enhancements

- Vector Database (ChromaDB / FAISS)
- Advanced RAG Pipeline
- Multi-PDF Comparison
- Research Recommendation Engine
- Research Paper Similarity Search
- Citation Network Visualization
- User Authentication
- Cloud Deployment
- REST API
- Docker Support

---

# 👨‍💻 Author

**Balakrishna Tadela**

Final Year B.Tech (Artificial Intelligence & Machine Learning)

Malla Reddy University

Hyderabad, India

GitHub:
https://github.com/<your-github-username>

LinkedIn:
https://linkedin.com/in/<your-linkedin>

---

# 📄 License

This project is developed for educational and research purposes.

MIT License.

---