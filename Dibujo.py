import cv2
import numpy as np
import struct
import os

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

    def guarda(self, archivo):
        if os.path.exists(archivo):
            print("El Archivo ya existe")
        else:
            height, width, _ = self.frame.shape
            row_size = width * 3
            row_size = (row_size + 3) & ~3
            padding = row_size - (width * 3)
            file_size = row_size * height
            with open(archivo, "wb") as f:
                f.write(b'BM')
                f.write(struct.pack('<I', file_size + 54))
                f.write(b'\x00\x00\x00\x00')
                f.write(struct.pack('<I', 54))
                f.write(struct.pack('<I', 40))
                f.write(struct.pack('<I', width))
                f.write(struct.pack('<I', height))
                f.write(struct.pack('<H', 1))
                f.write(struct.pack('<H', 24))
                f.write(struct.pack('<I', 0))
                f.write(struct.pack('<I', file_size))
                f.write(struct.pack('<I', 2835))
                f.write(struct.pack('<I', 2835))
                f.write(struct.pack('<I', 0))
                f.write(struct.pack('<I', 0))
                for y in range (height - 1, -1, -1):
                    for x in range (width):
                        b, g, r = self.frame[y, x]
                        f.write(struct.pack('B', b))
                        f.write(struct.pack('B', g))
                        f.write(struct.pack('B', r))
                    for z in range (padding):
                        f.write(b'\x00')

    def cargar(self, archivo):
        if not os.path.exists(archivo):
            print("Archivo no encontrado")
        with open(archivo, 'rb') as f:
            if f.read(2) != b'BM':
                print("Solo soporta BMP")
                return
            f.seek(54)
            height = 480
            width = 640
            for y in range(height -1, -1, -1):
                for x in range(width):
                    pixel = f.read(3)
                    self.punto(x, y, (pixel[0], pixel[1], pixel[2]))