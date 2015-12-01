__author__ = 'jakubkopec'
"""
Stern Interface
------------------------------------------------------------------------------------------
Interface für alle Sterne.
"""
from abc import ABCMeta, abstractmethod
from OpenGL.GL import *
from OpenGL.GLU import *
from Textur.Textur import Textur

class Stern(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self,groesse,position,drehrichtung,drehgeschwindigkeit,textur):
        self.winkel = 1
        self.groesse = groesse
        self.drehrichtung = drehrichtung
        self.drehurgeschwindigkeit = drehgeschwindigkeit
        self.drehgeschwindigkeit = drehgeschwindigkeit
        self.textur = textur
        self.position = position
        #Textur laden
        self.textur_stern = Textur.laden(Textur.getPfad(self.textur))

    def zeichnen(self):

        #matrix zuruecksetzen
        glLoadIdentity()

        #Sonne positionieren
        glTranslatef(self.position[0],self.position[1],self.position[2])

        self.winkel = self.winkel + self.drehgeschwindigkeit

        glRotatef(self.winkel,self.drehrichtung[0],self.drehrichtung[1],self.drehrichtung[2])


        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, self.textur_stern)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        gluSphere(quadratic,self.groesse,50,50)

    def getPosition(self):
        return self.position


    def setGeschwindigkeitsfaktor(self,geschwindigkeit):
        self.drehgeschwindigkeit = self.drehurgeschwindigkeit*geschwindigkeit

    def getGeschwindigkeit(self):
        return self.drehgeschwindigkeit

    def setGeschwindigkeit(self,geschwindigkeit):
        self.drehgeschwindigkeit = geschwindigkeit