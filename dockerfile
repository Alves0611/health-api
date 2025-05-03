FROM python:3.11-slim

WORKDIR /app

COPY api.py .

RUN pip install flask

EXPOSE 9090

CMD ["python", "api.py"]
