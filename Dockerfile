FROM python:3.8.3-alpine
WORKDIR /app
COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]
ENTRYPOINT ["python", "-u", "./game/main.py"]

