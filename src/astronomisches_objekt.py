__author__ = 'Jakub Kopec'

from OpenGL.GL import *
from OpenGL.GLU import *


class AstronomischesObjekt(object):

    def __init__(self):
        pass

    def sonne(textur):
        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        gluSphere(quadratic,1,50,50)

        #Eigenrotation
        glRotatef(1,0,1,0)