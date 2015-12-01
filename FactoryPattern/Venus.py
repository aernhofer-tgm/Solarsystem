__author__ = 'jakubkopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Venus(Planet):

    def __init__(self,groesse = 1, rotationswinkel=[264,1],rotationspunkt=[0,0,0], position = [5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-2.4,-1.5], textur = "venus" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)