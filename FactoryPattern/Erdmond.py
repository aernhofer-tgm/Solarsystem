__author__ = 'jakubkopec'
"""
Erdmond
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften vom Erdmond festgelegt werden.
"""
from FactoryPattern.Mond import Mond

class Erdmond(Mond):

    def __init__(self, groesse = 0.3, position = [1.5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-30,-10], textur = "mond" ):
        self.rotationswinkel = 1
        self.planetrotationswinkel = 1
        self.eigenrotationswinkel=1
        self.groesse = groesse
        self.rotationsrichtung = rotationsrichtung
        self.rotationsgeschwindigkeit = rotationsgeschwindigkeit
        self.textur = textur
        self.position = position
