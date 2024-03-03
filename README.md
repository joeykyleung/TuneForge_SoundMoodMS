Sources:
1. Audio Provisioned on: https://freemusicarchive.org/
2. mp3_to_wav.py code obtained from: https://www.geeksforgeeks.org/convert-mp3-to-wav-using-python/

Project Structure:
.
├── README.md
├── __init__.py
├── app.py
├── audio_processing
│   ├── audio_signature.py
│   ├── audio_signature_deprecated.py
│   ├── mp3.py
│   └── mp3_to_wav.py
├── cnn_model
│   ├── __init__.py
│   ├── audio_cnn.py
│   └── mood_predictor_state_dict.pth
├── data
│   └── unit_testing
│       ├── test.json
│       ├── test.mp3
│       └── test.wav
├── predict.py
└── test
    ├── __init__.py
    ├── test_audio_signature.py
    └── test_main.py