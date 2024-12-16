#with flask

from flask import Flask, jsonify, Response

app = Flask(__name__)

# Endpoint: Hello World
@app.route('/')
def hello_world():
    return "Hello, World!"

# Endpoint: Error with proper JSON response
@app.route('/error')
def trigger_error():
    # Construct a response object with JSON error message
    response = jsonify({"error": "Bad Request"})
    response.status_code = 400  # HTTP 400 status for a bad request
    return response

if __name__ == '__main__':
    # Ensure app binds to all interfaces (for Docker and local testing)
    app.run(host='0.0.0.0', port=5000)
