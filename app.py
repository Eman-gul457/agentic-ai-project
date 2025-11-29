import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
from tools.weather import get_weather

load_dotenv()

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Query(BaseModel):
    question: str

def ai_agent(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def router(question):
    q = question.lower()

    if "weather" in q or "temperature" in q:
        city = (
            q.replace("weather in", "")
            .replace("weather of", "")
            .replace("temperature in", "")
            .replace("temperature of", "")
            .strip()
        )
        if city == "":
            return "Please provide a city name."
        return get_weather(city)

    return ai_agent(question)


# ----------------------------
# ✅ GET endpoint (browser test)
# http://localhost:8000/ask?question=hi
# ----------------------------
@app.get("/ask")
def ask_ai_get(question: str):
    result = router(question)
    return {"answer": result}


# ----------------------------
# ✅ POST endpoint (API / frontend)
# ----------------------------
@app.post("/ask")
def ask_ai_post(data: Query):
    result = router(data.question)
    return {"answer": result}
