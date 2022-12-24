from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = ''
    if 'name' in request.args:
        name = request.args.get('name', '')
    return f'Hello, {name}!' if name != "" else "Hello, stranger!"