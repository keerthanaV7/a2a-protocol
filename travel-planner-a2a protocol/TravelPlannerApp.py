import streamlit as st
from python_a2a import AgentNetwork, A2AClient
import asyncio

# Function to run async logic inside Streamlit
def run_async(coro):
    return asyncio.run(coro)

async def plan_trip(destination, travel_dates):
    # Create an agent network
    network = AgentNetwork(name="Travel Assistant Network")
    network.add("weather", "http://localhost:8001")
    network.add("search", "http://localhost:8002")

    # Get agents
    weather_agent = network.get_agent("weather")
    search_agent = network.get_agent("search")
    llm_client = A2AClient("http://localhost:5001")

    # Get weather forecast
    forecast = weather_agent.ask(f"What's the weather in {destination}?")

    # Search based on weather
    if "sunny" in forecast.lower() or "clear" in forecast.lower():
        activities = search_agent.ask(f"Recommend outdoor activities in {destination}")
    else:
        activities = search_agent.ask(f"Recommend indoor activities in {destination}")

    # Summarize using LLM
    prompt = (
        f"You are a travel assistant. Based on the weather forecast result '{forecast}' "
        f"and the recommendations [{activities}], suggest me a few must-see attractions "
        f"on date {travel_dates}."
    )

    llm_result = llm_client.ask(prompt)

    return forecast, activities, llm_result

# Streamlit UI
st.set_page_config(page_title="🧳 Travel Planner Assistant")

st.title("🧭 Travel Planner Assistant")
st.write("Get personalized trip suggestions based on real-time weather and recommendations.")

destination = st.text_input("Enter destination", value="Kerala, India")
travel_dates = st.text_input("Enter travel dates", value="August 1-5")

if st.button("Plan My Trip"):
    with st.spinner("Planning your trip..."):
        try:
            forecast, activities, llm_result = run_async(plan_trip(destination, travel_dates))

            st.subheader("📍 Weather Forecast")
            st.success(forecast)

            st.subheader("🎯 Recommended Activities")
            st.info(activities)

            st.subheader("🗺️ Suggested Travel Plan")
            st.markdown(llm_result)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
