FROM python:3.9-slim

EXPOSE 8000

WORKDIR /app
COPY app.py .

RUN pip install flask

ENV FLASK_APP=app.py

CMD ["python", "app.py"]
