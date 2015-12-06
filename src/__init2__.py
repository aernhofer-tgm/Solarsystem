from FactoryPattern.Solarsystem import Solarsystem
from Kamera import Kamera

__author__ = 'Jakub Kopec'

import pygame

from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *

#Config
topansicht = True
geschwindigkeit = 1

zoom = 1

pygame.init()

#define colors
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)

#define display size
display_width = 1280
display_height = 720

#creating the game display
screen = pygame.display.set_mode((display_width,display_height), DOUBLEBUF|OPENGL|RESIZABLE)

#setting the name of the window
pygame.display.set_caption('Solarsystem')

#define variable for exiting game
gameExit = False

#define clock for setting frame rates
clock = pygame.time.Clock()

#set the perspective
kamera = Kamera()

#initialize the solar system
solarsystem = Solarsystem()

erdgeschwindigkeit = [-10, -1.5]

old_speed = 1

#create a while loop for as long as the game gets quitted
while not gameExit:
    for event in pygame.event.get():
        #what should happen if someone quitts the game?
        if event.type == pygame.QUIT:
            #while ends after this point
            gameExit = True

        elif event.type == VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width,height), HWSURFACE|DOUBLEBUF|OPENGL|RESIZABLE)
            solarsystem = Solarsystem()
            kamera.updateScreenSize(width,height)

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_PLUS:
                if kamera.upY == 1:
                    kamera.eyeZ -= 1
                    kamera.update()
                elif kamera.upZ == 1:
                    kamera.eyeY -= 1
                    kamera.update()

            if event.key == pygame.K_MINUS:
                if kamera.upY == 1:
                    kamera.eyeZ += 1
                    kamera.update()
                elif kamera.upZ == 1:
                    kamera.eyeY += 1
                    kamera.update()

            if event.key == pygame.K_s:
                solarsystem.updateSpeed(0.1)

            elif event.key == pygame.K_l:
                solarsystem.updateSpeed(-0.1)

            elif event.key == pygame.K_p:
                if solarsystem.geschwindigkeit != 0:
                    solarsystem.pause(True)
                else:
                    solarsystem.pause(False)

            elif event.key == pygame.K_k:
                if kamera.upY == 1:
                    kamera.reset()
                    kamera.upZ = 1
                    kamera.eyeY = 30
                    kamera.update()
                elif kamera.upZ == 1:
                    kamera.reset()
                    kamera.upY = 1
                    kamera.eyeZ = 30
                    kamera.update()

    #Objekte zeichnen
    solarsystem.zeichnen()

    #Achsen zeichnen
    solarsystem.achsenZeichnen()

    #Bahnen zeichnen
    solarsystem.bahnenZeichnen()

    #update the screen
    pygame.display.flip()

    #set frame rate to 30
    clock.tick(30)

#quitting pygame
pygame.quit()
#quitting python
quit()

