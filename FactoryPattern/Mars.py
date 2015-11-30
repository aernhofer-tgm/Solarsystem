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

    def __init__(self, groesse = 0.8, rotationswinkel=[1,1],rotationspunkt=[0,0,0], position = [9,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-1.3,-2], textur = "mars" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)