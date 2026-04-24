from langchain.chains import LLMMathChain
from langchain_openai import OpenAI
from python_a2a.langchain import to_a2a_server
from python_a2a import run_server

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Create a LangChain chain
llm = OpenAI(temperature=0)
math_chain = LLMMathChain(llm=llm)

# Convert to A2A server
a2a_server = to_a2a_server(math_chain)

# Run the server
if __name__ == "__main__":
    run_server(a2a_server, port=5000)