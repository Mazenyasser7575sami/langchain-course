from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from langchain_tavily import TavilySearch

# tavily = TavilyClient()
#
# @tool
# def search(query:str)->str:
#     """Look up real-time information and weather conditions for a given location or query."""
#     print(f'Searching for {query}')
#     return tavily.search(query)

llm = ChatOpenAI()
llm1=ChatOllama(model='gemma4:12b')
tools=[TavilySearch()]
agent=create_agent(model=llm1,tools=tools)


def main():
    print("Hello from react-search-agent!")
    result=agent.invoke({'messages':HumanMessage(content='search for 3 job postings for an ai engineer using langchain in Cairo on linkedin and list their details')})
    print(result)


if __name__ == "__main__":
    main()
