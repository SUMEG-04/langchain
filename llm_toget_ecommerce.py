import openai
import os 
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')


prompt=PromptTemplate.from_template("What is the name of e-commerce stotre that sells {product}?")
llm=OpenAI(temperature=0.3)
chain1=LLMChain(llm=llm,prompt=prompt)
# product='Boat'
#output=chain.run(product)
# print(output)


prompt=PromptTemplate.from_template("What is the name of products at {store}?")
llm=OpenAI(temperature=0.3)
chain2=LLMChain(llm=llm,prompt=prompt)
# store='Amazon'
# output=chain.run(store)
# print(output)

# This is the overall chain where we run these two chains in sequence.

chain = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

chain.run("speaker")