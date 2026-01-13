from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok",
            "service": "auth-api"
            }

@app.route("/login", methods=["GET"])
def login():
    return {"message": "login page",
            "auth_type": "basic"
            }

if __name__ == "__main__":
    app.run(debug=True)
