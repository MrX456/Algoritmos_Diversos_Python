# Executar arquivo mp3 em Python
from pygame import mixer
mixer.init()
mixer.music.load('D021.mp3')
mixer.music.play()
input('Aperte s para sair?')