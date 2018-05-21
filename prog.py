from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sqrt

anglex = 30
angley = 30
anglez = 30

def init():
    glClearColor(1, 1, 1, 0)


def keyPressEvent(key, x, y) :
    global anglex, angley, anglez

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

    glTranslatef(-0.666, 0.666, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glutWireCube(0.4)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(0.666, 0, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glutWireSphere(0.2, 10, 10)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(0.666, 0, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glutWireCone(0.2, 0.2, 10, 10)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(0, -0.666, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glutWireTorus(0.05, 0.2, 10, 10)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glTranslatef(-0.666, 0, 0)
    size = 0.2
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glutWireDodecahedron()
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
    glutWireOctahedron()
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
    glutWireTetrahedron()
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
    glutWireIcosahedron()
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(0.666, 0, 0)
    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glutWireTeapot(0.1)
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
