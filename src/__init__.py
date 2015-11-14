__author__ = 'Andi Ernhofer'

import pygame

pygame.init()

#define colors
white = (255,255,255)
black = (0,0,0)

#define display size
display_width = 1280
display_height = 720

#creating the game display
screen = pygame.display.set_mode((display_width,display_height))

#setting the name of the window
pygame.display.set_caption('Solarsystem')

#define variable for exiting game
gameExit = False

#define clock for setting frame rates
clock = pygame.time.Clock()

#create a while loop for as long as the game gets quitted
while not gameExit:
    for event in pygame.event.get():
        #what should happen if someone quitts the game?
        if event.type == pygame.QUIT:
            #while ends after this point
            gameExit = True

    #paint the whole screen black to remove not wanted parts from any older frame
    screen.fill(black)

    #paint something

    #update to see changes
    pygame.display.update()

    #set frame rate to 30
    clock.tick(30)

#quitting pygame
pygame.quit()
#quitting python
quit()
