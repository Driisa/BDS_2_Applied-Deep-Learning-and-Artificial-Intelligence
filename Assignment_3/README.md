# AI News Extractor

## 📌 Overview
AI News Extractor is a Python-based project that utilizes **CrewAI** to extract, analyze, and summarize news articles. It employs multiple AI agents to perform tasks such as data extraction, sentiment analysis, and summarization.

## 🚀 Features
- **News Extraction:** Fetches news articles using APIs.
- **Sentiment Analysis:** Analyzes the sentiment of extracted articles.
- **Summarization:** Condenses news content into key points.
- **CrewAI Integration:** Implements AI agents for modular workflow.
- **Streamlit UI:** Provides an interactive web-based UI.

## 📂 Project Structure
```
ASSIGNMENT_3_AI_NEWS_EXTRACTOR/
│── agents/
│   ├── news_extractor_agent.py
│   ├── sentiment_agent.py
│   ├── summarizer_agent.py
│
│── workflows/
│   ├── crew_workflow.py
│
│── app.py
│── config.py
│── Dockerfile
│── README.md
│── requirements.txt
```

## ⚙️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Driisa/BDS_2_Applied-Deep-Learning-and-Artificial-Intelligence.git
cd BDS_2_Applied-Deep-Learning-and-Artificial-Intelligence/Assignment_3_AI_News_Extractor
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install --no-cache-dir -r requirements.txt
```

## 🏃 Running the Project
```bash
streamlit run app.py
```

## 🐳 Running with Docker
```bash
docker build -t ai-news-extractor .
docker run -p 8501:8501 ai-news-extractor
```

## 🔧 Configuration
Modify `config.py` to adjust API keys, model settings, and other parameters.

## 🎯 Future Improvements
- Add more AI agents for deeper analysis.
- Improve UI with visualization features.
- Implement multilingual support.

---

### ✨ Contributing
Feel free to fork this repository and submit pull requests!

### 📜 License
This project is licensed under the MIT License.

### 📬 Contact
For questions or feedback, reach out via GitHub Issues.

🚀 Happy Coding!
