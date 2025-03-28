import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


@CrewBase
class ReportFormattingCrew:
    """ReportFormattingCrew for processing and formatting report data"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,  # Lower temperature for more consistent outputs
        )
        super().__init__()

    @agent
    def report_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config["report_formatter"], 
            verbose=True, 
            llm=self.llm
        )

    @task
    def extract_numerical_values_task(self) -> Task:
        return Task(
            config=self.tasks_config["extract_numerical_values_task"],
        )

    @task
    def convert_to_percentages_task(self) -> Task:
        return Task(config=self.tasks_config["convert_to_percentages_task"])

    @task
    def sort_values_task(self) -> Task:
        return Task(config=self.tasks_config["sort_values_task"])

    @task
    def format_as_markdown_table_task(self) -> Task:
        return Task(config=self.tasks_config["format_as_markdown_table_task"])


    @crew
    def crew(self) -> Crew:
        """Creates the ReportFormattingCrew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
