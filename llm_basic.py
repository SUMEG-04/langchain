import openai
import os

from langchain.llms import OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate.from_template("What is the capital of {place}?")
llm=OpenAI(temperature=0.3)

chain=LLMChain(llm=llm,prompt=prompt)

output=chain.run("Gujrat")
print(output)