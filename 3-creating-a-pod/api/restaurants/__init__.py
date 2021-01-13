from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/locations')
def locations():
    return jsonify([{'id': 1, 'name': 'chipotle'}, {'id': 2, 'name': 'famiglia'}])
