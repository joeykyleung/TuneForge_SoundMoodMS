# TuneForge Sound Mood Microservice

A sophisticated deep learning-based microservice that analyzes the emotional content of audio using advanced signal processing and convolutional neural networks (CNN).

## Technical Overview

This microservice is a critical component of the TuneForge platform, responsible for:
1. Audio signal processing and feature extraction
2. Mood classification using deep learning
3. Real-time audio analysis through RESTful APIs

### Machine Learning Architecture

The service implements a custom CNN architecture optimized for audio mood classification:
- Input Layer: Processes chromagram features
- Convolutional Layer: 32 filters with 3x3 kernel
- ReLU Activation & MaxPooling
- Fully Connected Layers: 128 neurons with ReLU
- Output Layer: Multi-class mood classification

### Audio Processing Pipeline

1. **Feature Extraction**
   - Utilizes `librosa` for advanced audio processing
   - Extracts chromagram features using Short-Time Fourier Transform (STFT)
   - Processes temporal and spectral characteristics

2. **Data Processing**
   - Converts various audio formats to WAV
   - Implements real-time audio signature generation
   - Handles variable-length audio inputs

## Technical Challenges & Solutions

### 1. Real-time Processing
**Challenge:** Processing audio files efficiently in real-time
**Solution:** 
- Implemented efficient audio feature extraction
- Optimized CNN architecture for quick inference
- Utilized PyTorch for GPU acceleration

### 2. Audio Format Compatibility
**Challenge:** Handling various audio formats
**Solution:**
- Developed robust MP3 to WAV conversion pipeline
- Implemented format validation and error handling
- Standardized audio preprocessing

### 3. Model Deployment
**Challenge:** Deploying ML model in production
**Solution:**
- Used PyTorch model serialization
- Implemented model state management
- Created efficient inference pipeline

## Technology Stack

- **Deep Learning Framework:** PyTorch
- **Audio Processing:** librosa
- **Cloud Storage:** Azure Blob Storage
- **API Framework:** Flask
- **Testing:** Python unittest

## Project Structure
```
.
├── README.md
├── app.py                        # Main Flask application
├── audio_processing/            
│   ├── audio_signature.py       # Audio feature extraction
│   ├── mp3.py                   # MP3 handling
│   └── mp3_to_wav.py           # Format conversion
├── cnn_model/
│   ├── audio_cnn.py            # CNN architecture
│   └── mood_predictor_state_dict.pth  # Trained model
├── data/
│   └── unit_testing/           # Test data
└── test/                       # Unit tests
```

## Setup and Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd TuneForge_SoundMoodMS
```

2. Set up environment variables:
```bash
export AZURE_STORAGE_CONNECTION_STRING="your-connection-string"
export BLOB_CONTAINER_NAME="your-container-name"
```

3. Install dependencies:
```bash
pip install torch librosa numpy flask azure-storage-blob
```

4. Run the service:
```bash
python app.py
```

## API Endpoints

- `POST /api/blob_upload`: Upload audio file for analysis
- `GET /api/predict`: Get mood prediction for uploaded audio

## Testing

Run the test suite:
```bash
python -m unittest discover test
```

## Attribution

Audio dataset sourced from:
- [Free Music Archive](https://freemusicarchive.org/)

MP3 to WAV conversion adapted from:
- [GeeksforGeeks Tutorial](https://www.geeksforgeeks.org/convert-mp3-to-wav-using-python/)
