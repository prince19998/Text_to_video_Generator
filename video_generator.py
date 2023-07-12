import openai 
import re, os
import urllib.request
from gtts import gTTS
from moviepy.editor import *
from config import API_KEY
from api_key import API_KEY

# set your OpenAi API key
openai.api_key =API_KEY

# Read the text file
with open("generated_text.txt", "r") as file:
    text = file.read()

# split the text by , and.
paragraphs = re.split(r"[,.]",text) 

# creat Necessary Folder
os.makedirs("audio")
os.makedirs("images")
os.makedirs("videos")

#loop through each paragraph and generate an image from each
i=1
for para in paragraphs[:-1]:
    response = openai.Image.create(
        prompt=para.strip(),
        n=1,
        size="1024x1024"
    )
    print("Generate New AI Image From Paragraph....")
    image_url= response['date'][0]['url']
    urllib.request.urlretrieve(image_url, f"image/image{i}.jpg")
    print("The Generate Image Saved in Image Folder!")

    #create gTTS instant and save to a file
    tts=gTTS(text=para, lang='en', slow=False)
    tts.save(f"audio/voiceover{i}.mp3")
    print("The paragraph Converated into VoiceOver $ Save in Audio Folder!")

    #Load the audio file using moviepy
    print("Extra voiceover and get duration.....")
    audio_clip=AudioFileClip(f"audio/voiceover{i}.mp3")
    audio_duration = audio_clip.duration

    #Load the image file using moviepy
    print("Customize The Text Clip....")
    image_clip=ImageClip(f"image/image{i}.jpg").set_duration(audio_duration)

    # use moviepy to create a text clip from the text
    print("customize The text Clip...")
    text_clip= TextClip(para, fontsize=50, color="white")
    text_clip=text_clip.set_pos('center'),set_duration(audio_duration)

    #use moviepy to create a final video by concatenating
    #the audio, image, and text clips
    print("Concatenate Audio, Image, Text to Create Final Clip....")
    clip=image_clip.set_audio(audio_clip)
    video=CompositeAudioClip([clip, text_clip])

    #save the final video to the file
    video=video.write_audiofile(f"videos/video{i}.mp4",fps=24)
    print(f"The Video{i} Has Been Created Successfully!")
    i+=1

clips=[]
l_file=os.listdir["videos"]
for file in l_files:
    clip=VideoFileClip(f"videos/{file}") 
    clips.append(clip)

print("Concatenate All The Clip to Create a Final Video...")
final_video=concatenate_audioclips(clipa, method="compose")
final_video=final_video.write_videofile("final_video.mp4")
print("The Final Video Has Been Created Successfully!")       



