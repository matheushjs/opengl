from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

if __name__ == '__main__':   
    glutInit()
    glutInitWindowSize(400, 400)
    glutCreateWindow("Hello World!")

    glClearColor(0.3, 0.3, 0.3, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

    glutMainLoop()
