from pytube import YouTube

VIDEO_URL = 'https://www.youtube.com/watch?v=i1aL-ENakb8&t=6s'
yt = YouTube(VIDEO_URL)

video = yt.streams.get_highest_resolution()
video.download()
