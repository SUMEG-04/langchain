# LANGCHAIN


These scripts showcase the versatility of AI-powered conversational agents and their ability to handle a wide range of user queries and tasks, from answering factual questions to assisting with e-commerce-related inquiries.

---

## 1. Capital of a Place (capital_of_place.py):

This script demonstrates the use of the OpenAI GPT-3.5 Turbo model to answer questions about the capital of a place. It defines a prompt template to ask questions like "What is the capital of {place}?" and utilizes the Langchain library to create an AI chain for generating answers based on user-provided place names.

## 2. E-commerce Product and Store Queries (ecommerce_queries.py):

This script showcases two separate AI chains. The first chain answers questions about the name of an e-commerce store that sells a specific product, while the second chain responds to queries about the names of products available at a given store. It leverages the OpenAI GPT-3.5 Turbo model and Langchain to provide accurate and informative responses.

## 3. Simple Sequential Chain (sequential_chain.py):

This script combines the two previously defined chains (e-commerce product and store queries) into a single sequential chain. It uses Langchain's SimpleSequentialChain to execute both chains in sequence, allowing users to ask questions like "What products are available at {store} that sell {product}?" and receive comprehensive answers.

## 4. Agent for Information Queries (information_agent.py):

This script creates an AI agent for information queries. It uses the OpenAI GPT-3.5 Turbo model and Langchain to answer a wide range of questions. The agent is initialized with tools and can provide information on topics like the age of a celebrity in a specific year. It's designed to handle various information-based queries.

## 5. E-commerce Store and Product Query with Memory (memory_chain.py):

This script focuses on e-commerce queries, specifically identifying the name of an e-commerce store that sells a particular product. It incorporates a memory component using Langchain's ConversationBufferMemory to store and retrieve information related to previous conversations, enhancing the context-awareness of the AI assistant.

