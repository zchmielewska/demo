import pickle
from flask import Flask, render_template

app = Flask(__name__)


with open("./app/data/foos.pkl", "rb") as f:
    FOOS = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html", foos=FOOS)


if __name__ == "__main__":
    app.run(debug=True)
