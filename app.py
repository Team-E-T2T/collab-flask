from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask App!"
@app.route("/nimsara")
def nimsara():
    return "Hello from Nimsara!"

@app.route("/hello-atheefa")
def hello_atheefa():
    return "Hello from Atheefa!"
@app.route("/hajistha")
def hajistha():
    return "Hello from Hajistha!"

@app.route("/zeenath-hana")
def zeenath_hana():
    return "Hello from Zeenath hana!" 
@app.route("/hello/mahathir")
def hello_mahathir():
    return "Hello from Mahathir"

if __name__ == "__main__":
    app.run(debug=True)

    