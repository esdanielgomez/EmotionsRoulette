import sys
import random
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from Principal1900x1000 import Ui_MainWindow
from UnJugador1900x1000 import Ui_Form
import requests
import cv2
from PIL import Image
subscription_key = "KEY"
face_api_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'
assert subscription_key

class ventanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(ventanaPrincipal,self).__init__(parent)
        self.setupUi(self)
        self.actionUn_Jugador.triggered.connect(self.unJugador)
    
    def unJugador(self):
        self.vl=ventanaJugador()
        self.vl.show()
        
class ventanaJugador(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(ventanaJugador,self).__init__(parent)
        self.setupUi(self)
        self.pushButtonIniciar.clicked.connect(self.iniciar)
        self.pushButtonResultados.clicked.connect(self.resultados)
        self.pushButtonReset.clicked.connect(self.reset)
        self.foto=None
        self.image_data = None
        self.inicarCam()
        self.result=0
        self.combo=1
        self.a=0
        self.imagen = random.randrange(5)
        self.imagen1 = self.elegirEmoji(self.imagen)
        self.estado=self.imagen
    
    def iniciar(self):
        if self.a==0:
            self.pushButtonIniciar.setEnabled(False)
        imagenes = ["./images/normal.png", "./images/sorprendido.png", "./images/enojado.png", "./images/triste.png", "./images/feliz.png"]
        lista=[]
        lista=self.obtenerResultado()
        if (lista[self.estado]>=50):
            self.result+=10*self.combo
            self.combo+=1
        else:
            self.combo=1
        self.lcdNumberCombo.display(self.combo)
        self.lcdNumberPuntuacion.display(self.result)
        if self.a!=8:
            self.labelEmoji.setPixmap(QPixmap(imagenes[self.imagen]))
            self.labelSiguienteEmoji.setPixmap(QPixmap(imagenes[self.imagen1]))
            self.labelContador.setText(str(self.a+1)+"/8")
            
        else:
            self.pushButtonResultados.setEnabled(False)
        self.progressBarNormal.setValue(lista[0])
        self.progressBarSorp.setValue(lista[1])
        self.progressBarEnojado.setValue(lista[2])
        self.progressBarTriste.setValue(lista[3])
        self.progressBarFeliz.setValue(lista[4])
        self.show_frame()
        self.estado=self.imagen
        self.imagen = self.imagen1
        self.imagen1 = self.elegirEmoji(self.imagen)
        self.a+=1

    def reset(self):
        self.pushButtonIniciar.setEnabled(True)
        self.pushButtonResultados.setEnabled(True)
        self.a=0
        self.result=0
        self.combo=1
        self.lcdNumberCombo.display(self.combo)
        self.lcdNumberPuntuacion.display(self.result)
        self.labelContador.setText(str(self.a+1)+"/8")  
            
    def inicarCam(self):
        self.webcam = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_frame)
        self.timer.start(5)
            
    def obtenerResultado(self):
        lista=[]
        if self.image_data==None:
            lista=[1,1,1,1,1]
        else:
            response = requests.post(face_api_url, params=params, headers=headers, data=self.image_data)
            faces = response.json()
            lista.append(faces[0]['faceAttributes']['emotion']['neutral']*100)
            lista.append(faces[0]['faceAttributes']['emotion']['surprise']*100)
            lista.append(faces[0]['faceAttributes']['emotion']['anger']*100)
            lista.append(faces[0]['faceAttributes']['emotion']['sadness']*100)
            lista.append(faces[0]['faceAttributes']['emotion']['happiness']*100)
        return lista

    def elegirEmoji(self, actual):
        imagen = random.randrange(5)
        while (imagen == actual):
            imagen = random.randrange(5)
        return imagen        
    
    def resultados(self):
        ok, self.foto = self.webcam.read()
        cv2.imwrite("./images/foto.png",self.foto)
        self.image_data = open("./images/foto.png", "rb").read()
        self.iniciar()

    def show_frame(self):
        ok, self.foto = self.webcam.read()
        self.foto =cv2.flip(self.foto,1)
        self.displayImg(self.foto)
    
    def displayImg(self,img):
        qformat=QImage.Format_Indexed8
        if (len(img.shape)==3):
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        image = QImage(img, img.shape[1], img.shape[0], img.strides[0],qformat)
        image = image.rgbSwapped()
        self.labelFoto.setPixmap(QPixmap.fromImage(image))

headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion'
}
app=QtWidgets.QApplication(sys.argv)
myApp=ventanaPrincipal()
myApp.show()
app.exec_()