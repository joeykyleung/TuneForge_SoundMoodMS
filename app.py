import os
from flask import Flask, request, jsonify
import predict
from storage import azureStorage
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/api/blob_upload', methods=['POST'])
def upload_blob():
    app.logger.info('Blob upload request received:' + request.get_json())
    blob_in = request.get_json().get('wav')
    if not blob_in:
        app.logger.warning('Warning: Conversion request received '
                           + 'with no \'wav\' field.')
        return 'Error: Conversion request received with no \'wav\' field.', 422

    directory = 'uploads/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    blob_out = directory + blob_in
    try:
        azureStorage.download(blob_out, blob_in)
    except Exception as e:
        app.logger.error(e)
        return 'Error: Could not download from blob storage.', 500
    return 'Success: File downloaded successfully from blob storage.', 200


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


@app.route('/api/predict', methods=['GET'])
def predict_mood():
    app.logger.info('Model prediction request received. Processing...')
    folder_path = "uploads/"

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, f))]

    # Get the full path of each file
    file_paths = [os.path.join(folder_path, f) for f in files]

    output = []
    for file in file_paths:
        output.append(predict.predict_mood(file))
        os.remove(file)

    app.logger.info('Model prediction output: ' + str(output))
    return jsonify(output), 200
