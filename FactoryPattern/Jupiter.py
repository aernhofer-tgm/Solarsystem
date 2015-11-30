__author__ = 'jakubkopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Jupiter(Planet):

    def __init__(self,groesse = 2, rotationswinkel=[1,1],rotationspunkt=[0,0,0], position = [13.5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-2,-1.5], textur = "jupiter" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)