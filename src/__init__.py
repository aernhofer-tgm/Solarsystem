__author__ = 'Andi Ernhofer'

import pygame

pygame.init()

white = (255,255,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Solarsystem')

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    pygame.draw.rect(gameDisplay, white,[400,300,50,50])
    pygame.display.update()

pygame.quit()
quit()
