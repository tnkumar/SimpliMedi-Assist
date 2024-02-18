from flask import jsonify, request
from app import app
from .helpers import some_helper_function

@app.route('/')
def index():
    response_data = {
        "message": "Welcome to SimpliMedi-Assist!"
    }
    return jsonify(response=response_data), 200


@app.app_errorhandler(404)
def not_found(e):
    return jsonify(error=404, text=str(e)), 404