from flask import Flask
import os

app = Flask(__name__)

@app.route('/estudando-argocd')
def estudando_argocd():
    env = os.environ.get("APP_ENV", "undefined")
    debug = os.environ.get("APP_DEBUG", "false")
    password = os.environ.get("DB_PASSWORD", "not_set")
    return f"✔️ ArgoCD ativo!\nEnvironment: {env}\nDebug: {debug}\nDB Password: {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
