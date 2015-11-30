__author__ = 'jakubkopec'
"""
Mars
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften vom Mars festgelegt werden.
"""
from FactoryPattern.Planet import Planet

from OpenGL.GL import *
from OpenGL.GLU import *

from Textur.Textur import Textur

class Mars(Planet):

    def __init__(self, groesse = 0.8, position = [9,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-1.3,-2], textur = "mars" ):
        self.rotationswinkel = 1
        self.eigenrotationswinkel=1
        self.groesse = groesse
        self.rotationsrichtung = rotationsrichtung
        self.rotationsgeschwindigkeit = rotationsgeschwindigkeit
        self.textur = textur
        self.position = position