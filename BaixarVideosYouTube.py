# Instalação do pacote, pode ser utilizado as uma das 2 formas apresentadas abaixo
python -m pip install pytube
python -m pip install git+https://github.com/pytube/pytube

# Importando pytube 
from pytube import YouTube

# Baixar video único

YouTube('https://www.youtube.com/watch?v=i1aL-ENakb8&t=6s').streams.first().download()
