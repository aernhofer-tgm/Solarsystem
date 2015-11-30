__author__ = 'jakubkopec'
"""
Planet Interface
------------------------------------------------------------------------------------------
Interface für alle Planeten.
"""
from abc import ABCMeta, abstractmethod

from OpenGL.GL import *
from OpenGL.GLU import *

from Textur.Textur import Textur

class Planet(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, groesse, rotationswinkel, rotationspunkt, position,rotationsrichtung,rotationsgeschwindigkeit,textur):
        self.rotationswinkel = rotationswinkel[0]
        self.eigenrotationswinkel = rotationswinkel[1]
        self.groesse = groesse
        self.rotationsrichtung = rotationsrichtung
        self.rotationsgeschwindigkeit = rotationsgeschwindigkeit
        self.textur = textur
        self.position = position
        self.rotationspunkt = rotationspunkt

    def zeichnen(self):

        #matrix zuruecksetzen
        glLoadIdentity()

        #Rotationspunkt festlegen
        glTranslatef(self.rotationspunkt[0],self.rotationspunkt[1],self.rotationspunkt[2])
        #Rotation um die Sonne
        self.rotationswinkel = self.rotationswinkel + self.rotationsgeschwindigkeit[0]
        glRotatef(self.rotationswinkel,self.rotationsrichtung[0],self.rotationsrichtung[1],self.rotationsrichtung[2])

        #Erde positionieren
        glTranslatef(self.position[0],self.position[1],self.position[2])
        #Rotation um sich selbst
        self.eigenrotationswinkel = self.eigenrotationswinkel + self.rotationsgeschwindigkeit[1]
        glRotatef(self.rotationswinkel,self.rotationsrichtung[0],self.rotationsrichtung[1],self.rotationsrichtung[2])

        #Textur laden
        textur_sonne = Textur.laden(Textur.getPfad(self.textur))
        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur_sonne)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        gluSphere(quadratic,self.groesse,50,50)

    def setRotationspunkt(self,rotationspunkt):
        self.rotationspunkt = rotationspunkt

    def getRotationsgeschwindigkeit(self):
        return self.rotationsgeschwindigkeit[0]

    def getPosition(self):
        return self.position

    def setGeschwindigkeitsfaktor(self,geschwindigkeit):
        self.rotationsgeschwindigkeit[0] *= geschwindigkeit
        self.rotationsgeschwindigkeit[1] *= geschwindigkeit

    @abstractmethod
    def addMond(self):
        pass