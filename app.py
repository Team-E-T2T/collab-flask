from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the common app!"

@app.route("/suchinthana")
def suchinthana():
    return "Hello from Suchinthana!"

if __name__ == "__main__":
    app.run(debug=True)