#!/usr/bin/python3
""" Web server
"""
from flask import Flask, request
from flask import jsonify
import json
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """ Root
    """
    return "Index"

@app.route("/search_user", methods=['POST'], strict_slashes=False)
def search_user():
    return "nop"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
