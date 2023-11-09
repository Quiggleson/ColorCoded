# Imports
import requests

# [ This module serves to make requests to our API endpoints in Flask ]

# Make a request to 127.0.0.1:5000/api to check if it is alive
def test_check_alive():
    response = requests.get('http://127.0.0.1:5000/api/')
    if response.status_code == 200:
        print("Server is alive!")
        return True
    else:
        print("Server is not alive. Make sure you are running the Flask backend with `python3 ./src/api/app.py` in your venv.")
        return False

# Make a request to 127.0.0.1:5000/api/file-upload to upload an image
def test_upload_image():
    # Note: Our test image is stored in test/demo.jpg
    # Our Flask server expects a file with the id of "image"
    image_upload = {'image': open('test/demo.jpg', 'rb')}
    response = requests.post('http://127.0.0.1:5000/api/file-upload', files=image_upload)
    if response.status_code == 200:
        print("Image uploaded successfully!")
        print("Response:")
        print(response.json())
        return True
    else:
        print("Image upload failed!")
        print("Stack trace:")
        print(response.text)
        return False

if __name__ == '__main__':
    print("Hello!")
    # Uncomment any of the following lines to check functionality
    test_check_alive() # Checks if the server is alive by sending a GET request
    # test_upload_image() # Uploads an image to the server by sending a POST request