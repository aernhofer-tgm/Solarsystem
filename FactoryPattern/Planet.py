from FactoryPattern.AstronomischesObjekt import AstronomischesObjekt

__author__ = 'Andreas Ernhofer, Jakub Kopec'
"""
Planet Interface
------------------------------------------------------------------------------------------
Interface für alle Planeten.
"""
from abc import ABCMeta, abstractmethod

from OpenGL.GL import *
from OpenGL.GLU import *

from Textur.Textur import Textur

class Planet(AstronomischesObjekt):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, groesse, rotationswinkel, rotationspunkt, position,rotationsrichtung,rotationsgeschwindigkeit,texturname):
        self.rotationswinkel = rotationswinkel[0]
        self.eigenrotationswinkel = rotationswinkel[1]
        self.groesse = groesse
        self.rotationsrichtung = rotationsrichtung
        self.rotationsurgeschwindigkeit = rotationsgeschwindigkeit
        self.rotationsgeschwindigkeit = [1,1]
        self.rotationsgeschwindigkeit[0] = rotationsgeschwindigkeit[0]
        self.rotationsgeschwindigkeit[1] = rotationsgeschwindigkeit[1]
        self.texturname = texturname
        self.position = position
        self.rotationspunkt = rotationspunkt
        #Textur laden
        self.textur_planet = Textur.laden(self.texturname)

    def zeichnen(self):

        #matrix zuruecksetzen
        glLoadIdentity()

        #Rotationspunkt festlegen
        glTranslatef(self.rotationspunkt[0],self.rotationspunkt[1],self.rotationspunkt[2])
        #Rotation um die Sonne
        self.rotationswinkel = (self.rotationswinkel + self.rotationsgeschwindigkeit[0])%360
        glRotatef(self.rotationswinkel,self.rotationsrichtung[0],self.rotationsrichtung[1],self.rotationsrichtung[2])

        #Erde positionieren
        glTranslatef(self.position[0],self.position[1],self.position[2])
        #Rotation um sich selbst
        self.eigenrotationswinkel = (self.eigenrotationswinkel + self.rotationsgeschwindigkeit[1])%360
        glRotatef(self.rotationswinkel,self.rotationsrichtung[0],self.rotationsrichtung[1],self.rotationsrichtung[2])

        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, self.textur_planet)
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

    def getGeschwindigkeit(self):
        return self.rotationsgeschwindigkeit

    def setGeschwindigkeit(self, geschwindigkeit):
        self.rotationsgeschwindigkeit = geschwindigkeit
        #print(self.rotationsgeschwindigkeit)

    def setGeschwindigkeitsfaktor(self,geschwindigkeit):
        self.rotationsgeschwindigkeit[0] = round(self.rotationsurgeschwindigkeit[0] * geschwindigkeit,3)
        self.rotationsgeschwindigkeit[1] = round(self.rotationsurgeschwindigkeit[1] * geschwindigkeit,3)