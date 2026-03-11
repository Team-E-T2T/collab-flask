from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the common app!"

@app.route("/nimsara")
def nimsara():
    return "Hello from Nimsara!"

if __name__ == "__main__":
    app.run(debug=True)

    