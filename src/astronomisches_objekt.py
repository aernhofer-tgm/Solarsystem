__author__ = 'Jakub Kopec'

from OpenGL.GL import *
from OpenGL.GLU import *


class AstronomischesObjekt(object):

    def __init__(self):
        pass

    def sonne(textur):


        #glLoadIdentity()
        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        gluSphere(quadratic,2.5,50,50)


    def erde(textur):

        #iwas was uns das rotieren erlaubt
        #glMatrixMode(GL_MODELVIEW)

        #glLoadIdentity()

        #rotation um die Sonne
        #glRotatef(1, 0, 1, 0)

        #glPushMatrix()
        #glRotatef(0, 1.0, 0.0, 0.0)  # Rotatation um X-Achse
        #glRotatef(0, 0.0, 1.0, 0.0)  # Rotatation um Y-Achse
        #glRotatef(1, 0.0, 0.0, 1.0)  # Rotatation um Z-Achse


        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        #glTranslatef(5.0, 0.0, 0.0)
        gluSphere(quadratic,1,50,50)
        #glTranslatef(-5.0, 0.0, 0.0)
        #glPopMatrix()


    def mars(textur):

        #iwas was uns das rotieren erlaubt
        #glMatrixMode(GL_MODELVIEW)

        #rotation um die Sonne
        #glRotatef(1, 0, 1, 0)

        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        glTranslatef(8.0, 0.0, 0.0)
        gluSphere(quadratic,0.8,50,50)
        glTranslatef(-8.0, 0.0, 0.0)

    def mond(textur):

        #iwas was uns das rotieren erlaubt
        glMatrixMode(GL_MODELVIEW)

        #rotation um die Sonne
        glRotatef(1, 0.0, 0.0, -10.0)

        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        glTranslatef(4.0, 0.0, -10)
        gluSphere(quadratic,0.5,50,50)
        glTranslatef(-4.0, 0.0, 10)