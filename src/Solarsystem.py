__author__ = 'Jakub Kopec'
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from astronomisches_objekt import *
from textur import *

class Solarsystem(object):

    def __init__(self):
        pass

    def zeichnen():
        #clear the surface
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #draw something pretty
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)

        #Textur laden
        textur_sonne = Textur.laden("../texturen/sun.gif")

        #Sonne zeichnen
        AstronomischesObjekt.sonne(textur_sonne)
