from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from agents.email_agent import get_email_agent
from agents.jira_agent import get_jira_agent
from ollama_llm.llm import get_ollama_llm
from agents.prompts import main_system_prompt


def get_main_agent():
    email_agent = get_email_agent()
    jira_agent = get_jira_agent()

    tools = [
        Tool(name="EmailAgent", func=email_agent.run,
             description="Delegate to email agent"),

        Tool(name="EventAgent", func=jira_agent.run,
             description="Delegate to JIRA agent"),
    ]

    llm = get_ollama_llm()

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={"system_message": main_system_prompt}
    )
