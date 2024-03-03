import project.cnn_model.audio_cnn as audio_cnn
from project.audio_processing import audio_signature
import torch

INPUT_SHAPE = (12,431)
CLASSES = 2
MODEL_STATE_DICT_FILE_PATH = "cnn_model/mood_predictor_state_dict.pth"

model = audio_cnn.AudioCNN(INPUT_SHAPE, CLASSES)
model.load_state_dict(torch.load(MODEL_STATE_DICT_FILE_PATH))

def convert_wav_to_tensor_input(wav_file: str) -> torch.tensor:
    "Preprocessing wav file into a pytorch tensor of the features of that wav file"
    global INPUT_SHAPE
    features = audio_signature.extract_features(wav_file)
    assert(features.shape == INPUT_SHAPE), "The song must be 10 second long or longer"
    return torch.from_numpy(features).reshape(1,12,431)

def predict_mood(wav_file: str) -> str:
    global model
    X_input = convert_wav_to_tensor_input(wav_file)
    _, prediction = torch.max(model(X_input),1)
    mood = "happy" if prediction.item() else "sad"
    return mood
