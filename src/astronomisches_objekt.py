__author__ = 'Jakub Kopec'

from OpenGL.GL import *
from OpenGL.GLU import *


class AstronomischesObjekt(object):

    def __init__(self):
        pass

    def sonne(textur):

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45,(1280/720),0.1,100)
        #glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 0, 0, 0, -10, 0, 1, 0)
        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form

        glTranslatef(0.0, 0.0, -10)
        gluSphere(quadratic,2,50,50)
        glTranslatef(0.0, 0.0, 10)

        #glRotatef(90, 1.0, 0.0, 0.0)  # Rotatation um X-Achse
        #glRotatef(0, 0.0, 1.0, 0.0)  # Rotatation um Y-Achse
        #glRotatef(0, 0.0, 0.0, 1.0)  # Rotatation um Z-Achse




    def erde(textur):
        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        glTranslatef(4.0, 0.0, -5)
        gluSphere(quadratic,0.5,50,50)
        glTranslatef(-4.0, 0.0, 5)
        #Eigenrotation
