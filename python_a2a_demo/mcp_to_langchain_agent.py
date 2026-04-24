from python_a2a.mcp import FastMCP
from python_a2a.langchain import to_langchain_tool
from python_a2a import run_server
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI

# Create an MCP server with tools
calculator = FastMCP(name="Calculator MCP")

@calculator.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@calculator.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

# Run the MCP server in a background thread
import threading
server_thread = threading.Thread(
    target=run_server,
    args=(calculator,),
    kwargs={"port": 8000},
    daemon=True
)
server_thread.start()

# Convert MCP tools to LangChain tools
add_tool = to_langchain_tool("http://localhost:8000", "add")
subtract_tool = to_langchain_tool("http://localhost:8000", "subtract")

# Use in a LangChain agent
llm = OpenAI(temperature=0)
tools = [add_tool, subtract_tool]

agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
result = agent.run("Add 15 and 27, then subtract 5 from the result")
print(result)