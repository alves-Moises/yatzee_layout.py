import pygame, sys
import dice as d

pygame.init()

def main():
    size = width, height = 800, 600
    # size = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode(size)

    
    print(pygame.display.get_desktop_sizes())
    
    black = 0, 0, 0

    # red = 10, 0, 0
    # green = 0, 10, 0
    # blue = 0, 0, 10
    # cor = [black, red, green, blue]
    


    game = True
    while game:




        screen.fill(black)
        screen.blit(d.dice_1, d.dicerect_1)
        d.dicerect_1 = d.dicerect_1.move(1, 10)


        pygame.display.flip()
        input('asd')

main()