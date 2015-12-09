__author__ = 'Andreas Ernhofer, Jakub Kopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Saturn(Planet):

    def __init__(self,groesse = 1.8, rotationswinkel=[1,1],rotationspunkt=[0,0,0], position = [21.5,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-1.8,-1.5], textur = "saturn" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)