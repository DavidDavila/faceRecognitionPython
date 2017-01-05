import cv2
import sys
import urllib, cStringIO

imagen_dir = sys.argv[1]  #obtenemos la ruta de la imagen a analizar y almacenamos
cascade_dir = sys.argv[2] #obtenemos la ruta del archivo cascade y almacenamos

#Cargamos el archivo cascade
rostroCascade = cv2.CascadeClassifier(cascade_dir)
imagen = cv2.imread(imagen_dir)  #cargamos imagen
filtro = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) #aplicamos filtro
rostros = rostroCascade.detectMultiScale(
	filtro,
	scaleFactor = 1.2,
	minNeighbors = 5,
	minSize= (30,30),
	flags = cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in rostros:
	##imagen, coordenadas, dimension, color rgb, canal alpha
	cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 1)
print(rostros)
cv2.imshow("Rostros encontrados", imagen) #abrimos una ventana con la imagen resultante
cv2.waitKey(0) #evento de salida o cierre de la ventana