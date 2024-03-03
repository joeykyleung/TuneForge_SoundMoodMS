import os
from flask import Flask, request, jsonify
from project import predict

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has a file attached
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    # Check if the file has a name
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Handle the file (e.g., save it to a folder)
    # Make sure to create a folder named 'api/uploads' in the same directory as your script
    file.save('uploads/' + file.filename)

    return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/api/predict', methods = ['GET'])
def predict_mood():
    folder_path = "uploads/"

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Get the full path of each file
    file_paths = [os.path.join(folder_path, f) for f in files]

    output = []
    for file in file_paths:
        output.append(predict.predict_mood(file))
        os.remove(file)

    return jsonify(output), 200
