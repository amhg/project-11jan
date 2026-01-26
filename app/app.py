from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/login", methods=["GET"])
def login():
    return {"message": "login v2"}

@app.route("/logout", methods=["POST"])
def logout():
    return {"message": "logged out"}

if __name__ == "__main__":
    app.run(debug=True)
