# external endpoints
from flask import Flask, render_template

app = Flask(__name__, template_folder='../frontend/templates')


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")
