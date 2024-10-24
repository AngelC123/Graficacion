import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('link.jpg')

# Obtener las dimensiones de la imagen original
alto_original, ancho_original = imagen.shape[:2]

# Definir el tamaño de la ventana
alto_ventana = 700
ancho_ventana = 700

# Crear una ventana para mostrar la animación
cv2.namedWindow('Animacion Escalamiento', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Animacion Escalamiento', ancho_ventana, alto_ventana)  # Tamaño de ventana

# Definir el número de pasos de la animación
pasos = 100
escalado_maximo = max(ancho_ventana / ancho_original, alto_ventana / alto_original)  # Factor de escala máximo uniforme

# Definir la matriz de escalado 2D
def aplicar_escalamiento(x, y, factor):
    # Matriz de escalado uniforme (mismo factor para x y y)
    matriz_escalado = np.array([[factor, 0],
                                [0, factor]])
    # Vector con las coordenadas actuales
    coordenadas = np.array([x,
                            y])
    # Aplicar la transformación
    x_escalado, y_escalado = np.dot(matriz_escalado, coordenadas)
    return int(x_escalado), int(y_escalado)

# Animación de escalamiento
for i in range(pasos):
    # Calcular el factor de escala en función de los pasos (uniforme)
    if i < pasos // 2:
        # Escalar hacia arriba hasta el límite de la ventana
        factor = 1 + (escalado_maximo - 1) * (i / (pasos // 2))
    else:
        # Escalar hacia abajo
        if i < (pasos * 3) // 4:
            factor = escalado_maximo - ((escalado_maximo - 0.5) * ((i - (pasos // 2)) / (pasos // 4)))
        else:
            # Regresar al tamaño original
            factor = 0.5 + (1 - 0.5) * ((i - (3 * pasos // 4)) / (pasos // 4))

    # Calcular el nuevo tamaño de la imagen escalada (uniforme en ambos ejes)
    nuevo_ancho = int(ancho_original * factor)
    nuevo_alto = int(alto_original * factor)

    # Asegurarse de que el nuevo tamaño no exceda los límites de la ventana
    nuevo_ancho = min(nuevo_ancho, ancho_ventana)
    nuevo_alto = min(nuevo_alto, alto_ventana)

    # Crear un fondo
    fondo = np.ones((alto_ventana, ancho_ventana, 3), dtype=np.uint8) * 255

    # Calcular la posición para centrar la imagen escalada en el fondo
    centro_x = (fondo.shape[1] - nuevo_ancho) // 2
    centro_y = (fondo.shape[0] - nuevo_alto) // 2

    # Usar la matriz de transformación para escalar manualmente
    for y in range(nuevo_alto):
        for x in range(nuevo_ancho):
            # Calcular las coordenadas de la imagen escalada usando la matriz de escalado (uniforme)
            original_x, original_y = aplicar_escalamiento(x, y, 1 / factor)

            # Asegurarse de que las coordenadas originales están dentro de los límites de la imagen
            if original_x < ancho_original and original_y < alto_original:
                # Asignar el píxel de la imagen escalada en el fondo
                fondo[centro_y + y, centro_x + x] = imagen[original_y, original_x]

    # Mostrar la imagen escalada en la ventana
    cv2.imshow('Animacion Escalamiento', fondo)

    # Esperar 30 ms entre cada cuadro para hacer visible la animación
    cv2.waitKey(1)

# Terminar la animación
cv2.destroyAllWindows()
