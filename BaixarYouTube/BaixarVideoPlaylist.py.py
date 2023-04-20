from pytube import YouTube, Playlist

PLAYLIST_URL = 'https://www.youtube.com/watch?v=Q8DS2SR9VjE&list=PLnNURxKyyLIIBGBjTU8MQ2JodP7KxBxji'
playlist = Playlist(PLAYLIST_URL)


for url in playlist:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path='playlist')