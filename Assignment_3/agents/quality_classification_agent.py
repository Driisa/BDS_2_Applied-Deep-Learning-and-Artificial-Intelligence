from crewai import Agent, Task, Crew

class ClassificationAgent:
    def __init__(self):
        self.agent = Agent(
            name="News Classification",
            role="Rate the quality of the articles and their relevance to the specified topic.",
            goal="Distinguish between relevant (returning True) and irrelevant news (returning False).",
            backstory="A digital news curator dedicated to fetching the most relevant and up-to-date news articles.",
            verbose=True
        )

    def classify_relevance(self, content: str, topic: str) -> bool:
        """
        Assess if the provided content is relevant to the specified topic.

        Args:
            content (str): The content to evaluate
            topic (str): The topic to assess relevance against

        Returns:
            bool: True if the content is relevant to the topic, False otherwise
        """
        task_description = f"""
        Determine if the following content is relevant to the topic '{topic}':
        
        {content}

        Respond with ONLY 'True' or 'False'.
        """

        task = Task(
            description=task_description,
            expected_output="A single word: 'True' or 'False', indicating whether the content is relevant to the topic.",
            agent=self.agent
        )

        # Create a Crew and add the task
        crew = Crew(agents=[self.agent], tasks=[task])

        # Execute the Crew and get the response
        crew_output = crew.kickoff()

        # If the response is a dictionary, extract the output
        if isinstance(crew_output, dict):
            response_text = crew_output.get("output", "").strip()
        else:
            response_text = str(crew_output).strip()  # Convert to string and clean up

        return response_text.lower() == 'true'
