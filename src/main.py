from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from FactoryPattern.Erde import Erde
from FactoryPattern.Erdmond import Erdmond
from FactoryPattern.Jupiter import Jupiter
from FactoryPattern.Mars import Mars
from FactoryPattern.Neptun import Neptun
from FactoryPattern.Saturn import Saturn
from FactoryPattern.Sonne import Sonne
from FactoryPattern.Uranus import Uranus
from FactoryPattern.Venus import Venus

name = 'ball_glut'
display_width = 1280
display_height = 720

#Config
topansicht = True
geschwindigkeit = 1

sonne = Sonne()
sonne.setGeschwindigkeitsfaktor(geschwindigkeit)

venus = Venus()
venus.setRotationspunkt(sonne.getPosition())
venus.setGeschwindigkeitsfaktor(geschwindigkeit)

erde = Erde()
erde.setRotationspunkt(sonne.getPosition())
erde.setGeschwindigkeitsfaktor(geschwindigkeit)

erdmond = Erdmond()
erdmond.setStern(sonne.getPosition())
erdmond.setPlanet(erde.getPosition())
erdmond.setPlanetGeschwindigkeit(erde.getRotationsgeschwindigkeit())
erdmond.setGeschwindigkeitsfaktor(geschwindigkeit)

mars = Mars()
mars.setRotationspunkt(sonne.getPosition())
mars.setGeschwindigkeitsfaktor(geschwindigkeit)

jupiter = Jupiter()
jupiter.setRotationspunkt(sonne.getPosition())
jupiter.setGeschwindigkeitsfaktor(geschwindigkeit)

saturn = Saturn()
saturn.setRotationspunkt(sonne.getPosition())
saturn.setGeschwindigkeitsfaktor(geschwindigkeit)

uranus = Uranus()
uranus.setRotationspunkt(sonne.getPosition())
uranus.setGeschwindigkeitsfaktor(geschwindigkeit)

neptun = Neptun()
neptun.setRotationspunkt(sonne.getPosition())
neptun.setGeschwindigkeitsfaktor(geschwindigkeit)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(display_width,display_height)
    glutCreateWindow( b"Solarsystem" )

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    """
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    """
    glutDisplayFunc(display)
    #set the perspective
    glViewport(0, 0, display_width, display_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()



    gluPerspective(45,(display_width/display_height),0.1,100)
    if topansicht:
        #Obenansicht
        gluLookAt(0, 0, 30, 0, 0, 0, 0, 1, 0)
    else:
        #Seitenansicht
        gluLookAt(0, 30, 0, 0, 0, 0, 0, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    while True:
        display()
    glutMainLoop()
    #return

def display():
    """
    #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glPushMatrix()
    #color = [1.0,0.,0.,1.]
    #glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    #glutSolidSphere(2,50,50)
    #glPopMatrix()
    glutSwapBuffers()
    #return
    """

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


    #Objekte zeichnen
    sonne.zeichnen()
    venus.zeichnen()
    erde.zeichnen()
    erdmond.zeichnen()
    mars.zeichnen()
    jupiter.zeichnen()
    saturn.zeichnen()
    uranus.zeichnen()
    neptun.zeichnen()


    glLoadIdentity()
    #Rote Achse -- X-Achse
    glLineWidth(2.5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(100, 0, 0)
    glEnd()

    glLoadIdentity()
    #Gruene Achse -- Y-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 100, 0)
    glEnd()

    glLoadIdentity()
    #Weisse Achse -- Z-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 100)
    glEnd()

    glutSwapBuffers()

main()

if name == '__main__': main()