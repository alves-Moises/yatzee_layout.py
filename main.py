import pygame, sys

def main():
    pygame.init()
    size = width, height = 1080, 720
    screen = pygame.display.set_mode(size)

    dices = [pygame.image.load("/assets/1.jpg")]
    dicerect = [dices[0].get_rect()]

    
    black = 0, 0, 0
    red = 10, 0, 0
    green = 0, 10, 0
    blue = 0, 0, 10
    cor = [black, red, green, blue]
    while 1:


            screen.fill(black)
            pygame.display.flip()
main()