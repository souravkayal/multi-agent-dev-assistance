from langchain_community.llms import Ollama


def get_ollama_llm():
    return Ollama(model="mistral:latest")
