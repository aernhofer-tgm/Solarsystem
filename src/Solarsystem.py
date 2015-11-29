__author__ = 'Jakub Kopec'

from astronomisches_objekt import *
from textur import *

class Solarsystem(object):

    global penis,nudel

    def __init__(self):
        self.penis = 1
        self.nudel = 1
        pass

    def zeichnen(self):

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #draw something pretty
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)

        glLoadIdentity()
        glTranslatef(0, 0.0, 0)
        self.penis = self.penis + 1
        glRotatef(self.penis,0,1,0)
        #Textur laden
        textur_sonne = Textur.laden("../texturen/sun.gif")
        #Erde zeichnen
        AstronomischesObjekt.sonne(textur_sonne)

        glLoadIdentity()
        self.nudel = self.nudel - 1
        glRotatef(self.nudel,0,1,0)
        glTranslatef(5.0, 0.0, 0)
        glRotatef(self.nudel,0,1,0)
        #Textur laden
        textur_erde = Textur.laden("../texturen/erde.jpg")
        #Erde zeichnen
        AstronomischesObjekt.erde(textur_erde)

