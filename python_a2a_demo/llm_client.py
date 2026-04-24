from python_a2a import A2AClient

# Connect to the OpenAI-based A2A agent
client = A2AClient("http://localhost:5000")

# Print agent metadata
print(f"Connected to: {client.agent_card.name}")
print(f"Description: {client.agent_card.description}")
print("Skills:")
for skill in client.agent_card.skills:
    print(f" - {skill.name}: {skill.description}")

# Send some example questions to test
messages = [
    "In short, why speed of light is constant?",
    "What is the square root of 144?",
]

# Send messages and print responses
for msg in messages:
    response = client.ask(msg)
    print(f"\nUser: {msg}")
    print(f"Agent: {response}")
