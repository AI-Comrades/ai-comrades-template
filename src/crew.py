from crewai import Crew
from src.agents import Agents
from src.tasks import Tasks
from dotenv import load_dotenv


load_dotenv()

class AIComradesCrew():
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = Agents()
        tasks = Tasks()

        # Define your custom agents and tasks here
        agent = agents.example_agent()

        # Custom tasks include agent name and variables as input
        task = tasks.example_task(agent)

        # Define your custom crew here
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True,
        )

        result = crew.kickoff()
        return result