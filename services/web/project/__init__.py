from crypt import methods
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def default():
    args = request.args
    return jsonify(hello=str(args))
