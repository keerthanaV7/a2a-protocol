import subprocess
import time
import sys

def main():
    print("Hello from travel-planner!")

    # Scripts to launch before the Streamlit app
    scripts = ["WeatherAgent.py", "TavilySearchAgent.py", "LocalLLMAgent.py"]
    streamlit_app = "TravelPlannerApp.py"

    processes = []

    # Launch agent scripts
    for script in scripts:
        print(f"Launching {script}...")
        p = subprocess.Popen([sys.executable, script])
        processes.append(p)
        print(f"{script} started. Waiting 2 seconds before next...\n")
        time.sleep(2)

    # Launch Streamlit app
    print(f"Launching Streamlit app: {streamlit_app}...")
    p = subprocess.Popen(["streamlit", "run", streamlit_app])
    processes.append(p)

    # Keep the main process alive
    try:
        print("All agents (and UI) are running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down all agents...")
        for p in processes:
            p.terminate()
        print("All agents stopped.")

if __name__ == "__main__":
    main()
