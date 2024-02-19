from flask import jsonify, request
from app import app
from .helpers import create_index

@app.route('/', methods=['POST'])
def index():
    if request.method != 'POST':
        # Method not allowed
        return jsonify(error="Method not allowed"), 405

    # Get the text data from the request
    data = request.data.decode('utf-8')

    # Prepare the response data
    response_data = {
        "message": "Welcome to SimpliMedi-Assist!",
    }

    # Return the response
    return jsonify(status=200, response=response_data), 200

@app.route('/build-index', methods=['GET'])
def build_index():
    if request.method != 'GET':
        # Method not allowed
        return jsonify(error="Method not allowed"), 405

    create_index()

    # Prepare the response data
    response_data = {
        "message": "Vector DB set up successfully!",
    }

    # Return the response
    return jsonify(status=200, response=response_data), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify(error=404, text=str(e)), 404