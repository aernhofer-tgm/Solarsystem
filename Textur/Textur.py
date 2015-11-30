__author__ = 'jakubkopec'
"""
Ladet die Texturen
"""
from PIL.Image import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Textur(object):

    def __init__(self):
        pass

    def getPfad(art):
        if(art=="sonne"):
            return "../texturen/sun.gif"
        elif(art=="erde"):
            return "../texturen/erde2.jpg"
        elif(art=="mars"):
            return "../texturen/mars2.jpg"
        elif(art=="mond"):
            return "../texturen/mond.jpg"

    def laden(dateipfad):
        if type(dateipfad) is str:
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
        else:
            raise TypeError("Der Parameter ist nicht vom Datentyp 'String' !")