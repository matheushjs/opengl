from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sqrt

def init():
    glClearColor(0, 0, 0, 0)

def display():
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

    glTranslatef(-0.666, 0.666, 0)
    glutWireCube(0.4)

    glTranslatef(0.666, 0, 0)
    glutWireSphere(0.2, 10, 10)

    glTranslatef(0.666, 0, 0)
    glutWireCone(0.2, 0.2, 10, 10)

    glTranslatef(0, -0.666, 0)
    glutWireTorus(0.05, 0.2, 10, 10)

    glTranslatef(-0.666, 0, 0)
    size = 0.2
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glutWireDodecahedron()
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(-0.666, 0, 0)
    size = 0.3
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glutWireOctahedron()
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(0, -0.666, 0)
    size = 0.3
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glutWireTetrahedron()
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(0.666, 0, 0)
    size = 0.3
    glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
    glutWireIcosahedron()
    glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)

    glTranslatef(0.666, 0, 0)
    glutWireTeapot(0.1)

    glFlush()


if __name__ == '__main__':   
    glutInit()
    glutInitWindowSize(800, 800)
    glutCreateWindow("Trab 2")

    init()
    glutDisplayFunc(display)

    glutMainLoop()
