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
    return {"message": "profile page"}

@app.route("/logout", methods=["POST"])
def logout():
    return {"message": "logout page"}

@app.route("/admin", methods=["GET"])
def admin():
    return {"message": "admin page"}

@app.route("/debug", methods=["GET"])
def debug():
    return {"message": "debug info"}


if __name__ == "__main__":
    app.run(debug=True)
