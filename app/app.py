from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/login", methods=["GET"])
def login():
    return {"message": "login page v1"}

@app.route("/logout", methods=["GET"])
def logout():
    return {"message": "logout page"}

@app.route("/register", methods=["POST"])
def register():
    return {"message": "register page"}


if __name__ == "__main__":
    app.run(debug=True)
