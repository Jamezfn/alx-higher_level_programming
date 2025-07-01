from flask import Flask, make_response, request
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/route_1')
def route_1():
    return 'Route 2'

@app.route('/route_3', methods=['DELETE'])
def route_3():
    return 'I\'m a DELETE request'
@app.route('/route_4', methods=['OPTIONS', 'HEAD', 'PUT'])
def route_4():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['ALLOW'] = 'OPTION, HEAD, PUT' 
        return response
    elif request.method == 'HEAD':
        return '', 200
    elif request.method == 'PUT':
        return 'PUT request processed', 200

@app.route('/route_5', methods=['GET'])
def route_5():
    if request.headers.get("X-School-User-Id") == '98':
        return 'Hello School!'
    return 'Invalid User ID', 403

@app.route('/route_6', methods=['POST'])
def route_6():
    email = request.form.get('email')
    subject = request.form.get('subject')
    if email and subject:
        return f"POST params:\n    email: {email}\n    subject: {subject}"
    return 'Missing parameters', 400

@app.route('/route_json', methods=['POST'])
def route_json():
    try:
        json.loads(request.get_data(as_text=True))
        return 'Valid JSON', 200
    except json.JSONDecodeError:
        return 'Not a valid JSON', 400

@app.route('/catch_me', methods=['POST'])
def catch_me():
    return 'You got me!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
