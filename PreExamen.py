import numpy as np
import cv2 as cv

img = cv.imread("salida.png", 1)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Límites para rojos
linf_rojo1 = np.array([0, 100, 100])   
lis_rojo1 = np.array([7, 255, 255])

limf_rojo2 = np.array([160, 100, 100])  
lis_rojo2 = np.array([180, 255, 255])

#Generar máscaras rojas
mask1_rojo = cv.inRange(hsv, linf_rojo1, lis_rojo1)
mask2_rojo = cv.inRange(hsv, limf_rojo2, lis_rojo2)
mask_rojo = mask1_rojo + mask2_rojo

#Límites para azules
linf_azul = np.array([85, 100, 100])
lis_azul = np.array([130, 255, 255])

#Generar máscara azul
mask_azul = cv.inRange(hsv, linf_azul, lis_azul)

#Límites para verdes
linf_verde = np.array([40, 50, 50])
lis_verde = np.array([82, 255, 255])

#Generar máscara verde
mask_verde= cv.inRange(hsv, linf_verde, lis_verde)

#Límites para amarillos
linf_amarillo = np.array([20, 100, 100])
lis_amarillo = np.array([30, 255, 255])

#Generar máscara amarilla
mask_amarillo = cv.inRange(hsv, linf_amarillo, lis_amarillo)

#Imagen a grises para editar
esc_grises = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gris_total = cv.cvtColor(esc_grises, cv.COLOR_GRAY2BGR)

#Reaplicar colores
res_rojo = cv.bitwise_and(img, img, mask=mask_rojo)
res_azul = cv.bitwise_and(img, img, mask=mask_azul)
res_verde = cv.bitwise_and(img, img, mask=mask_verde)
res_amarillo = cv.bitwise_and(img, img, mask=mask_amarillo)

resultado_rojo = np.where(res_rojo != 0, res_rojo, gris_total)
resultado_azul = np.where(res_azul != 0, res_azul, gris_total)
resultado_verde = np.where(res_verde != 0, res_verde, gris_total)
resultado_amarillo = np.where(res_amarillo != 0, res_amarillo, gris_total)


cv.imshow("Imagen padrísima", img)
cv.imshow("Imagen rojos", resultado_rojo) 
cv.imshow("Imagen azules", resultado_azul) 
cv.imshow("Imagen verdes", resultado_verde) 
cv.imshow("Imagen amarillos", resultado_amarillo) 

cv.waitKey(0)
cv.destroyAllWindows()