__author__ = 'jakubkopec'
"""
Stern Interface
------------------------------------------------------------------------------------------
Interface für alle Sterne.
"""
from abc import ABCMeta, abstractmethod

class Stern(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self,groesse,position,drehrichtung,drehgeschwindigkeit,textur):
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

    @abstractmethod
    def addPlanet(self):
        pass