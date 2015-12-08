__author__ = 'Jakub Kopec'

from OpenGL.GL import *
from OpenGL.GLU import *

class Licht(object):

    def __init__(self):
        pass

    def anknipsen(self):
        #print("Licht aufdrehen")
        glEnable(GL_LIGHTING)
        #lightZeroPosition = (10, 4, 10, 1)
        lightZeroPosition = (4, 4, 4, 1)
        lightZeroColor = (0.8, 1, 0.8, 1) #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

    def ausknipsen(self):
        glDisable(GL_LIGHTING)