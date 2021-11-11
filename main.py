import pygame, sys


def main():
    pygame.init()
    size = width, height = 1080, 720
    screen = pygame.display.set_mode(size)
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename="audio.wav")
    audio = pygame.mixer.Channel.get_sound("audio.wav")
    audio.play() 

main()