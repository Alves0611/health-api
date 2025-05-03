# app/app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    env = os.environ.get("APP_ENV", "undefined")
    debug = os.environ.get("APP_DEBUG", "false")
    password = os.environ.get("DB_PASSWORD", "not_set")
    return f"""
        <h1>🚀 Hello from poc-python!</h1>
        <p>Environment: {env}</p>
        <p>Debug: {debug}</p>
        <p>DB Password (from secret): {password}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
