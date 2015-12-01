__author__ = 'jakubkopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Uranus(Planet):

    def __init__(self,groesse = 1, rotationswinkel=[140,1],rotationspunkt=[0,0,0], position = [21,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-0.8,-1.5], textur = "uranus" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)