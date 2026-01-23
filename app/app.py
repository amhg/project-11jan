from flask import Flask

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def info():
    return {
        "service": "health-service",
        "version": VERSION
    }

@app.route("/health")
def health():
    return {
        "status": "ok",
        "uptime": "stable"
        }

if __name__ == "__main__":
    app.run(debug=False)
