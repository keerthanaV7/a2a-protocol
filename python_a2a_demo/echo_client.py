from python_a2a import A2AClient, Message, TextContent, MessageRole

# Create a client to talk to our agent
client = A2AClient("http://localhost:5000/a2a")

# Send a message using Python A2A
message = Message(
    content=TextContent(text="Hello, Good morning!"),
    role=MessageRole.USER
)
response = client.send_message(message)

# Print the response from our agent
print(f"Agent says: {response.content.text}")