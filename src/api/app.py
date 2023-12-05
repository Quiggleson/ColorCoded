from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from PIL import Image
from colorthief import ColorThief
from werkzeug.utils import secure_filename
from cbprocessing import nored
import os
import random
import string
import numpy as np
import cv2

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
        return {'filepath': filename}
    
@app.route('/api/file/<path:filename>', methods=['GET'])
def image(filename):
    if os.path.exists(f'{app.config["UPLOAD_FOLDER"]}/{filename}'):
        return send_file(f'{app.config["UPLOAD_FOLDER"]}/{filename}', mimetype="image/png")
    else:
        return 'File not found', 404
    
@app.route('/api/colors/<path:filename>', methods=['GET'])
def colors(filename):
    if not os.path.exists(f'{app.config["UPLOAD_FOLDER"]}/{filename}'):
        return 'File not found', 404
    
    # colors = []
    
    # img = cv2.imread(f'{app.config["UPLOAD_FOLDER"]}/{filename}')
    # RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        color_thief = ColorThief(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        print(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        print(cv2.imread(os.path.join(app.config["UPLOAD_FOLDER"], filename)).shape)
        colors = color_thief.get_palette(color_count=15)
    except:
        #make it so the image colors are all white
        colors = [(255,255,255)]*15
    print(colors)
    top_colors = [f'#{c[0]:02x}{c[1]:02x}{c[2]:02x}' for c in colors]
    # for row in RGB_img:
    #     for pixel in row:
    #         hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel)
    #         colors.append(hex_color)

    # return random.choices(colors,k=16)
    return top_colors

# Accepts POST request with a list of colors to remain unchanged
# like {"colors": [[255,255,255], [100,100,100]] }
@app.route('/api/red/<path:filename>', methods=['POST'])
def red(filename):
    if not os.path.exists(f'{app.config["UPLOAD_FOLDER"]}/{filename}'):
        return 'File not found', 404
    print(f'request: {request.get_json()}')
    nored_filename = nored(request.get_json()["colors"], app.config['UPLOAD_FOLDER'], filename)
    return {"nored_filename": nored_filename}

if __name__ == '__main__':
    app.run()