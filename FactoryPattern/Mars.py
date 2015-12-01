__author__ = 'jakubkopec'
"""
Mars
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften vom Mars festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Mars(Planet):

    def __init__(self, groesse = 0.8, rotationswinkel=[262,1],rotationspunkt=[0,0,0], position = [10.5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-1.1,-2], textur = "mars" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)