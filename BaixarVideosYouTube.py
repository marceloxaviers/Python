# Importando pytube 
from pytube import YouTube

# Baixar video único

YouTube('https://www.youtube.com/watch?v=i1aL-ENakb8&t=6s').streams.first().download()
