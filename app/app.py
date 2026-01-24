from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/login", methods=["GET"])
def login():
    return {"message": "login page message"}

@app.route("/status")
def status():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(debug=True)
