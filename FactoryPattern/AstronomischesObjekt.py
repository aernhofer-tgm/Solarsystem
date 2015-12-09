from FactoryPattern.SSI import SSI
from abc import ABCMeta, abstractmethod

__author__ = 'Andreas Ernhofer, Jakub Kopec'

"""
Astronomisches Objekt
------------------------------------------------------------------------------------------
Das kann entweder ein Stern, ein Planet oder ein Mond sein.
"""

class AstronomischesObjekt(object):

    @abstractmethod
    def zeichnen(self):
        pass