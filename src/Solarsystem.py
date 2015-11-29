__author__ = 'Jakub Kopec'

from astronomisches_objekt import *
from textur import *

class Solarsystem(object):

    global sonne,erde,mars,mond

    def __init__(self):
        self.sonne = 1
        self.erde = 1
        self.mars = 1
        self.mond = 1
        pass

    def zeichnen(self):

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #draw something pretty
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)

        glLoadIdentity()
        glTranslatef(0, 0.0, 0)
        self.sonne = self.sonne - 1
        glRotatef(self.sonne,0,1,0)
        #Textur laden
        textur_sonne = Textur.laden("../texturen/sun.gif")
        #Erde zeichnen
        AstronomischesObjekt.sonne(textur_sonne)

        glLoadIdentity()
        self.erde = self.erde - 1
        #drehung um die sonne
        glRotatef(self.erde,0,1,0)
        glTranslatef(5.0, 0.0, 0)
        #Eigenrotation
        glRotatef(self.erde,0,1,0)
        #Textur laden
        textur_erde = Textur.laden("../texturen/erde.jpg")
        #Erde zeichnen
        AstronomischesObjekt.erde(textur_erde)

        glLoadIdentity()
        self.mars = self.mars - 5
        #drehung um die sonne
        glRotatef(self.mars,0,1,0)
        glTranslatef(10.0, 0.0, 0)
        #Eigenrotation
        glRotatef(self.mars,0,1,0)
        #Textur laden
        textur_mars = Textur.laden("../texturen/mars.jpg")
        #Mars zeichnen
        AstronomischesObjekt.mars(textur_mars)


        """
        Monde
        """
        glLoadIdentity()
        self.mond = self.mond - 3
        #drehung um die sonne
        glRotatef(self.erde,0,1,0)
        glTranslatef(5.0, 0.0, 0)
        #Drehung um die Erde
        glRotatef(self.mond,0,1,0)
        glTranslatef(2.0, 0.0, 0)
        #Eigenrotation
        glRotatef(self.mond,0,1,0)
        #Textur laden
        textur_mond = Textur.laden("../texturen/mond.jpg")
        #Erde zeichnen
        AstronomischesObjekt.mond(textur_mond)

