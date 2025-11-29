import os
from dotenv import load_dotenv
from groq import Groq
from tools.weather import get_weather

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Agentic AI — Local Smart Agent (Groq Powered)")
print("Ask anything! Type 'quit' to exit.\n")

def ai_agent(prompt):
    """AI model response using Groq."""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",  # Your working model
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def route_to_tools(user_input):
    """Detect if user wants weather information."""
    text = user_input.lower()

    if "weather" in text or "temperature" in text:
        # Tool: extract city
        city = (
            text.replace("weather in", "")
            .replace("weather of", "")
            .replace("temperature in", "")
            .replace("temperature of", "")
            .strip()
        )

        if city == "" or city == "weather" or city == "temperature":
            return "Please specify a city name."

        return get_weather(city)

    # If no tool is needed → send to AI model
    return ai_agent(user_input)


# Main Loop
while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["quit", "exit"]:
        print("Agent: Goodbye!")
        break

    response = route_to_tools(user_input)
    print(f"Agent: {response}\n")
