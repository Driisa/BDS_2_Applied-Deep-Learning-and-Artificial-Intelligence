from crewai import Task, Crew
from agents.news_extractor_agent import NewsExtractionAgent
from agents.summarizer_agent import SummarizationAgent
from agents.sentiment_agent import SentimentAnalysisAgent

# Initialize AI agents
news_extractor = NewsExtractionAgent()
summarizer = SummarizationAgent()
sentiment_analyzer = SentimentAnalysisAgent()

# Define tasks
news_task = Task(
    description="Extract latest AI news articles and headlines.",
    agent=news_extractor.agent,
    expected_output="A list of latest AI-related news headlines."
)

summary_task = Task(
    description="Summarize the news headlines into key insights.",
    agent=summarizer.agent,
    expected_output="A well-written summary of AI news articles."
)

sentiment_task = Task(
    description="Analyze the overall sentiment of summarized AI news.",
    agent=sentiment_analyzer.agent,
    expected_output="A sentiment classification (Positive, Negative, or Neutral)."
)

# Create Crew
crew = Crew(
    agents=[news_extractor.agent, summarizer.agent, sentiment_analyzer.agent],
    tasks=[news_task, summary_task, sentiment_task]
)

def run_workflow(query="AI news", num_articles=5):
    articles = news_extractor.fetch_news(query, num_articles)
    summary = summarizer.summarize_news(articles)
    sentiment = sentiment_analyzer.analyze_sentiment(summary)

    return {"headlines": articles, "summary": summary, "sentiment": sentiment}

if __name__ == "__main__":
    result = run_workflow()
    
    print("\n📰 Extracted News Headlines:")
    for title, url in result["headlines"]:
        print(f"- {title} ({url})")
    
    print("\n📄 Summary:")
    print(result["summary"])

    print("\n📊 Sentiment Analysis:")
    print(result["sentiment"])
