## external imports
import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "Praxisprojekt 2021 !"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
