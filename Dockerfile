FROM python:3.10-slim

WORKDIR /app

# Fix slow pip / build issues
RUN apt-get update && apt-get install -y build-essential curl

COPY requirements.txt .

RUN pip install --default-timeout=1000 --retries=10 --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
