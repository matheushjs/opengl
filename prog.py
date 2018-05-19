from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

angle  = 0
levels = 3
zoom   = 1


def init():
    # Inicialize para uso de coisas 3D
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH) 

    # Inicializa janela
    glutInitWindowSize(800, 800)
    glutCreateWindow("Exercicio Extra")

    # Habilita coisas que precisam ser habilitadas
    glEnable(GL_DEPTH_TEST) 
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    # Pinta plano de fundo de branco
    glClearColor(0.90, 0.90, 0.90, 0)

def keyPressEvent(key, x, y) :
    global angle, levels, zoom

    key = key.decode('ascii')

    if key == '\x1b':
        exit(0)

    elif key == 'q':
        angle -= 10
    elif key == 'w':
        angle -= 1
    elif key == 'e':
        angle += 1
    elif key == 'r':
        angle += 10

    elif key == 'a':
        zoom = max(zoom - 0.5, 0.1)
    elif key == 's':
        zoom = max(zoom - 0.1, 0.1)
    elif key == 'd':
        zoom += 0.1
    elif key == 'f':
        zoom += 0.5

    elif key == 'z':
        levels = (levels - 1 + 5)%5
    elif key == 'x':
        levels = (levels + 1)%5

    glutSetWindowTitle('Angle: {}, Zoom: {}, Levels: {}'.format(angle, zoom, levels));
    display()

def drawFractal(xmin=-0.5, xmax=0.5, ymin=-0.5, ymax=0.5, zmin=-0.5, zmax=0.5, levels=10):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0]);
    glMaterialfv(GL_FRONT, GL_EMISSION, [0.1, 0.1, 0.1]);

    if levels == 0:
        # Desenhamos o cubo
        glTranslatef( (xmax+xmin)/2 , (ymax+ymin)/2 , (zmax+zmin)/2 )
        glColor3f(0,0.6,0.6)
        glutSolidCube( (xmax-xmin) ) 
        glTranslatef( -(xmax+xmin)/2 , -(ymax+ymin)/2 , -(zmax+zmin)/2 )
    else:
        sx = (xmax - xmin)/3
        sy = (ymax - ymin)/3
        sz = (zmax - zmin)/3
        
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if (i, j) == (1, 1) or (i, k) == (1, 1) or (j, k) == (1, 1):
                        continue
                    drawFractal(xmin+i*sx, xmin+(i+1)*sx, ymin+j*sy, ymin+(j+1)*sy, zmin+k*sz, zmin+(k+1)*sz, levels-1)

def display():
    global angle, zoom, levels

    # Limpa o que tem que ser limpo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Definimos o viewport
    glViewport(0, 0, 800, 800)

    # Trocamos a projecao
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 100)
    # glOrtho(-2, 2, -2, 2, -2, 100)

    # Definimos o ponto de visão e rotacionamos o objeto
    glMatrixMode(GL_MODELVIEW)

    # Arruma luz e sombreamento
    light_position = [10.0, 10.0, -20.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);
    glShadeModel(GL_SMOOTH)

    glLoadIdentity()
    gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
    glRotatef(angle, 1, 1, 1)
    glScalef(zoom, zoom, zoom) 

    drawFractal(levels=levels)

    glFlush()


if __name__ == '__main__':   
    print(
"""Atenção para o modo de uso!!!

Teclas q, w, e, r  ====> Alteração do ângulo (teclas 'q' e 'r' mais rápidas)
Teclas a, s, d, f  ====> Alteração do zoom (teclas 'a' e 'f' mais rápidas)
Teclas z, x ===========> Alteração da profundidade

Profundidades permitidas: 0, 1, 2, 3, 4
Com 4 já fica lento.""")


    print("\n")
    print("Pressione ENTER para iniciar\n")
    input()

    glutInit()

    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressEvent)

    glutMainLoop()
