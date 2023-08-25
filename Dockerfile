FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . .

RUN chmod +x main.py

ENTRYPOINT ["python", "main.py"]
