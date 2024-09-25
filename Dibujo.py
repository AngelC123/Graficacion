import cv2
import numpy as np

class Dibujo:
    window = "Mi Ventana"
    def __init__(self, ancho=640, alto=480):
        self.frame = np.full((alto, ancho, 3), (255, 255, 255), dtype=np.uint8)

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
        sx = 1 if dx > 0 else -1
        sy = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            err = dx / 2.0
            while x != x2:
                self.punto(x, y, color)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y2:
                self.punto(x, y, color)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy

    def circunferencia(self, x, y, r, color=(0, 0, 0)):
        for i in range(0, 361):
            x2 = int(x + r * np.cos(i))
            y2 = int(y + r * np.sin(i))
            self.punto(x2, y2, color)

    def getPunto(self, x, y):
        if x > 640 or y > 480 or x < 0 or y < 0:
            return
        resultado = (self.frame[y, x, 0], self.frame[y, x, 1], self.frame[y, x, 2])
        return resultado

    def rellenar(self, x, y, color=(0, 0, 0)):
        color_actual = self.frame[y, x].tolist()
        if color_actual == self.getPunto(x, y):
            return
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if self.frame[y, x].tolist() != color_actual:
                continue
            self.punto(x, y, color)
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

    def mostrar(self):
        cv2.imshow(self.window, self.frame)
        cv2.waitKey(0)

'''
a = Dibujo()
a.linea(100, 100, 200, 200)
a.caja(200, 200, 100, 100)
a.mostrar()
cv2.destroyAllWindows()
'''

ROJO = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL = (255, 0, 0)
AMARILLO = (0, 255, 255)
CAFE = (1, 46, 70)
PURPURA = (240, 32, 160)
TERRACOTA = (36, 88, 196)
ROSA = (138, 31, 217)
CELESTE = (217, 169, 31)

casa = Dibujo()
casa.caja(200, 200, 300, 100) # Fachada
casa.linea(200, 200, 100, 200) # Tejado 1
casa.linea(500, 200, 600, 200) # Tejado 2
casa.linea(100, 200, 350, 100) # Tejado 3
casa.linea(350, 100, 600, 200) # Tejado 4
casa.caja(330, 220, 50, 80) # Puerta
casa.caja(250, 220, 50, 50) # Ventana izquierda
casa.linea(250, 245, 300, 245) # Marco Horizontal ventana izquierda
casa.linea(275, 220, 275, 270) # Marco Vertical ventana izquierda
casa.caja(410, 220, 50, 50) # Ventana derecha
casa.linea(410, 245, 460, 245)
casa.linea(435, 220, 435, 270)
casa.circunferencia(365, 260, 5)

casa.rellenar(340, 240, CAFE)
casa.rellenar(364, 258, AMARILLO)
casa.rellenar(325, 162, TERRACOTA)
casa.rellenar(226, 234, AMARILLO)
casa.rellenar(263, 234, ROSA)
casa.rellenar(444, 233, ROSA)
casa.rellenar(287, 254, PURPURA)
casa.rellenar(424, 254, PURPURA)
casa.rellenar(283, 234, CELESTE)
casa.rellenar(261, 261, CELESTE)
casa.rellenar(429, 231, CELESTE)
casa.rellenar(444, 251, CELESTE)

'''
casa.circunferencia(425, 100, 15)
casa.cajaRellena(425, 100-15, 30, 30, (255, 255, 255))
casa.circunferencia(425, 100-30, 15)
casa.cajaRellena(395, 70-15, 30, 30, (255, 255, 255))
casa.circunferencia(425, 100-60, 15)
casa.cajaRellena(425, 25, 30, 30, (255, 255, 255))
'''

casa.mostrar()
