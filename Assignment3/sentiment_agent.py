from crewai import Agent
from textblob import TextBlob

class SentimentAnalysisAgent:
    def __init__(self):
        self.agent = Agent(
            name="Sentiment Analyzer",
            role="Analyzes sentiment trends in summarized AI news.",
            goal="Detect whether news is mostly positive, neutral, or negative.",
            backstory="An AI analyst trained to detect sentiment in news articles, providing insights on how the media perceives AI trends.",
            verbose=True
        )

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # Range: -1 to 1

        if polarity > 0.2:
            return "😊 Positive"
        elif polarity < -0.2:
            return "😠 Negative"
        else:
            return "😐 Neutral"
