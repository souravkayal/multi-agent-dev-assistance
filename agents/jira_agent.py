from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from tools.jira_tools import get_summary_of_pending_tickets
from ollama_llm.llm import get_ollama_llm
from agents.prompts import jira_system_prompt


def get_jira_agent():

    tools = [
        Tool(name="GerSummaryOfPendingTicket", func=get_summary_of_pending_tickets,
             description="Return the summary of pending tickets in JIRA"),
    ]

    llm = get_ollama_llm()

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={"system_message": jira_system_prompt}
    )
