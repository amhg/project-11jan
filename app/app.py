from flask import Flask, request

app = Flask(__name__)

SERVICE_VERSION = "1.0.0"
ENVIRONMENT = "dev"

@app.route("/health")
def health():
    return {"status": "ok",
            "service": "auth-api",
            "version": SERVICE_VERSION,
            "environment": ENVIRONMENT
            }

@app.route("/login", methods=["GET"])
def login():
    return {"message": "login page",
            "auth_type": "basic",
            "environment": ENVIRONMENT
            }

if __name__ == "__main__":
    app.run(debug=True)
