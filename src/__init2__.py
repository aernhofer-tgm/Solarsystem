from FactoryPattern.Solarsystem import Solarsystem
from Kamera import Kamera

__author__ = 'Jakub Kopec'

import pygame
from pygame.locals import *

pygame.init()

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

#create a while loop for as long as the game gets quitted
while not gameExit:
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_PLUS]:
        if kamera.upY == 1:
            kamera.eyeZ -= 1
            kamera.update()
        elif kamera.upZ == 1:
            kamera.eyeY -= 1
            kamera.update()

    if keys[pygame.K_MINUS]:
        if kamera.upY == 1:
            kamera.eyeZ += 1
            kamera.update()
        elif kamera.upZ == 1:
            kamera.eyeY += 1
            kamera.update()

    if keys[pygame.K_s]:
        solarsystem.updateSpeed(0.1)

    if keys[pygame.K_l]:
        solarsystem.updateSpeed(-0.1)

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

            if event.key == pygame.K_p:
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

