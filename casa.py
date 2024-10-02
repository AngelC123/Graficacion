from Dibujo import Dibujo

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
casa.guarda("casa.bmp")