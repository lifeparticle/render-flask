from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():

    if 'name' in request.args:
        name = request.args.get('name')
        message = "Hello, " + name + "!"
    else:
        message = "Hello, stranger!"


    return message
