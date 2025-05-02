from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from tools.email_tool import get_unread_email_summary, get_high_priority_email
from ollama_llm.llm import get_ollama_llm
from agents.prompts import email_system_prompt


def get_email_agent():

    tools = [
        Tool(name="GetUnreadEmailSummary", func=get_unread_email_summary,
             description="Give detail of unread emails in the inbox"),

        Tool(name="GetHighPriorityEmail", func=get_high_priority_email,
             description="Return the detail of high priority email in the inbox"),
    ]

    llm = get_ollama_llm()

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={"system_message": email_system_prompt}
    )
