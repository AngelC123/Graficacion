import cv2
import numpy as np

class Dibujo:
    window = "Mi Ventana"
    def __init__(self, ancho=640, alto=480):
        self.frame = np.full((ancho, alto, 3), (255, 255, 255), dtype=np.uint8)

    def punto(self, x, y, color=(0, 0, 0)):
        self.frame[y, x] = color

    def caja(self, x, y, ancho, alto, color=(0, 0, 0)):
        for i in range(ancho):
            self.punto(x + i, y, color)
            self.punto(x + i, y + alto, color)
        for i in range(alto):
            self.punto(x, y + i, color)
            self.punto(x + ancho, y + i, color)

    def cajaRellena(self, x, y, ancho, alto, color=(0, 0, 0)):
        for r in range(alto):
            for c in range(ancho):
                self.punto(x + c, y + r, color)

    def linea(self, x, y, x2, y2, color=(0, 0, 0)):
        dx = x2 - x
        dy = y2 - y
        mayor = max(abs(dx), abs(dy))
        # if dx >= dy:
        #    mayor = dx
        sumx = dx / mayor
        sumy = dy / mayor
        xc = x
        yc = y
        for j in range(mayor):
            self.punto(int(xc), int(yc), color)
            xc = xc + sumx
            yc = yc + sumy

    def circunferencia(self, x, y, r, color=(0, 0, 0)):
        for i in range(0, 361):
            x2 = int(y + r * np.cos(i))
            y2 = int(x + r * np.sin(i))
            self.punto(x2, y2, color)

    def mostrar(self):
        cv2.imshow(self.window, self.frame)
        cv2.destroyAllWindows()