from os import path 
from pydub import AudioSegment 

def convert_mp3_to_wav(input_file: str, output_file: str):
    sound = AudioSegment.from_mp3(input_file) 
    sound = sound.set_channels(1)
    sound.export(output_file, format="wav")