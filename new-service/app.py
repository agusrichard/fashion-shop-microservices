from flask import Flask, request


app = Flask(__name__)


@app.route('/new-service/')
def index():
    print('request', request.headers)
    return 'New service'
