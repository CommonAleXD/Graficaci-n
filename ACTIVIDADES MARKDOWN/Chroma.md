# Actividad 8

## Instrucciones

*Captura una imagen, genera una máscara en la escala del HSV  y  haz que la imagen capturada sustituya la zona del HSV.*

### Código
```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.waitKey(2000)

# Capturar el fondo durante unos segundos
ret, background = cap.read()
if not ret:
    print("Error al capturar el fondo.")
    cap.release()
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el rango de azul
    lower_blue = np.array([80, 100, 0])
    upper_blue = np.array([130, 255, 255]) 

    # Máscara área azul
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Invertir la máscara para obtener las áreas que no son azules
    mask_inv = cv2.bitwise_not(mask)

    # Aplicar la máscara -> Solo mostrar zonas no azules
    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    res2 = cv2.bitwise_and(background, background, mask=mask)

    # Combinar imágenes
    resultado = cv2.addWeighted(res1, 1, res2, 1, 0) 

    cv2.imshow("Capa de Invisibilidad", resultado)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Resultado
![](Resultados/Fondo%20propio.png)
