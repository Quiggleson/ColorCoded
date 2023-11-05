from flask import Flask, request
from flask_cors import CORS
import os
import random
import string

# Create the Flask app
app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Define function to generate a random filename
def generate_random_filename():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(10))

# Endpoint to show that server is alive
@app.route('/api/', methods=['GET', 'POST'])
def check_alive():
    return {'message': 'Server is alive!'}

# Endpoint to receive an image and save in temporary directory
@app.route('/api/file-upload', methods=['GET', 'POST'])
def receive_image():
    if request.method == 'GET':
        print(f"GET request received from {request.remote_addr}")
        return {'message': 'This API endpoint only accepts POST requests'}, 400
    elif request.method == 'POST':
        print(f"POST request received from {request.remote_addr}")
        if 'image' not in request.files:
            return {'error': 'No image attached'}, 400
        image = request.files['image']
        if not image.filename:
            return {'error': 'No image attached'}, 400
        filename = generate_random_filename() + os.path.splitext(image.filename)[1]
        while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            filename = generate_random_filename() + os.path.splitext(image.filename)[1]
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        return {'filepath': filepath}

if __name__ == '__main__':
    app.run()