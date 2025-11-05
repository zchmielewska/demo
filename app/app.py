import pickle
from flask import Flask, render_template

from foo import Foo

app = Flask(__name__)


with open("./app/data/foos.pkl", "rb") as f:
    FOOS = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html", foos=FOOS[1:10])


if __name__ == "__main__":
    app.run(debug=True)
