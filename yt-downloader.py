import youtube_dl

url = input("Enter the URL for the video : \n")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download([url])