from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import sys

# Variables de control de rotación y textura
angulo_x, angulo_y = 0, 0
ultimo_x, ultimo_y = 0, 0
arrastrando = False
texture_id = None

def load_texture(image_path):
    global texture_id
    # Carga la imagen usando PIL
    image = Image.open(image_path)
    img_data = image.convert("RGBA").tobytes()

    # Genera una ID de textura en OpenGL
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Configuración de los parámetros de la textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Carga la imagen en la textura de OpenGL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)


def dibujar_cubo():
    global angulo_x, angulo_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Posiciona la cámara para ver el cubo desde una distancia adecuada
    glTranslatef(0.0, 0.0, -3.0)
    glRotatef(angulo_x, 1, 0, 0)
    glRotatef(angulo_y, 0, 1, 0)

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
        [3, 2, 5, 4],
        [4, 5, 6, 7],
        [7, 6, 1, 0],
        [1, 6, 5, 2],
        [4, 7, 0, 3]
    ]

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    for cara in caras:
        glTexCoord2f(0.0, 0.0);
        glVertex3fv(vertices[cara[0]])
        glTexCoord2f(1.0, 0.0);
        glVertex3fv(vertices[cara[1]])
        glTexCoord2f(1.0, 1.0);
        glVertex3fv(vertices[cara[2]])
        glTexCoord2f(0.0, 1.0);
        glVertex3fv(vertices[cara[3]])
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glutSwapBuffers()

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
        angulo_x += dy * 0.5
        angulo_y += dx * 0.5
        ultimo_x, ultimo_y = x, y
        glutPostRedisplay()

# Configuración de OpenGL y GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow("Cubo Texturizado")

glRotatef(45, -1, 1, 0)
glutDisplayFunc(dibujar_cubo)
glutMouseFunc(mouse_boton)
glutMotionFunc(mouse_mover)
load_texture("steve.png")

glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, 1.0, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

glutMainLoop()