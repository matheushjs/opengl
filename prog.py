from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0, 0, 0, 0)

def timer(value):
    display()
    
    glutTimerFunc(3000, timer, 0)

def drawFractal(xmin=-0.5, xmax=0.5, ymin=-0.5, ymax=0.5, zmin=-0.5, zmax=0.5, levels=1):
    print("Called with: ", levels)

    if levels == 0:
        # Desenhamos o cubo
        glTranslatef( (xmax+xmin)/2 , (ymax+ymin)/2 , (zmax+zmin)/2 )
        glColor3f(1,1,1)
        glutWireCube( (xmax-xmin) ) 
        glTranslatef( -(xmax+xmin)/2 , -(ymax+ymin)/2 , -(zmax+zmin)/2 )
    else:
        sx = (xmax - xmin)/3
        sy = (ymax - ymin)/3
        sz = (zmax - zmin)/3
        
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if (i, j, k) == (1, 1, 1):
                        continue
                    drawFractal(xmin+i*sx, xmin+(i+1)*sx, ymin+j*sy, ymin+(j+1)*sy, zmin+k*sz, zmin+(k+1)*sz, levels-1)

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

    drawFractal()

    glFlush()


if __name__ == '__main__':   
    glutInit()
    glutInitWindowSize(800, 800)
    glutCreateWindow("Exercicio Extra")

    init()
    timer(0)

    glutMainLoop()
