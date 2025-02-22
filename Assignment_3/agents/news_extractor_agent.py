from crewai import Agent
import requests
from config import NEWS_API_KEY

class NewsExtractionAgent:
    def __init__(self):
        self.agent = Agent(
            name="News Extractor",
            role="Fetches AI news articles from the web and provides raw headlines.",
            goal="Retrieve the latest AI news from reliable sources.",
            backstory="A digital news curator working tirelessly to fetch the most relevant and up-to-date AI news articles.",
            verbose=True
        )

    def fetch_news(self, query="AI technology", num_articles=5):
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize={num_articles}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if "articles" in data:
            articles = [(article["title"], article["url"]) for article in data["articles"]]
            return articles
        else:
            return ["No articles found."]
