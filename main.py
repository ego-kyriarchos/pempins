import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from view.view_winmain import Ui_MainWindow
from pysondb import db
from datetime import datetime
from view.viewIngresoGasto import Ui_IngresarGastar
from view.viewMovimiento import Ui_Movimiento
import view.config as config 

class MainWin(QMainWindow):
  def __init__(self):
    super().__init__()
    self.check_db()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.show()
    self.ui.botonSalir.clicked.connect(lambda:self.close())
    self.ui.botonIngresar.clicked.connect(lambda:self.ingresar())
    self.ui.botonGastar.clicked.connect(lambda:self.ingresar())
    self.ui.botonMover.clicked.connect(lambda:self.mover())
  
  def config(self):
    self.lista_tipos_de_registro = ['Diezmo', 'Ahorro', 'Comida', 'Capricho', 'Transporte', 'Vivienda', 'Todos']
    self.porcentages = {"Diezmo": 0.10, "Transporte": 0.10, "Ahorro": 0.18, "Comida": 0.30, "Capricho": 0.10, "Vivienda": 0.22}

  def check_db(self):
    self.historial_db = db.getDb('bbdd/historial.json')
    self.cuentas = db.getDb('bbdd/cuentas.json')
    cuentas = self.cuentas.get()
    fecha_actual = "01/01/1970 00:00:00"
    if cuentas == [{'': ''}]:
      self.cuentas.add({"ultima_modificacion":fecha_actual,"Diezmo":0,"Ahorro":0,"Comida":0,"Capricho":0,"Transporte":0,"Vivienda":0})

  def ingresar(self):
    self.ingreso = QtWidgets.QMainWindow()
    self.ui = Ui_IngresarGastar()
    self.ui.setupUi(self.ingreso)
    self.ingreso.show()
    self.ui.comboBoxAplicarEn.addItems(config.lista_tipos_de_registro)
    self.ui.pushButtonCancelar.clicked.connect(lambda:self.close())
    self.ui.pushButtonGuardarEnCache.clicked.connect(lambda:self.guardarEnCache())

  def gastar(self):
    self.gasto = QtWidgets.QMainWindow()
    self.ui = Ui_IngresarGastar()
    self.ui.setupUi(self.gasto)
    self.ui.comboBoxAplicarEn.addItems(config.lista_tipos_de_registro)
    self.gasto.show()
    self.ui.pushButtonCancelar.clicked.connect(lambda:self.close())
    self.ui.pushButtonGuardarEnCache.clicked.connect(lambda:self.guardarEnCache())

  def mover(self):
    self.movimiento = QtWidgets.QMainWindow()
    self.ui = Ui_Movimiento()
    self.ui.setupUi(self.movimiento)
    self.ui.comboBoxOrigen.addItems(config.lista_tipos_de_registro)
    self.ui.comboBoxDestino.addItems(config.lista_tipos_de_registro)
    self.movimiento.show()

  def guardarEnCache(self):
    self.checkGuardadoEnCache()
    #if self.check:
    pass

  def checkGuardadoEnCache(self):
    self.check = False
    contador = 0
    try:
      float(self.ui.lineEditImporte.text())
      contador += 1
    except:
      QMessageBox.information(self, 'Error', "Debes de escribir un numero. Ej: 12.00", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    razon = self.ui.lineEditRazon.text()
    if len(razon) > 30:
      QMessageBox.information(self, 'Error', "La razon debe de ser menos de 30 caracteres", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
    else:
      contador += 1

    if contador == 2:
      self.check = True

  def verMonedero(self):
    pass

if __name__ == '__main__':
  print("Iniciando Pempins")
  app = QApplication(sys.argv)
  window = MainWin()
  sys.exit(app.exec())