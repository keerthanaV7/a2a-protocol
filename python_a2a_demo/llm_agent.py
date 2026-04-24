from python_a2a import OpenAIA2AServer, run_server

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Create an OpenAI-based A2A agent
agent = OpenAIA2AServer(
    api_key=api_key,
    model="gpt-4",
    system_prompt="You are a helpful assistant that specializes in explaining complex concepts simply."
)

# Run the server
if __name__ == "__main__":
    print("Starting OpenAI-based A2A agent...")
    run_server(agent, host="0.0.0.0", port=5000)