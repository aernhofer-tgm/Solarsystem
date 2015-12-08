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

__author__ = 'jakubkopec'
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
        self.merkur.setRotationspunkt(self.sonne.getPosition())

        self.venus = Venus()
        self.venus.setRotationspunkt(self.sonne.getPosition())

        self.erde = Erde()
        self.erde.setRotationspunkt(self.sonne.getPosition())

        self.erdmond = Erdmond()
        self.erdmond.setStern(self.sonne.getPosition())
        self.erdmond.setPlanet(self.erde.getPosition())
        self.erdmond.setPlanetGeschwindigkeit(self.erde.getRotationsgeschwindigkeit())

        self.mars = Mars()
        self.mars.setRotationspunkt(self.sonne.getPosition())

        self.jupiter = Jupiter()
        self.jupiter.setRotationspunkt(self.sonne.getPosition())

        self.saturn = Saturn()
        self.saturn.setRotationspunkt(self.sonne.getPosition())

        self.uranus = Uranus()
        self.uranus.setRotationspunkt(self.sonne.getPosition())

        self.neptun = Neptun()
        self.neptun.setRotationspunkt(self.sonne.getPosition())

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
        self.merkur.zeichnen()
        self.venus.zeichnen()
        self.erde.zeichnen()
        self.erdmond.zeichnen()
        self.mars.zeichnen()
        self.jupiter.zeichnen()
        self.saturn.zeichnen()
        self.uranus.zeichnen()
        self.neptun.zeichnen()

    def updateSpeed(self,faktor):

        self.geschwindigkeit = round(self.geschwindigkeit+faktor,1)

        self.sonne.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.merkur.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.venus.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.erde.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.mars.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.jupiter.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.saturn.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.uranus.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.neptun.setGeschwindigkeitsfaktor(self.geschwindigkeit)
        self.erdmond.setPlanetGeschwindigkeit(self.erde.getRotationsgeschwindigkeit())
        self.erdmond.setGeschwindigkeitsfaktor(self.geschwindigkeit)

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
        self.bahnZeichnen(5)
        self.bahnZeichnen(7.5)
        self.bahnZeichnen(10.5)
        self.bahnZeichnen(13.5)
        self.bahnZeichnen(16.9)
        self.bahnZeichnen(21.5)
        self.bahnZeichnen(25)
        self.bahnZeichnen(27.5)

    def bahnZeichnen(self,radius):
        posx, posy = 0,0
        sides = 200
        glBegin(GL_LINE_LOOP)
        for i in range(1000):
            cosine= radius * cos(i*2*pi/sides) + posx
            sine  = radius * sin(i*2*pi/sides) + posy
            glVertex3f(cosine,sine,0)
        glEnd()