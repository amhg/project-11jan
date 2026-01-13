from flask import Flask, request

app = Flask(__name__)

SESSION_TIMEOUT_MINUTES = 30

@app.route("/health")
def health():
    return {"status": "ok",
            "service": "auth-api"
            }

@app.route("/login", methods=["GET"])
def login():
    return {"message": "login page",
            "session_timeout": SESSION_TIMEOUT_MINUTES
            }

if __name__ == "__main__":
    app.run(debug=True)
