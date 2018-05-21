from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0, 0, 0, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Definimos o viewport
    glViewport(0, 0, 800, 800)

    # Trocamos a projecao
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0, 100)

    # Definimos o ponto de visão e rotacionamos o objeto
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
    glRotatef(90, 1, 1, 1)

    glTranslatef(-0.9, -0.9, 0);
    glutWireCube(0.1) 

    glFlush()


if __name__ == '__main__':   
    glutInit()
    glutInitWindowSize(800, 800)
    glutCreateWindow("Trab 2")

    init()
    glutDisplayFunc(display)

    glutMainLoop()
