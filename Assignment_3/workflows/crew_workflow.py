from crewai import Task, Crew
from agents.news_extractor_agent import NewsExtractionAgent
from agents.summarizer_agent import SummarizationAgent
from agents.sentiment_agent import SentimentAnalysisAgent
from agents.quality_classification_agent import ClassificationAgent

def run_workflow(query="AI news", num_articles=10):
    # Initialize AI agents
    news_extractor = NewsExtractionAgent()
    summarizer = SummarizationAgent()
    sentiment_analyzer = SentimentAnalysisAgent()
    classification = ClassificationAgent()

    # Extract initial articles
    articles = news_extractor.fetch_news(query, num_articles)
    
    # Filter relevant articles
    relevant_articles = []
    for article in articles:
        title, url = article
        is_relevant = classification.classify_relevance(title, query)
        if is_relevant:
            relevant_articles.append(article)
    
    # Only proceed with relevant articles
    if relevant_articles:
        summary = summarizer.summarize_news(relevant_articles)
        sentiment = sentiment_analyzer.analyze_sentiment(summary)
    else:
        summary = "No relevant articles found."
        sentiment = "N/A"

    return {
        "headlines": relevant_articles,
        "summary": summary,
        "sentiment": sentiment
    }

# Define tasks
def create_crew():
    # Initialize AI agents
    news_extractor = NewsExtractionAgent()
    summarizer = SummarizationAgent()
    sentiment_analyzer = SentimentAnalysisAgent()
    classification = ClassificationAgent()

    news_task = Task(
        description="Extract latest AI news articles and headlines.",
        agent=news_extractor.agent,
        expected_output="A list of latest AI-related news headlines."
    )

    classification_task = Task(
        description="Classify the relevance of news headlines.",
        agent=classification.agent,
        expected_output="Classification of article relevance."
    )

    summary_task = Task(
        description="Summarize the relevant news headlines into key insights.",
        agent=summarizer.agent,
        expected_output="A well-written summary of relevant AI news articles."
    )

    sentiment_task = Task(
        description="Analyze the overall sentiment of summarized AI news.",
        agent=sentiment_analyzer.agent,
        expected_output="A sentiment classification (Positive, Negative, or Neutral)."
    )

    # Create Crew
    crew = Crew(
        agents=[news_extractor.agent, classification.agent, summarizer.agent, sentiment_analyzer.agent],
        tasks=[news_task, classification_task, summary_task, sentiment_task]
    )
    
    return crew

if __name__ == "__main__":
    result = run_workflow()
    
    print("\n📰 Relevant News Headlines:")
    if result["headlines"]:
        for title, url in result["headlines"]:
            print(f"- {title} ({url})")
    else:
        print("No relevant headlines found.")
    
    print("\n📄 Summary:")
    print(result["summary"])

    print("\n📊 Sentiment Analysis:")
    print(result["sentiment"])