from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel,Field

# tavily = TavilyClient()
#
# @tool
# def search(query:str)->str:
#     """Look up real-time information and weather conditions for a given location or query."""
#     print(f'Searching for {query}')
#     return tavily.search(query)
class Source(BaseModel):
    """Schema for source used by the agent"""
    Url:str=Field(description="The Url of the source")
class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer:str=Field(description="The agent answer to the question")
    sources:List[Source]=Field(default_factory=list,description=" a list of The sources that the agent answer")

llm = ChatOpenAI(model="gpt-5")
llm1=ChatOllama(model='gemma4:12b')
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools,response_format=AgentResponse)


def main():
    print("Hello from react-search-agent!")
    result=agent.invoke({'messages':HumanMessage(content='search for 3 job postings for an ai engineer using langchain in Cairo on linkedin and list their details')})
    print(result)


if __name__ == "__main__":
    main()
