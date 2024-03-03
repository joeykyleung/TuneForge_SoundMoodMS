from os import path 
from pydub import AudioSegment 

# assign files 
input_file = "data/Sad-The%20Wanderer%20-%20Coldness.mp3"
output_file = "data/unit_testing/test.mp3"

# cut song short
song = AudioSegment.from_mp3(input_file)
ten_seconds = 10 * 1000
first_10_seconds = song[:ten_seconds] 
first_10_seconds.export(output_file, format="mp3") 
