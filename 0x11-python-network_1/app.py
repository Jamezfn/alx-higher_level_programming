from flask import Flask, request, abort, jsonify
import string
import random
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    if email:
        return f"Your email is: {email}"
    return 'Missing email', 400

@app.route('/status_401')
def status_401():
    abort(401)

@app.route('/status_500')
def status_500():
    abort(500)

@app.route('/search_user', methods=['POST'])
def search_user():
    q = request.form.get('q', '')
    if q == '':
        return jsonify({})
    if q in 'ab':
        return jsonify({'id': random.randint(1000, 9999), 'name': ''.join(random.choices(string.ascii_lowercase, k=10))})
    return jsonify({})

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5000)
