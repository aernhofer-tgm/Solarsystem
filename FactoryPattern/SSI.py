__author__ = 'Andreas Ernhofer, Jakub Kopec'
"""
Solarsystem Interface
------------------------------------------------------------------------------------------
Interfaces sind in Python unnötig weil Mehrfachvererbung möglich ist, aber wenn man
unbedingt möchte kann man abstrakte Klassen mit selbiger funktionalität bauen.
"""
from abc import ABCMeta, abstractmethod

class SSI(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def zeichnen(self):
        pass
