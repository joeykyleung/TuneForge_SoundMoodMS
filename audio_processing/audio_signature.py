import librosa
import numpy as np

def extract_features(audio_file):
    y, sr = librosa.load(audio_file, duration=10)
    # tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    # features = [tempo, beats, chroma]
    # Add more features as needed
    return chroma