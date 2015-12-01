__author__ = 'jakubkopec'
"""
Erdmond
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften vom Erdmond festgelegt werden.
"""
from FactoryPattern.Mond import Mond

class Erdmond(Mond):

    def __init__(self, groesse = 0.3, rotationswinkel = [1,1,1], position = [1.5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-15,-10], textur = "mond" ):
        super().__init__(groesse,rotationswinkel,position,rotationsrichtung, rotationsgeschwindigkeit, textur)
