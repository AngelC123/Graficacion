import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dibujar_cubo():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    vertices = [
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5],
        [0.5, -0.5, 0.5],
        [-0.5, -0.5, 0.5]
    ]

    caras = [
        [0, 1, 2, 3],
        [5, 4, 3, 2],
        [0, 3, 4, 7],
        [0, 7, 6, 1],
        [4, 5, 6, 7],
        [6, 5, 2, 1]
    ]

    colores = [
        (1.0, 1.0, 1.0),
        (1.0, 0.0, 1.0),
        (0.0, 1.0, 0.0),
        (0.0, 1.0, 1.0),
        (0.0, 0.0, 1.0),
        (1.0, 0.0, 0.0)
    ]

    glBegin(GL_QUADS)
    i = 0
    for i, cara in enumerate(caras):
        glColor3f(*colores[i])
        for v in cara:
            glVertex3fv(vertices[v])
    glEnd()
    glFlush()

def actualizar():
    glRotatef(0.1, -1, 1, 1)
    dibujar_cubo()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow("Cubo Rotatorio")

glRotatef(45, -1, 1, 0)
glutDisplayFunc(dibujar_cubo)
glutIdleFunc(actualizar)

glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

glutMainLoop()