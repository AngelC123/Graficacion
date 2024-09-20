import cv2
import numpy as np

def punto(f, x, y, color = (0, 0, 0)):
    f[y, x] = color

def lineaDerecha(f, x, y, distancia, color = (0, 0, 0)):
    for i in range(0, distancia + 1):
        punto(f, x + i, y, color)

def lineaAbajo(f, x, y, distancia, color = (0, 0, 0)):
    for i in range(0, distancia + 1):
        punto(f, x, y + i, color)

def circunferencia(f, x, y, r, color = (0, 0, 0)):
    for i in range(0, 361):
        x2 = int(x + r * np.cos(i))
        y2 = int(y + r * np.sin(i))
        punto(f, x2, y2, color)

def caja(f, x, y, alto, ancho, color = (0, 0, 0)):
    for i in range(ancho):
        punto(f, x + i, y, color)
        punto(f, x + i, y + alto, color)
    for i in range(alto):
        punto(f, x, y + i, color)
        punto(f, x + ancho, y + i, color)

def cajaRellena(f, x, y, alto, ancho, color = (0, 0, 0)):
    for r in range(alto):
        for c in range(ancho):
            punto(f, x + c, y + r, color)

def linea(f, x, y, x2, y2, color = (0, 0, 0)):
    dx = x2 - x
    dy = y2 - y
    mayor = max(abs(dx), abs(dy))
    #if dx >= dy:
    #    mayor = dx
    sumx = dx / mayor
    sumy = dy / mayor
    xc = x
    yc = y
    for j in range(mayor):
        punto(f, int(xc), int(yc), color)
        xc = xc + sumx
        yc = yc + sumy

frame = np.full((600, 800, 3), (255, 255, 255), dtype=np.uint8)

color = (0, 0, 0)
rojo = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)
cyan = (255, 231, 4)

lineaDerecha(frame, 100, 100, 50, color)
lineaDerecha(frame, 100, 150, 50, color)
lineaAbajo(frame, 100, 100, 50, color)
lineaAbajo(frame, 150, 100, 50, color)

for a in range(0, 51):
    lineaDerecha(frame, 200, 200 + a, 50, color)

circunferencia(frame, 250, 100, 50, rojo)

caja(frame, 250, 250, 100, 50, rojo)
caja(frame, 10, 10, 400, 600, verde)

cajaRellena(frame, 180, 100, 80, 80, azul)

linea(frame, 10, 10, 610, 410, cyan)
linea(frame, 200, 50, 50, 80, azul)
'''
circulo(frame, 300, 300, 50, color)
'''

cv2.imshow("Ventana", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Investigar un algoritmo para dibujar lineas diagonales con valores negativos.
