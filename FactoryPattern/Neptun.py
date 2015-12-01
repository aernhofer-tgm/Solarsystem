__author__ = 'jakubkopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Neptun(Planet):

    def __init__(self,groesse = 1, rotationswinkel=[300,1],rotationspunkt=[0,0,0], position = [23,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-2.4,-1.5], textur = "neptun" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)