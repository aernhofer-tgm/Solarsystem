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

class Venus(Planet):

    def __init__(self,groesse = 1, rotationswinkel=[1,1],rotationspunkt=[0,0,0], position = [5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-2,-1.5], textur = "venus" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)