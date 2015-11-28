__author__ = 'Andi Ernhofer'

import pygame

from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Solarsystem import *
import sys

pygame.init()

#define colors
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)

#define display size
display_width = 1280
display_height = 720

#creating the game display
screen = pygame.display.set_mode((display_width,display_height), DOUBLEBUF|OPENGL)

#setting the name of the window
pygame.display.set_caption('Solarsystem')

#define variable for exiting game
gameExit = False

#define clock for setting frame rates
clock = pygame.time.Clock()

#set the perspective

glViewport(0, 0, display_width, display_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45,(display_width/display_height),0.1,100)
glMatrixMode(GL_MODELVIEW)

#Translate something ... no idea ... (set perspective on z = -5 I guess ...)
glTranslatef(0.0, 0.0, -10)

#Rotate nothing
#glRotatef(0, 0, 0, 0)


#create a while loop for as long as the game gets quitted
while not gameExit:
    for event in pygame.event.get():
        #what should happen if someone quitts the game?
        if event.type == pygame.QUIT:
            #while ends after this point
            gameExit = True

    Solarsystem.zeichnen()
    #glRotatef(1, 0.0, 0.0, -10.0)
    #update the screen
    pygame.display.flip()

    #set frame rate to 30
    clock.tick(30)

#quitting pygame
pygame.quit()
#quitting python
quit()
