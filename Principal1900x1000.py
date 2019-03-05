# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal1900x1000.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1073)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1900, 1000))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Inicio 1900x1000.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1900, 21))
        self.menubar.setObjectName("menubar")
        self.menuJugar = QtWidgets.QMenu(self.menubar)
        self.menuJugar.setObjectName("menuJugar")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        self.menuInstrucciones = QtWidgets.QMenu(self.menubar)
        self.menuInstrucciones.setObjectName("menuInstrucciones")
        self.menuSalir = QtWidgets.QMenu(self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUn_Jugador = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Un jugador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUn_Jugador.setIcon(icon)
        self.actionUn_Jugador.setAutoRepeat(True)
        self.actionUn_Jugador.setVisible(True)
        self.actionUn_Jugador.setIconVisibleInMenu(True)
        self.actionUn_Jugador.setObjectName("actionUn_Jugador")
        self.actionDos_Jugadores = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("2 jugadores.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDos_Jugadores.setIcon(icon1)
        self.actionDos_Jugadores.setObjectName("actionDos_Jugadores")
        self.actionInstrucciones = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("instrucciones.0x200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInstrucciones.setIcon(icon2)
        self.actionInstrucciones.setObjectName("actionInstrucciones")
        self.menuJugar.addAction(self.actionUn_Jugador)
        self.menuJugar.addAction(self.actionDos_Jugadores)
        self.menuInstrucciones.addAction(self.actionInstrucciones)
        self.menubar.addAction(self.menuJugar.menuAction())
        self.menubar.addAction(self.menuInstrucciones.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())
        self.toolBar.addAction(self.actionUn_Jugador)
        self.toolBar.addAction(self.actionDos_Jugadores)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInstrucciones)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuJugar.setTitle(_translate("MainWindow", "Jugar"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Acerca de "))
        self.menuInstrucciones.setTitle(_translate("MainWindow", "Instrucciones"))
        self.menuSalir.setTitle(_translate("MainWindow", "Salir"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionUn_Jugador.setText(_translate("MainWindow", "Un jugador"))
        self.actionUn_Jugador.setIconText(_translate("MainWindow", "Un jugador"))
        self.actionDos_Jugadores.setText(_translate("MainWindow", "Dos Jugadores"))
        self.actionInstrucciones.setText(_translate("MainWindow", "Instrucciones"))

