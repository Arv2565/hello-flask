from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello-armada"

@app.route("/healthz")
def health():
    return "healthz is working", 200

@app.route("/settings")
def settings():
    return "this shows the settings of the application", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
