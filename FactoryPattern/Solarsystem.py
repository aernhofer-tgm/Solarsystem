from FactoryPattern.Merkur import Merkur
from FactoryPattern.Sonne import Sonne
from FactoryPattern.Venus import Venus
from FactoryPattern.Erde import Erde
from FactoryPattern.Erdmond import Erdmond
from FactoryPattern.Jupiter import Jupiter
from FactoryPattern.Mars import Mars
from FactoryPattern.Neptun import Neptun
from FactoryPattern.Saturn import Saturn
from FactoryPattern.Uranus import Uranus

from OpenGL.GL import *

from math import *

__author__ = 'Andreas Ernhofer, Jakub Kopec'
"""
Solarsystem
------------------------------------------------------------------------------------------
Wenn man von einer abstrakten Klasse erbt, dann muss man die abstracten Methoden
überschreiben!
"""
from FactoryPattern.SSI import SSI

class Solarsystem(SSI):

    def __init__(self):

        self.sonne = Sonne()
        self.merkur = Merkur()
        self.venus = Venus()
        self.erde = Erde()
        self.erdmond = Erdmond()
        self.erdmond.setStern(self.sonne.getPosition())
        self.erdmond.setPlanet(self.erde.getPosition())
        self.erdmond.setPlanetGeschwindigkeit(self.erde.getRotationsgeschwindigkeit())
        self.mars = Mars()
        self.jupiter = Jupiter()
        self.saturn = Saturn()
        self.uranus = Uranus()
        self.neptun = Neptun()

        self.planeten = []
        self.planeten.append(self.merkur)
        self.planeten.append(self.venus)
        self.planeten.append(self.erde)
        self.planeten.append(self.mars)
        self.planeten.append(self.jupiter)
        self.planeten.append(self.saturn)
        self.planeten.append(self.uranus)
        self.planeten.append(self.neptun)

        #Um die Sonne drehen lassen
        for planet in self.planeten:
            planet.setRotationspunkt(self.sonne.getPosition())

        self.geschwindigkeit = 1

        self.geschwindigkeit_alt = 1


    """
    Zeichnet das Solarsystem.
    """
    def zeichnen(self):

        #den Bildschirm loeschen
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #macht alles schoen
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)

        #Objekte zeichnen
        self.sonne.zeichnen()
        self.erdmond.zeichnen()
        for planet in self.planeten:
            planet.zeichnen()

    def updateSpeed(self,faktor):

        self.geschwindigkeit = round(self.geschwindigkeit+faktor,1)

        self.sonne.setGeschwindigkeitsfaktor(self.geschwindigkeit)

        for planet in self.planeten:
            planet.setGeschwindigkeitsfaktor(self.geschwindigkeit)

        self.erdmond.setPlanetGeschwindigkeit(self.erde.getRotationsgeschwindigkeit())
        self.erdmond.setGeschwindigkeitsfaktor(self.geschwindigkeit)

    def disableTexture(self):
        glDisable(GL_TEXTURE_2D)

    def enableTexture(self):
        glEnable(GL_TEXTURE_2D)

    def pause(self, switch):

        if switch:
            self.geschwindigkeit_alt = self.geschwindigkeit
            self.geschwindigkeit = 0
            self.updateSpeed(0)
        else:
            self.geschwindigkeit = self.geschwindigkeit_alt
            self.updateSpeed(0)

    def achsenZeichnen(self):
        glLoadIdentity()
        #Rote Achse -- X-Achse
        glLineWidth(2.5)
        glColor3f(1, 0, 0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(100, 0, 0)
        glEnd()

        glLoadIdentity()
        #Gruene Achse -- Y-Achse
        glLineWidth(2.5)
        glColor3f(1, 1, 0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 100, 0)
        glEnd()

        glLoadIdentity()
        #Weisse Achse -- Z-Achse
        glLineWidth(2.5)
        glColor3f(1, 1, 1)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 100)
        glEnd()

    def bahnenZeichnen(self):

        for planet in self.planeten:
            self.bahnZeichnen(planet.getPosition()[0])

    def bahnZeichnen(self,radius):
        posx, posy = 0,0
        sides = 200
        glBegin(GL_LINE_LOOP)
        for i in range(1000):
            cosine= radius * cos(i*2*pi/sides) + posx
            sine  = radius * sin(i*2*pi/sides) + posy
            glVertex3f(cosine,sine,0)
        glEnd()