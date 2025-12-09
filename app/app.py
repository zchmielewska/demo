import os
import pickle
from flask import Flask, render_template

from foo import Foo

app = Flask(__name__)


DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "foos.pkl")
with open(DATA_PATH, "rb") as f:
    FOOS = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html", foos=FOOS[1:10])


if __name__ == "__main__":
    app.run(debug=True)
