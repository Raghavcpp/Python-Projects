import moviepy.editor as mp
import os
path = input("Enter the path for the video file : \n")

videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("audio.mp3")