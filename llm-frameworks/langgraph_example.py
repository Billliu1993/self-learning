from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

class ReportProcessor:
    def __init__(self, model="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model)
    
    class State(TypedDict):
        report: str
        extracted_values: str 
        formatted_values: str 
        sorted_values: str 
        markdown_table: str
    
    def _extract_values(self, state: State):
        prompt = f"""
        Extract only the numerical values and their associated metrics from the input.
        Format each as 'value: metric' on a new line.
        Example format:
        92: customer satisfaction
        45%: revenue growth
        Input:
        {state['report']}
        """
        msg = self.llm.invoke(prompt)
        return {"extracted_values": msg.content}

    def _format_values(self, state: State):
        prompt = f"""
        Convert all numerical values to percentages where possible.
        If not a percentage or points, convert to decimal (e.g., 92 points -> 92%).
        Keep one number per line.
        Example format:
        92%: customer satisfaction
        45%: revenue growth
        Input:
        {state['extracted_values']}
        """
        msg = self.llm.invoke(prompt)
        return {"formatted_values": msg.content}

    def _sort_values(self, state: State):
        prompt = f"""
        Sort all lines in descending order by numerical value.
        Keep the format 'value: metric' on each line.
        Example:
        92%: customer satisfaction
        87%: employee satisfaction
        Input:
        {state['formatted_values']}
        """
        msg = self.llm.invoke(prompt)
        return {"sorted_values": msg.content}

    def _create_markdown_table(self, state: State):
        prompt = f"""
        Format the sorted data as a markdown table with columns:
        | Metric | Value |
        |:--|--:|
        | Customer Satisfaction | 92% |
        Input:
        {state['sorted_values']}
        """
        msg = self.llm.invoke(prompt)
        return {"markdown_table": msg.content}
    
    def create_workflow(self):
        workflow = StateGraph(self.State)
        
        workflow.add_node("extract_values", self._extract_values)
        workflow.add_node("format_values", self._format_values)
        workflow.add_node("sort_values", self._sort_values)
        workflow.add_node("create_markdown_table", self._create_markdown_table)
        
        workflow.add_edge(START, "extract_values")
        workflow.add_edge("extract_values", "format_values")
        workflow.add_edge("format_values", "sort_values")
        workflow.add_edge("sort_values", "create_markdown_table")
        workflow.add_edge("create_markdown_table", END)
        
        return workflow.compile()