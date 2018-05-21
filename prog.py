from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sqrt

anglex = 30
angley = 30
anglez = 30

zoom   = 1

padx   = 0
pady   = 0


def init():
    glClearColor(1, 1, 1, 0)


def keyPressEvent(key, x, y) :
    global anglex, angley, anglez, zoom, padx, pady

    key = key.decode('ascii')

    if key == '\x1b':
        exit(0)

    elif key == 'w':
        anglex += 1
    elif key == 'a':
        angley -= 1
    elif key == 's':
        anglex -= 1
    elif key == 'd':
        angley += 1

    elif key == 'e':
        anglex += 180
        angley += 180
        anglez += 180

    elif key == 'z':
        zoom = max(0.1, zoom - 0.1)
    elif key == 'x':
        zoom = min(10, zoom + 0.1)

    elif key == 'i':
        pady += 0.1
    elif key == 'j':
        padx -= 0.1
    elif key == 'k':
        pady -= 0.1
    elif key == 'l':
        padx += 0.1


    anglex = (anglex + 720) % 360
    angley = (angley + 720) % 360
    anglez = (anglez + 720) % 360

    glutSetWindowTitle('Angle: ({}, {}, {})'.format(anglex, angley, anglez));
    display()


def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)

    # Definimos o viewport
    glViewport(0, 0, 800, 800)

    # Trocamos a projecao
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, 0, 100)

    # Definimos o ponto de visão
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)

    # Definimos cor
    glColor3f(0, 0, 0)
    
    # Adicionamos o padding
    glTranslatef(padx, pady, 0)


    glTranslatef(-0.666, 0.666, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireCube(0.4)
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(0.666, 0, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireSphere(0.2, 10, 10)
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(0.666, 0, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireCone(0.2, 0.2, 10, 10)
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(0, -0.666, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireTorus(0.05, 0.2, 10, 10)
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(-0.666, 0, 0)
    size = 0.2
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireDodecahedron()
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(-0.666, 0, 0)
    size = 0.3
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireOctahedron()
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(0, -0.666, 0)
    size = 0.3
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireTetrahedron()
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(0.666, 0, 0)
    size = 0.3
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireIcosahedron()
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(0.666, 0, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    glutWireTeapot(0.1)
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glFlush()


if __name__ == '__main__':   
    glutInit()
    glutInitWindowSize(800, 800)
    glutCreateWindow("Trab 2")

    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressEvent)

    glutMainLoop()
