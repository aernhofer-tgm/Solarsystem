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

#Config
topansicht = True
geschwindigkeit = 1

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
if topansicht:
    #Obenansicht
    gluLookAt(0, 0, 30, 0, 0, 0, 0, 1, 0)
else:
    #Seitenansicht
    gluLookAt(0, 30, 0, 0, 0, 0, 0, 0, 1)
glMatrixMode(GL_MODELVIEW)


s = Solarsystem()

s.__init__()


sonne = Sonne()
sonne.setGeschwindigkeitsfaktor(geschwindigkeit)

erde = Erde()
erde.setRotationspunkt(sonne.getPosition())
erde.setGeschwindigkeitsfaktor(geschwindigkeit)

mars = Mars()
mars.setRotationspunkt(sonne.getPosition())
mars.setGeschwindigkeitsfaktor(geschwindigkeit)

erdmond = Erdmond()
erdmond.setStern(sonne.getPosition())
erdmond.setPlanet(erde.getPosition())
erdmond.setPlanetGeschwindigkeit(erde.getRotationsgeschwindigkeit())
erdmond.setGeschwindigkeitsfaktor(geschwindigkeit)

erdgeschwindigkeit = [-10, -1.5]

#create a while loop for as long as the game gets quitted
while not gameExit:
    for event in pygame.event.get():
        #what should happen if someone quitts the game?
        if event.type == pygame.QUIT:
            #while ends after this point
            gameExit = True
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                geschwindigkeit = round(geschwindigkeit+0.1,1)
                print("langsamer" + str(geschwindigkeit))

                #Geschindigkeit updaten
                sonne.setGeschwindigkeitsfaktor(geschwindigkeit)
                erde.setGeschwindigkeitsfaktor(geschwindigkeit)
                mars.setGeschwindigkeitsfaktor(geschwindigkeit)
                erdmond.setPlanetGeschwindigkeit(erde.getRotationsgeschwindigkeit())
                erdmond.setGeschwindigkeitsfaktor(geschwindigkeit)

            elif event.key == pygame.K_l:
                if geschwindigkeit != 0:
                    geschwindigkeit = round(geschwindigkeit-0.1,1)
                    print("langsamer" + str(geschwindigkeit))

                    #Geschindigkeit updaten
                    sonne.setGeschwindigkeitsfaktor(geschwindigkeit)
                    erde.setGeschwindigkeitsfaktor(geschwindigkeit)
                    mars.setGeschwindigkeitsfaktor(geschwindigkeit)
                    erdmond.setPlanetGeschwindigkeit(erde.getRotationsgeschwindigkeit())
                    erdmond.setGeschwindigkeitsfaktor(geschwindigkeit)

            elif event.key == pygame.K_p:
                if geschwindigkeit != 0:
                    geschwindigkeitsfaktoralt = geschwindigkeit
                    sonnengeschwindigkeit = sonne.getGeschwindigkeit()
                    erdgeschwindigkeit = erde.getGeschwindigkeit()
                    print(erdgeschwindigkeit)
                    marsgeschwindigkeit = mars.getGeschwindigkeit()
                    geschwindigkeit = 0
                else:
                    sonne.setGeschwindigkeit(sonnengeschwindigkeit)
                    print(erdgeschwindigkeit)
                    erde.setGeschwindigkeit(erdgeschwindigkeit)
                    mars.setGeschwindigkeit(marsgeschwindigkeit)
                    geschwindigkeit = geschwindigkeitsfaktoralt

                #Geschindigkeit updatens
                sonne.setGeschwindigkeitsfaktor(geschwindigkeit)
                erde.setGeschwindigkeitsfaktor(geschwindigkeit)
                mars.setGeschwindigkeitsfaktor(geschwindigkeit)
                erdmond.setPlanetGeschwindigkeit(erde.getRotationsgeschwindigkeit())
                erdmond.setGeschwindigkeitsfaktor(geschwindigkeit)

            elif event.key == pygame.K_k:
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                gluPerspective(45,(display_width/display_height),0.1,100)

                if topansicht==False:
                    #Obenansicht
                    topansicht = True
                    gluLookAt(0, 0, 30, 0, 0, 0, 0, 1, 0)
                else:
                    #Seitenansicht
                    topansicht = False
                    gluLookAt(0, 30, 0, 0, 0, 0, 0, 0, 1)
                glMatrixMode(GL_MODELVIEW)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    #Objekte zeichnen
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
    clock.tick(30)

#quitting pygame
pygame.quit()
#quitting python
quit()

