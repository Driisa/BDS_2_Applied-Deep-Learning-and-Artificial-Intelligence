from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from config import OPENAI_API_KEY

class SummarizationAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7, openai_api_key=OPENAI_API_KEY)
        self.agent = Agent(
            name="Summarization AI",
            role="Summarizes key points from extracted AI news articles.",
            goal="Generate concise summaries for quick reading.",
            backstory="An AI-powered journalist who condenses lengthy news articles into bite-sized summaries.",
            verbose=True
        )

    def summarize_news(self, articles):
        prompt = "Summarize the following AI news headlines:\n\n" + "\n".join([title for title, url in articles])
        response = self.llm([HumanMessage(content=prompt)])
        return response.content
