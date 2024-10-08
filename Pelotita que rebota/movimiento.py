import numpy as np
import cv2

ancho, alto = 500, 500

# Configurar círculo
x, y = np.random.randint(50, ancho-50), np.random.randint(50, alto-50)
vx, vy = 5, 3
radio = 10 


while True:
    area = np.ones((alto, ancho, 3), dtype=np.uint8)*255

    cv2.circle(area, (x, y), radio, (0, 0, 0), -1)

    # Actualizar la posición del círculo
    x += vx
    y += vy

    # Verificar colisiones con los bordes y rebotar
    if x - radio <= 0 or x + radio >= ancho:
        vx = -vx  # Cambiar la dirección en el eje x
    if y - radio <= 0 or y + radio >= alto:
        vy = -vy  # Cambiar la dirección en el eje y
        

    cv2.imshow("Circulito", area)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()