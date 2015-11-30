from FactoryPattern.Erde import Erde
from FactoryPattern.Erdmond import Erdmond
from FactoryPattern.Mars import Mars
from FactoryPattern.Sonne import Sonne
import Solarsystem

__author__ = 'Andi Ernhofer'

import pygame

from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Solarsystem import *

topanischt = False

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
if topanischt:
    #Obenansicht
    gluLookAt(0, 0, 30, 0, 0, 0, 0, 1, 0)
else:
    #Seitenansicht
    gluLookAt(0, 30, 0, 0, 0, 0, 0, 0, 1)
glMatrixMode(GL_MODELVIEW)


s = Solarsystem()

s.__init__()

sonne = Sonne()

erde = Erde()
erde.setRotationspunkt(sonne.getPosition())

mars = Mars()
mars.setRotationspunkt(sonne.getPosition())

erdmond = Erdmond()
erdmond.setStern(sonne.getPosition())
erdmond.setPlanet(erde.getPosition())
erdmond.setPlanetGeschwindigkeit(erde.getRotationsgeschwindigkeit())

#create a while loop for as long as the game gets quitted
while not gameExit:
    for event in pygame.event.get():
        #what should happen if someone quitts the game?
        if event.type == pygame.QUIT:
            #while ends after this point
            gameExit = True

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    sonne.zeichnen()
    erde.zeichnen()
    mars.zeichnen()
    erdmond.zeichnen()

    glLoadIdentity()
    #Rote Achse -- X-Achse
    glLineWidth(2.5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(100, 0, 0)
    glEnd()

    glLoadIdentity()
    #Gruene Achse -- Y-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 100, 0)
    glEnd()

    glLoadIdentity()
    #Weisse Achse -- Z-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 100)
    glEnd()

    #update the screen
    pygame.display.flip()

    #set frame rate to 30
    clock.tick(60)

#quitting pygame
pygame.quit()
#quitting python
quit()
