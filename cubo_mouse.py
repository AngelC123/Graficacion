import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import sys

angulo_x, angulo_y = 0, 0
ultimo_x, ultimo_y = 0, 0
arrastrando = False

def dibujar_cubo():
    global angulo_x, angulo_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(angulo_x, 1, 0, 0)
    glRotatef(angulo_y, 0, 1, 0)
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

def mouse_boton(boton, estado, x, y):
    global arrastrando, ultimo_x, ultimo_y
    if boton == GLUT_LEFT_BUTTON:
        arrastrando = True
        ultimo_x, ultimo_y = x, y
    elif estado == GLUT_UP:
        arrastrando = False

def mouse_mover(x, y):
    global angulo_x, angulo_y, ultimo_x, ultimo_y
    if arrastrando:
        dx = x - ultimo_x
        dy = y - ultimo_y
        angulo_x += dy * -0.5
        angulo_y += dx * -0.5
        ultimo_x, ultimo_y = x, y
        glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow("Cubo Interactivo")

glRotatef(45, -1, 1, 0)
glutDisplayFunc(dibujar_cubo)
glutMouseFunc(mouse_boton)
glutMotionFunc(mouse_mover)

glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

glutMainLoop()