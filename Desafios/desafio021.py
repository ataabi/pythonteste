# Faça um programa em python que abra e reproduza o audio de um arquivo MP3
import mp3play
filename = r'C:\Users\jhony\Music\day.mp3'
clip = mp3play.load(filename)
clip.play()