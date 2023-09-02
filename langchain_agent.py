import openai
import os

from langchain.llms import OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from langchain.agents import AgentType,initialize_agent,load_tools

llm=OpenAI(temperature=.7)
tools=load_tools(["wikipedia","llm-math"],llm=llm)
agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
print(agent.run("How old is Alia Bhatt in 2029?"))
