__author__ = 'Andreas Ernhofer, Jakub Kopec'
"""
Ladet die Texturen
"""
from PIL.Image import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Textur(object):

    def laden(dateiname):

        dateipfad = "../texturen/"+dateiname+".jpg"

        try:
            image = open(dateipfad)

            x = image.size[0]
            y = image.size[1]

            image = image.convert("RGBA").tobytes("raw", "RGBA")
            textur = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D,textur)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
            gluBuild2DMipmaps(GL_TEXTURE_2D, 3, x, y, GL_RGBA, GL_UNSIGNED_BYTE, image)

            glEnable(GL_TEXTURE_2D)

            return textur
        except:
            raise FileNotFoundError("Textur konnte nicht geladen werden")
