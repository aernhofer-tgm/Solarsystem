from FactoryPattern.AstronomischesObjekt import AstronomischesObjekt

__author__ = 'jakubkopec'
"""
Mond Interface
------------------------------------------------------------------------------------------
Interface für alle Monde.
"""
from abc import ABCMeta, abstractmethod

from OpenGL.GL import *
from OpenGL.GLU import *

from Textur.Textur import Textur

class Mond(AstronomischesObjekt):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, groesse, rotationswinkel, position,rotationsrichtung,rotationsgeschwindigkeit,textur):
        self.rotationswinkel = rotationswinkel[0]
        self.planetrotationswinkel = rotationswinkel[1]
        self.eigenrotationswinkel = rotationswinkel[2]
        self.groesse = groesse
        self.rotationsrichtung = rotationsrichtung
        self.rotationsurgeschwindigkeit = rotationsgeschwindigkeit
        self.rotationsgeschwindigkeit = [1,1]
        self.rotationsgeschwindigkeit[0] = rotationsgeschwindigkeit[0]
        self.rotationsgeschwindigkeit[1] = rotationsgeschwindigkeit[1]
        self.textur = textur
        self.position = position
        #Textur laden
        self.textur_mond = Textur.laden(Textur.getPfad(self.textur))
        #self.stern = stern
        #self.planet = planet
        #self.planetgeschwindigkeit = planetgeschwindigkeit

    def zeichnen(self):

        #matrix zuruecksetzen
        glLoadIdentity()

        #Rotationspunkt festlegen
        glTranslatef(self.stern[0],self.stern[1],self.stern[2])

        #Rotation um die Sonne
        self.rotationswinkel = self.rotationswinkel + self.planetgeschwindigkeit
        glRotatef(self.rotationswinkel,self.rotationsrichtung[0],self.rotationsrichtung[1],self.rotationsrichtung[2])

        #zum Planeten positionieren
        glTranslatef(self.planet[0],self.planet[1],self.planet[2])
        self.planetrotationswinkel = self.planetrotationswinkel + self.rotationsgeschwindigkeit[0]
        glRotatef(self.planetrotationswinkel,self.rotationsrichtung[0],self.rotationsrichtung[1],self.rotationsrichtung[2])

        #Mond positionieren
        glTranslatef(self.position[0],self.position[1],self.position[2])

        #Rotation um sich selbst
        self.eigenrotationswinkel = self.eigenrotationswinkel + self.rotationsgeschwindigkeit[1]
        glRotatef(self.eigenrotationswinkel,self.rotationsrichtung[0],self.rotationsrichtung[1],self.rotationsrichtung[2])


        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, self.textur_mond)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        gluSphere(quadratic,self.groesse,50,50)

    def setStern(self,stern):
        self.stern = stern

    def setPlanet(self,planet):
        self.planet = planet

    def setPlanetGeschwindigkeit(self,planetgeschwindigkeit):
        self.planetgeschwindigkeit = planetgeschwindigkeit

    def setGeschwindigkeitsfaktor(self,geschwindigkeit):
        self.rotationsgeschwindigkeit[0] = round(self.rotationsurgeschwindigkeit[0] * geschwindigkeit,3)
        self.rotationsgeschwindigkeit[1] = round(self.rotationsurgeschwindigkeit[1] * geschwindigkeit,3)