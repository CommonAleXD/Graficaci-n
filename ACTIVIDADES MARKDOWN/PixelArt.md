# Actividad 1

## Instrucciones

*Generar una imagen tipo pixel art utilizando una matriz de enteros en el rango de 0 a 255.*
(Usé un formato BGR para facilitar el posicionamiento de los pixeles)

```python
import numpy as np
import cv2

matrix = np.ones((16, 12, 3), dtype=np.uint8) * 255

red_coordinates = [
    (0, slice(3, 8)), (1, slice(2,10)), (9, slice(0,4)),
    (8, slice(1,4)), (7,3), (8, 1), (8, 2), (8, 9), (8, 10), (10,2), (7, 8)
    ,(8,5),(8,6),(7,5),(7,6), (9, 11), (9,10), (9,9), (9,8), (8,8), (10,9)
]

piel_coordinates = [
    (5,slice(3,6)),(6, slice(3,9)), (2, 8),(2, 5),(2, 6)
    ,(slice(2,6),slice(5,7)), (slice(10,13), slice(0,2)), (11,2), (4,7), (4, slice(9,12)),
    (3,10), (3,8), (3,9), (3,4), (3,2),(4,2), (6, 3), (6, 9), (10, 11), (11, 11), 
    (12, 10), (12, 11), (11,10), (11,9), (12,10), (10,10)
]

cafe_coordinates = [
    (14, slice (2,5)), (14,slice(7,10)), (15, slice(1, 5)), (15, slice(7, 11)),
    (5, 1), (5, 2), (5, slice(7,11)), (4,8), (2, 2), (2, 3), (2, 4), (3, 1),
    (4, 1), (4,3), (3,3), (5,4), (4,4)
]

amarillo_coordinates = [
    (10,4), (10,7)
]

azul_coordinates = [
    (13,2), (13,3), (13,4), (13,7), (13,8), (13,9),
    (12,slice(2,10)), (11, slice(3,9)), (10,3), (slice(7,10),4), (slice(7,10),7),
    (9,5), (9,6), (10,5), (10,6), (10,8)
]

black_coordinates = [
    (2,7), (3,7)
]

for coord in cafe_coordinates:
    if isinstance(coord[1], slice):
        matrix[coord[0], coord[1]] = [0, 76, 153]  
    else:
        matrix[coord[0], coord[1]] = [0, 76, 153]


for coord in piel_coordinates:
    if isinstance(coord[1], slice):
        matrix[coord[0], coord[1]] = [102, 178, 255]  
    else:
        matrix[coord[0], coord[1]] = [102, 178, 255]


for coord in red_coordinates:
    if isinstance(coord[1], slice):
        matrix[coord[0], coord[1]] = [0, 0, 255]
    else:  
        matrix[coord[0], coord[1]] = [0, 0, 255]
        
for coord in amarillo_coordinates:
    if isinstance(coord[1], slice):
        matrix[coord[0], coord[1]] = [51, 255, 255]
    else:  
        matrix[coord[0], coord[1]] = [51, 255, 255]
        
for coord in azul_coordinates:
    if isinstance(coord[1], slice):
        matrix[coord[0], coord[1]] = [170, 170, 0]  
    else:
        matrix[coord[0], coord[1]] = [170, 170, 0]

for coord in black_coordinates:
    if isinstance(coord[1], slice):
        matrix[coord[0], coord[1]] = [0, 0, 0]  # Negro en formato BGR
    else:
        matrix[coord[0], coord[1]] = [0, 0, 0]

scale_factor = 40
scaled_matrix = cv2.resize(matrix, (matrix.shape[1] * scale_factor, matrix.shape[0] * scale_factor), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Scaled Image', scaled_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
