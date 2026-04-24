from python_a2a import run_server
from python_a2a.langchain import to_a2a_server
from langchain_ollama.llms import OllamaLLM

# Create a LangChain LLM
#llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm = OllamaLLM(model="llama3.2:latest")

# Convert LLM to A2A server
llm_server = to_a2a_server(llm)

if __name__ == "__main__":
    print("Starting LLM A2A server on port 5001...")
    run_server(llm_server, port=5001)
