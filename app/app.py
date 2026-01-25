from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "healthy new"}

@app.route("/login", methods=["GET"])
def login():
    return {"message": "Login endpoint updated"}

@app.route("/status")
def status():
    return {"status": "running"}

@app.route("/register")
def status():
    return {"message": "register page"}

if __name__ == "__main__":
    app.run(debug=True)
