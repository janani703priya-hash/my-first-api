from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! My first API is live. Version 2."

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)