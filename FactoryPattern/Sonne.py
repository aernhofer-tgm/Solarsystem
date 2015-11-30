__author__ = 'jakubkopec'
"""
Sonne
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Sonne festgelegt werden.
"""
from FactoryPattern.Stern import Stern

from OpenGL.GL import *
from OpenGL.GLU import *

from Textur.Textur import Textur

class Sonne(Stern):

    def __init__(self, groesse = 3, position = [0,0,0],drehrichtung = [0,0,1],drehgeschwindigkeit = -0.3, textur = "sonne" ):
        self.sonne = 1
        self.groesse = groesse
        self.drehrichtung = drehrichtung
        self.drehgeschwindigkeit = drehgeschwindigkeit
        self.textur = textur
        self.position = position

    def zeichnen(self):

        #matrix zuruecksetzen
        glLoadIdentity()

        #Sonne positionieren
        glTranslatef(self.position[0],self.position[1],self.position[2])

        self.sonne = self.sonne + self.drehgeschwindigkeit

        glRotatef(self.sonne,self.drehrichtung[0],self.drehrichtung[1],self.drehrichtung[2])

        #Textur laden
        textur_sonne = Textur.laden(Textur.getPfad(self.textur))

        #Textur uebernehmen
        glBindTexture(GL_TEXTURE_2D, textur_sonne)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)

        #die eigentliche Form
        gluSphere(quadratic,self.groesse,50,50)

    def getPosition(self):
        return self.position