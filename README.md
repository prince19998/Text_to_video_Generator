# Text_to_video_Generator

This project is a text to video generator that can convert any textual input into a video output. The video output can be customized with different parameters such as voice, background music, animation style, etc.

Installation
To install this project, you need to have Python 3.6 or higher and the following libraries:

OpenCV
NLTK
gTTS
moviepy
You can install them using pip


Usage
To use this project, you need to run the main.py script with the following arguments:

–input: The path to the text file that contains the input text. The text file should have one sentence per line.
–output: The path to the video file that will be generated. The video file should have a .mp4 extension.
–voice: The voice that will be used for the narration. You can choose from ‘male’ or ‘female’.
–music: The path to the audio file that will be used as the background music. The audio file should have a .mp3 extension.
–style: The animation style that will be used for the video. You can choose from ‘cartoon’, ‘realistic’, or ‘abstract’.
For example, to generate a video from the text file input.txt with a female voice, a music file music.mp3, and a cartoon style, you can run:
