
from time import gmtime, strftime
import numpy as np
import cv2 
import logging as log
import threading  

class Camara(threading.Thread):  
    def __init__(self, num):  
        threading.Thread.__init__(self)  
        self.num = num  

    def exit(): 
        cap.release()

    def run(self):  
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        length = 0
        while(True):
            #leemos un frame y lo guardamos
            ret, img = cap.read()
         
            #convertimos la imagen a blanco y negro
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         
            #buscamos las coordenadas de los rostros (si los hay) y
            #guardamos su posicion
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize= (20, 20),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
           
            #Dibujamos un rectangulo en las coordenadas de cada rostro
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),0)

          
            #Mostramos la imagen
            cv2.imshow('img',img)
             
            #con la tecla 'q' salimos del programa
            
            if len(faces) != length:
                length =  len(faces) 
                if length > 0 :            
                    log.warning( 'Numero de personas detectadas: '+ str( length ) + ' en la fecha: ' + strftime( "%Y-%m-%d %H:%M:%S", gmtime() ))
                   
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 

        cap.release()

class test(threading.Thread):  
    def __init__(self, num):  
        threading.Thread.__init__(self)  
        self.num = num  

    def run(self):  
      for value in range(0,500):
        print(str(value))

print "Soy el hilo principal"  
    
t = Camara('camara')  
 

g = test('test') 
g.start()  
t.start()  
g.join()
t.join()
print 'fin'