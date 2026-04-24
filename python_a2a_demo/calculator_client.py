from python_a2a import A2AClient

# Connect to the running CalculatorAgent server
client = A2AClient("http://localhost:5000")

# Print agent metadata
print(f"Connected to: {client.agent_card.name}")
print(f"Description: {client.agent_card.description}")
print("Skills:")
for skill in client.agent_card.skills:
    print(f" - {skill.name}: {skill.description}")

# Interact with the agent
messages = [
    "Hello there! My name is Alice.",
    "What can you do?",
    "Can you add 10 and 5?",
    "What is 20 divided by 4?",
    "Multiply 7 and 8.",
    "Please subtract 100 from 250.",
    "Divide 9 by 0."  # test divide-by-zero case
]

# Send messages and print responses
for msg in messages:
    response = client.ask(msg)
    print(f"\nUser: {msg}")
    print(f"Agent: {response}")