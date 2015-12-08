from FactoryPattern.Solarsystem import Solarsystem
from Kamera import Kamera
from licht import Licht

__author__ = 'Jakub Kopec'

import pygame
from pygame.locals import *

"""
STEUERUNG
---------

k           Kammera Ansicht aendern
p           Pause
.           Schneller
,           langsamer
Pfeiltasten Bewegen
wasd        Ansicht aendern
+           Ranzoomen
-           Wegzoomen
esc         Beenden
linkemaus   reinzoomen
rechtemaus  wegzoomen
"""

class Main(object):

    def main():
        pygame.init()

        infoObject = pygame.display.Info()
        #pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

        #define display size
        display_width = 1280
        display_height = 720
        fullscreen = False

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

        #Maus ausblenden
        #pygame.mouse.set_visible(False)

        #Mauszeiger setzen
        pygame.mouse.set_pos(display_width/2,display_height/2)

        #Licht
        licht = Licht()
        #licht.anknipsen()
        licht_schalter = False

        #Textur
        textur_schalter = True

        #create a while loop for as long as the game gets quitted
        while not gameExit:
            keys = pygame.key.get_pressed()  #checking pressed keys
            mousebutton = pygame.mouse.get_pressed()

            #print(pygame.mouse.get_pos())

            drehung = pygame.mouse.get_rel()

            #print(drehung)

            #Mauszeiger setzen
            if drehung[0] == 0 and drehung[1] == 0:
                #pygame.mouse.set_pos(display_width/2,display_height/2)
                #jakub = pygame.mouse.get_rel()
                pass
            else:

                #drehung mit der maus
                kamera.centerX += drehung[0]/20
                if kamera.upY == 1:
                    kamera.centerY += -drehung[1]/20
                elif kamera.upZ == 1:
                    kamera.centerZ += -drehung[1]/20
                kamera.update()

            #Zoom
            if keys[pygame.K_PLUS]:
                if kamera.upY == 1:
                    kamera.eyeZ -= 1
                    kamera.update()
                elif kamera.upZ == 1:
                    kamera.eyeY += 1
                    kamera.update()

            if keys[pygame.K_MINUS]:
                if kamera.upY == 1:
                    kamera.eyeZ += 1
                    kamera.update()
                elif kamera.upZ == 1:
                    kamera.eyeY -= 1
                    kamera.update()

            #Geschwindigkeit
            if keys[pygame.K_PERIOD]:
                solarsystem.updateSpeed(0.1)

            if keys[pygame.K_COMMA]:
                if solarsystem.geschwindigkeit != 0:
                    solarsystem.updateSpeed(-0.1)

            #Bewegen
            if keys[pygame.K_RIGHT]:
                kamera.eyeX += 1
                kamera.update()

            if keys[pygame.K_LEFT]:
                kamera.eyeX -= 1
                kamera.update()

            if keys[pygame.K_UP]:
                kamera.eyeY += 1
                kamera.update()

            if keys[pygame.K_DOWN]:
                kamera.eyeY -= 1
                kamera.update()

            #Blickwinkel
            if keys[pygame.K_d]:
                kamera.centerX += 1
                kamera.eyeX += 1
                kamera.update()

            if keys[pygame.K_a]:
                kamera.centerX -= 1
                kamera.eyeX -= 1
                kamera.update()

            if keys[pygame.K_w]:
                kamera.centerY += 1
                kamera.eyeY += 1
                kamera.update()

            if keys[pygame.K_s]:
                kamera.centerY -= 1
                kamera.eyeY -= 1
                kamera.update()

            for event in pygame.event.get():
                #what should happen if someone quitts the game?
                if event.type == pygame.QUIT:
                    #while ends after this point
                    gameExit = True

                elif event.type == MOUSEBUTTONDOWN:

                    #linksklick Maus
                    if event.button == 1:
                        if licht_schalter == False:
                            licht_schalter = True
                            licht.anknipsen()
                        else:
                            licht_schalter = False
                            licht.ausknipsen()

                    #mausradklick
                    if event.button == 2:
                        if solarsystem.geschwindigkeit != 0:
                            solarsystem.pause(True)
                        else:
                            solarsystem.pause(False)

                    #Rechtsklick Maus
                    if event.button == 3:
                        if textur_schalter == True:
                            textur_schalter = False
                            solarsystem.disableTexture()
                        else:
                            textur_schalter = True
                            solarsystem.enableTexture()

                elif event.type == VIDEORESIZE:
                    width, height = event.size
                    screen = pygame.display.set_mode((width,height), HWSURFACE|DOUBLEBUF|OPENGL|RESIZABLE)
                    solarsystem = Solarsystem()
                    kamera.updateScreenSize(width,height)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if kamera.upY == 1:
                            kamera.eyeZ -= 10
                            kamera.update()
                        elif kamera.upZ == 1:
                            kamera.eyeY += 7
                            kamera.update()
                    if event.button == 5:
                        if kamera.upY == 1:
                            kamera.eyeZ += 10
                            kamera.update()
                        elif kamera.upZ == 1:
                            kamera.eyeY -= 7
                            kamera.update()

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_p:
                        if solarsystem.geschwindigkeit != 0:
                            solarsystem.pause(True)
                        else:
                            solarsystem.pause(False)

                    elif event.key == pygame.K_k:
                        #Mauszeiger zuruecksetzen
                        drehung = pygame.mouse.get_rel() # Maus hupft sonst nach kamera wechsel
                        pygame.mouse.set_pos(display_width/2,display_height/2)
                        drehung = pygame.mouse.get_rel() # Maus hupft sonst nach kamera wechsel

                        if kamera.upY == 1:
                            kamera.reset()
                            kamera.upZ = 1
                            kamera.eyeY = -50
                            kamera.update()
                        elif kamera.upZ == 1:
                            kamera.reset()
                            kamera.upY = 1
                            kamera.eyeZ = 30
                            kamera.update()
                    elif event.key == pygame.K_ESCAPE:
                        gameExit = True

                    elif event.key == pygame.K_F11:
                        if fullscreen:
                            fullscreen = False
                            screen = pygame.display.set_mode((display_width,display_height), DOUBLEBUF|OPENGL|RESIZABLE)
                            solarsystem = Solarsystem()
                            kamera.updateScreenSize(display_width,display_height)
                        else:
                            fullscreen = True
                            #pygame.display.toggle_fullscreen()
                            #screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), FULLSCREEN|HWSURFACE|DOUBLEBUF|OPENGL)
                            screen = pygame.display.set_mode((display_width,display_height), FULLSCREEN|HWSURFACE|DOUBLEBUF|OPENGL)
                            solarsystem = Solarsystem()
                            kamera.updateScreenSize(display_width,display_height)

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

if __name__ == '__main__':
    Main.main()