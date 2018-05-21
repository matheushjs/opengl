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

objectNum = 0


def init():
    glClearColor(1, 1, 1, 0)


def keyPressEvent(key, x, y) :
    global anglex, angley, anglez, zoom, padx, pady, objectNum

    key = key.decode('ascii')

    if key == '\x1b':
        exit(0)

    elif key == 'w':
        anglex += 3
    elif key == 'a':
        angley -= 3
    elif key == 's':
        anglex -= 3
    elif key == 'd':
        angley += 3

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

    elif key == 'n':
        objectNum += 1


    anglex = (anglex + 720) % 360
    angley = (angley + 720) % 360
    anglez = (anglez + 720) % 360
    objectNum = objectNum % 9

    glutSetWindowTitle('Angle: ({}, {}, {}); Zoom: {}; Padding: ({}, {}); Object: {}'.format(anglex, angley, anglez, zoom, padx, pady, objectNum));
    display()

def drawObject():
    if objectNum == 0:
        glutWireCube(0.4)
    elif objectNum == 1:
        glutWireSphere(0.2, 10, 10)
    elif objectNum == 2:
        glutWireCone(0.2, 0.2, 10, 10)
    elif objectNum == 3:
        glutWireTorus(0.05, 0.2, 10, 10)
    elif objectNum == 4:
        size = 0.2
        glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
        glutWireDodecahedron()
        glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)
    elif objectNum == 5:
        size = 0.3
        glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
        glutWireOctahedron()
        glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)
    elif objectNum == 6:
        size = 0.3
        glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
        glutWireTetrahedron()
        glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)
    elif objectNum == 7:
        size = 0.3
        glScale(size/sqrt(3), size/sqrt(3), size/sqrt(3))
        glutWireIcosahedron()
        glScale(sqrt(3)/size, sqrt(3)/size, sqrt(3)/size)
    elif objectNum == 8:
        glutWireTeapot(0.1)

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

    glRotate(anglex, 1, 0, 0)
    glRotate(angley, 0, 1, 0)
    glRotate(anglez, 0, 0, 1)
    glScale(zoom, zoom, zoom)
    drawObject()
    glScale(1/zoom, 1/zoom, 1/zoom)
    glRotate(-anglez, 0, 0, 1)
    glRotate(-angley, 0, 1, 0)
    glRotate(-anglex, 1, 0, 0)

    glFlush()


if __name__ == '__main__':   
    print(
"""Atenção para o modo de uso!!!

  TECLAS     ====>      FUNÇÃO
  ------                ------
    W
A   S   D    ====> Alteração do ângulo

    I
J   K   L    ====> Translação no plano XY

   Z X       ====> Alteração do zoom

    N        ====> Alteração da profundidade
    
    E        ====> Espelhamento""")


    print("\n")
    print("Pressione ENTER para iniciar\n")
    input()


    glutInit()
    glutInitWindowSize(800, 800)
    glutCreateWindow("Trab 2")

    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressEvent)

    glutMainLoop()
