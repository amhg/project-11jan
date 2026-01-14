from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok",
            "service": "auth-api",
            "version": "1.0.0"
            }

@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username", "guest")
    return {
        "message": "login page",
        "user": username,
        "service": "auth-api"
        }

if __name__ == "__main__":
    app.run(debug=True)
