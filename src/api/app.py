from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/api/', methods=['GET', 'POST'])
def ack():
    message = f"I have received {request.method} request with the following data: {request.data}"
    return {'data': message}