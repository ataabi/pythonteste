# Faça um programa em python que abra e reproduza o audio de um arquivo MP3
from pygame import mixer

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
mixer.music.wait()