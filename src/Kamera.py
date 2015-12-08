from OpenGL.GL import *
from OpenGL.GLU import *

__author__ = 'Jakub Kopec'

class Kamera(object):

    def __init__(self):
        self.width = 1280
        self.height = 720

        self.blickwinkel = 45

        self.eyeX = 0
        self.eyeY = -50
        self.eyeZ = 0

        self.centerX = 0
        self.centerY = 0
        self.centerZ = 0

        self.upX = 0
        self.upY = 0
        self.upZ = 1

        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(self.blickwinkel,(self.width/self.height),0.1,100)

        gluLookAt(self.eyeX, self.eyeY, self.eyeZ, self.centerX, self.centerY, self.centerZ, self.upX, self.upY, self.upZ)

        glMatrixMode(GL_MODELVIEW)

    def updateScreenSize(self,width,height):
        self.width = width
        self.height = height

        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(self.blickwinkel,(self.width/self.height),0.1,100)

        gluLookAt(self.eyeX, self.eyeY, self.eyeZ, self.centerX, self.centerY, self.centerZ, self.upX, self.upY, self.upZ)

        glMatrixMode(GL_MODELVIEW)

    def update(self):
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(self.blickwinkel,(self.width/self.height),0.1,100)

        gluLookAt(self.eyeX, self.eyeY, self.eyeZ, self.centerX, self.centerY, self.centerZ, self.upX, self.upY, self.upZ)

        glMatrixMode(GL_MODELVIEW)

    def reset(self):
        self.eyeX = 0
        self.eyeY = 0
        self.eyeZ = 0

        self.centerX = 0
        self.centerY = 0
        self.centerZ = 0

        self.upX = 0
        self.upY = 0
        self.upZ = 0