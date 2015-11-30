__author__ = 'jakubkopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

from OpenGL.GL import *
from OpenGL.GLU import *

from Textur.Textur import Textur

class Erde(Planet):

    def __init__(self, groesse = 1,rotationspunkt=[0,0,0], position = [5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-10,-1.5], textur = "erde" ):
        self.rotationswinkel = 1
        self.eigenrotationswinkel = 1
        self.groesse = groesse
        self.rotationsrichtung = rotationsrichtung
        self.rotationsgeschwindigkeit = rotationsgeschwindigkeit
        self.textur = textur
        self.position = position
        self.rotationspunkt = rotationspunkt