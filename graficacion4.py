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
        x2 = int(y + r * np.cos(i))
        y2 = int(x + r * np.sin(i))
        punto(f, x2, y2, color)

def circulo(f, x, y, r, color = (0, 0, 0)):
    for i in range(0, r + 1):
        circunferencia(f, x, y, i, color)

frame = np.full((500, 500, 3), (255, 255, 255), dtype=np.uint8)
color = (0, 0, 0)

lineaDerecha(frame, 100, 100, 50, color)
lineaDerecha(frame, 100, 150, 50, color)
lineaAbajo(frame, 100, 100, 50, color)
lineaAbajo(frame, 150, 100, 50, color)

for a in range(0, 51):
    lineaDerecha(frame, 200, 200 + a, 50, color)

circunferencia(frame, 250, 100, 50, color)

circulo(frame, 300, 300, 50, color)

cv2.imshow("Ventana", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()