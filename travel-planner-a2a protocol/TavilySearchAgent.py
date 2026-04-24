from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
from tavily import TavilyClient
import os
import logging

from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("TAVILY_API_KEY")

@agent(
    name="Tavily Search Agent",
    description="Performs internet search using Tavily API",
    version="1.0.0",
    url="https://yourdomain.com"
)
class TavilySearchAgent(A2AServer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = TavilyClient(api_key)

    @skill(
        name="Search Internet",
        description="Perform a web search using Tavily API",
        tags=["search", "internet", "tavily"],
        examples="Search 'must visit places in utah in may'"
    )
    def search(self, query: str):
        """Perform search using Tavily Search API"""
        try:
            response = self.client.search(query=query)

            results = response.get("results", [])
            if not results:
                return "No search results found."

            summary = "\n".join(
                [f"- {r.get('title')}: {r.get('url')}" for r in results]
            )
            return f"Top results for '{query}':\n{summary}"

        except Exception as e:
            logging.error(f"Error during Tavily search: {e}")
            return f"Search failed: {e}"

    def handle_task(self, task):
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""

        if text.strip():
            query = text.strip()
            result = self.search(query)
            task.artifacts = [{
                "parts": [{"type": "text", "text": result}]
            }]
            task.status = TaskStatus(state=TaskState.COMPLETED)
        else:
            task.status = TaskStatus(
                state=TaskState.INPUT_REQUIRED,
                message={"role": "agent", "content": {"type": "text", 
                         "text": "Please provide a search query."}}
            )
        return task


if __name__ == "__main__":
    agent = TavilySearchAgent(google_a2a_compatible=True)
    run_server(agent, port=8002, debug=True)
