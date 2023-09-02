from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

prompt=PromptTemplate.from_template("What is the name of e-commerce stotre that sells {product}?")
llm=OpenAI(temperature=0.3)
chain1=LLMChain(llm=llm,prompt=prompt,memory=ConversationBufferMemory())
print(chain1.run("fruits"))