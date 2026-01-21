from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok",
            "service": "auth-api"
            }

@app.route("/login", methods=["GET"])
def login():
    return {"message": "login page"}

@app.route("/register", methods=["POST"])
def register():
    return {"message": "register page"}

@app.route("/profile", methods=["GET"])
def profile():
    print("DEBUG: profile accessed")  # should be removed in production
    return {"message": "profile page"}


if __name__ == "__main__":
    app.run(debug=True)
