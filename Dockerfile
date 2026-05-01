FROM python:3.11.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t myapp .
# docker run -p 8000:8000 myapp
# 브라우저에서 http://localhost:8000/docs