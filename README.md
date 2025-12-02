🚀 Agentic-AI — Smart AI Agent (Groq-Powered) with Weather & Time Tools
---
This project implements a local intelligent AI agent built using:
---
FastAPI
Groq LLM (gpt-oss-20b)
Custom tools (Weather + Time)
Local CLI agent + API agent
Dockerized deployment
It supports:
🌦 Real-time Weather
🕒 Time-zone calculation
🤖 Conversational AI
🔧 Extendable Tools system
The app works locally or inside Docker and exposes REST APIs.

---
🧰 Tech Stack
---
# 🚀 Agentic-AI — Smart AI Agent (Groq-Powered)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white)](#)
[![Groq](https://img.shields.io/badge/Groq-LLM-EA580C?logo=googlecloud&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](#)
[![WeatherAPI](https://img.shields.io/badge/WeatherAPI-Enabled-1E90FF?logo=cloudflare&logoColor=white)](#)
[![CI/CD](https://img.shields.io/badge/Jenkins-Ready-D24939?logo=jenkins&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)

A smart agent built with FastAPI, Groq LLM, Docker, Weather API, and extendable tool systems.

---
📦 Project Structure
---
```bash
agentic-ai-project/
│── agent.py
│── app.py
│── tools/
│     ├── weather.py
│     └── time_tool.py
│── Dockerfile
│── requirements.txt
│── README.md
│── screenshots/
```
---
🔑 API Keys Setup
---
⭐ Groq API Key
---
```bash
export GROQ_API_KEY="your-groq-key"
```
⭐ Weather API Key
---
```bash
---export WEATHER_API_KEY="your-weather-api-key"
```
---
If using .env:
```bash
GROQ_API_KEY=xxxx
WEATHER_API_KEY=xxxx
```
---
▶️ Run Locally (No Docker)
---
Install dependencies:
---
```bash
pip install -r requirements.txt
```
---
Run FastAPI:
---
```bash
---uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
---
Run agent:
---
```bash
python3 agent.py
```
<img width="1323" height="497" alt="AI Agent Response Inside Container" src="https://github.com/user-attachments/assets/702df67e-dfa3-4504-a0f4-bc7dabd07f1b" />

---
🐳 Run Using Docker (Step-by-Step)
---
1️⃣ Build Docker Image
---
```bash
docker build -t agentic-ai-app .
```
<img width="1333" height="377" alt="docker-build" src="https://github.com/user-attachments/assets/7ec89cba-3a09-4c32-8701-5a0aa9bb318a" />

---
2️⃣ Run Container
---
```bash
docker run -d \
  -p 8000:8000 \
  -e GROQ_API_KEY=your-key \
  -e WEATHER_API_KEY=your-key \
  --name agentic-ai-container \
  agentic-ai-app
```
<img width="1356" height="150" alt="docker-run" src="https://github.com/user-attachments/assets/1dfa1d60-e392-437e-b6af-c29c44e494ef" />

---
3️⃣ Check Container Status
---
```bash
docker ps
```
---
4️⃣ Test API in Browser
---
```bash
http://localhost:8000/docs
```
<img width="1214" height="512" alt="fastapi-running" src="https://github.com/user-attachments/assets/c998d321-3584-4c50-a5c5-8446b590ad8a" />

---
🧠 How the Agent Works
---
1.User asks a question
2.Groq LLM interprets intent
3.If question needs tools →
4.Weather tool calls WeatherAPI
5.Time tool calculates UTC+offset
6.AI returns final merged response

---
🔧 DevOps Responsibilities in This Project
---
This is what YOUR DevOps work include:

✔ Containerization
---
You created Dockerfile & containerized the entire app.

✔ Environment Management
---
API keys handled via env variables securely.

✔ CI/CD Ready (Jenkins)
---
Repository structured for pipelines:
---
•Automated Docker builds
•Automated deployment
•Testing stages
•Push to registry

<img width="1341" height="471" alt="jenkins-console" src="https://github.com/user-attachments/assets/56a243cc-ef0c-4632-850f-7bdee06926fb" />

---
🏁 Conclusion
---
This project demonstrates:
---
✨ AI engineering
✨ FastAPI backend development
✨ Tool-based reasoning system
✨ Dockerization
✨ DevOps CI/CD readiness
✨ API-driven microservice architecture

