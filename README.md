# 🎥 YouTube AI Assistant

An AI-powered YouTube Video Summarizer and Chat Assistant built using Streamlit, Gemini, Retrieval-Augmented Generation (RAG), FAISS, and Sentence Transformers.

The application allows users to:

✅ Generate AI-powered summaries of YouTube videos

✅ Ask questions about video content

✅ Chat with videos using Retrieval-Augmented Generation (RAG)

✅ Retrieve context-aware answers grounded in video transcripts

---

## 🚀 Features

### 📄 AI Video Summarization

- Extracts YouTube transcripts
- Cleans transcript content
- Generates structured summaries using Gemini
- Produces:
  - Executive Summary
  - Key Takeaways
  - Main Topics
  - Important Insights

---

### 💬 Chat With Video

Ask questions such as:

```text
What annual hike percentage is discussed?

Why do people feel stuck in their careers?

What is the 3.6 crore salary example?
```

The system:

```text
Question
    ↓
Semantic Retrieval
    ↓
Relevant Transcript Chunks
    ↓
Gemini
    ↓
Grounded Answer
```

---

## 🏗️ Architecture

```text
YouTube URL
      ↓
Transcript Extraction
      ↓
Transcript Cleaning
      ↓
Chunking
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
Semantic Retrieval
      ↓
Gemini QA
      ↓
Answer
```

---

## 🧠 Tech Stack

### Frontend

- Streamlit

### LLM

- Gemini 2.5 Flash

### RAG Components

- Sentence Transformers
- FAISS
- Semantic Search

### Transcript Extraction

- youtube-transcript-api

### Language

- Python

---

## 📂 Project Structure

```text
gen_ai_vid_summarizer/
│
├── app.py
├── transcript.py
├── summarizer.py
│
├── rag/
│   ├── __init__.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── qa.py
│   └── pipeline.py
│
├── tests/
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_pipeline.py
│   └── test_rag_pipeline.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Shreyascr5/gen_ai_vid_summarizer.git

cd gen_ai_vid_summarizer
```

---

### Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your Gemini API key from:

https://aistudio.google.com/

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 🧪 Running Tests

### Chunking Test

```bash
python -m tests.test_chunking
```

### Embedding Test

```bash
python -m tests.test_embeddings
```

### Full Pipeline Test

```bash
python -m tests.test_pipeline
```

### RAG Pipeline Test

```bash
python -m tests.test_rag_pipeline
```

---

## 🔍 Example Workflow

### Step 1

Paste YouTube URL

```text
https://youtu.be/VIDEO_ID
```

### Step 2

Process Video

The system:

- Extracts transcript
- Builds vector database
- Generates summary

### Step 3

Ask Questions

Example:

```text
What annual hike percentage is discussed?
```

Answer:

```text
The annual hike percentage discussed is 12%.
```

---

## 📈 Future Improvements

- Multi-video chat
- Conversation memory
- Citation-aware responses
- Video thumbnail integration
- Summary export (PDF/DOCX)
- Deploy on Streamlit Cloud
- LangChain integration
- Hybrid retrieval and reranking

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shreyas C R**
**Sanjay S**

GitHub:

https://github.com/Shreyascr5

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others
