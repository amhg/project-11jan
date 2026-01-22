from flask import Flask

app = Flask(__name__)

@app.route("/")
def info():
    return {
        "app": "health-service",
        "version": "dev"
    }


@app.route("/health")
def health():
    return {
        "status": "ok",
        "version": "1.0"
        }

if __name__ == "__main__":
    app.run(debug=True)
