from python_a2a import A2AServer, skill, agent, run_server
from python_a2a import TaskStatus, TaskState

@agent(
    name="Greeting Agent",
    description="A simple agent that responds to greetings",
    version="1.0.0"
)
class GreetingAgent(A2AServer):

    @skill(
        name="Greet",
        description="Respond to a greeting",
        tags=["greeting", "hello"]
    )
    def greet(self, name=None):
        if name:
            return f"Hello, {name}! How can I help you today?"
        else:
            return "Hello there! How can I help you today?"

    def handle_task(self, task):
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""

        greeting_words = ["hello", "hi", "hey", "greetings"]
        is_greeting = any(word in text.lower() for word in greeting_words)

        if is_greeting:
            name = None
            if "my name is" in text.lower():
                name = text.lower().split("my name is")[1].strip()

            greeting = self.greet(name)
            task.artifacts = [{
                "parts": [{"type": "text", "text": greeting}]
            }]
            task.status = TaskStatus(state=TaskState.COMPLETED)
        else:
            task.artifacts = [{
                "parts": [{"type": "text", "text": "I'm a greeting agent. Try saying hello!"}]
            }]
            task.status = TaskStatus(state=TaskState.COMPLETED)

        return task

# Run the server
if __name__ == "__main__":
    agent = GreetingAgent()
    run_server(agent, port=5000)