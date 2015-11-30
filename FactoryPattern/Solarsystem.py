__author__ = 'jakubkopec'
"""
Solarsystem
------------------------------------------------------------------------------------------
Wenn man von einer abstrakten Klasse erbt, dann muss man die abstracten Methoden
überschreiben!
"""
from FactoryPattern.SSI import SSI

class Solarsystem(object,SSI):

    """
    Zeichnet das Solarsystem.
    """
    def zeichnen(self):

        #den Bildschirm loeschen
        paglClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #macht alles schoen
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
