import sys, json, os, time
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,QPushButton)
from PyQt6.QtGui import QFont, QPixmap
from datetime import datetime
#from transaccion.gasto import Gasto
from ventanas.ingreso import IngresoView
#from transaccion.movimiento import Movimiento
# from transaccion.guardar import Guardar
import ventanas.config as config


if not os.path.isfile("registros.json"):
  with open('bbdd/registros.json', 'w') as registro_file:
    json.dump(config.json_registro, registro_file, indent=2)

if not os.path.isfile("cuentas.json"):
  now = datetime.now()
  fecha_actual = "01/01/1970 00:00:00"
  dictionary={"ultima_modificacion":fecha_actual,"Diezmo":0,"Ahorro":0,"Comida":0,"Capricho":0,"Transporte":0,"Vivienda":0}
  with open('bbdd/cuentas.json', 'w') as registro_file:
    json.dump(dictionary, registro_file, indent=2)

class Inicio(QWidget):
  def __init__(self):
    super().__init__()
    self.startUI()
  
  def startUI(self):
    self.setGeometry(100,100,450,500)
    self.setWindowTitle("Pempins-GUI")
    self.opciones()
    self.show()

  def opciones(self):
    ingreso_boton = QPushButton(self)
    ingreso_boton.setText("Ingresar")
    ingreso_boton.resize(120,24)
    ingreso_boton.move(20,40)
    ingreso_boton.clicked.connect(self.ingresar)
    
    gasto_boton = QPushButton(self)
    gasto_boton.setText("Gasto")
    gasto_boton.resize(120,24)
    gasto_boton.move(20,80)

    mover_boton = QPushButton(self)
    mover_boton.setText("Mover dinero")
    mover_boton.resize(120,24)
    mover_boton.move(20,120)

    guardar_boton = QPushButton(self)
    guardar_boton.setText("Guardar cambios")
    guardar_boton.resize(120,24)
    guardar_boton.move(20,160)

    vercuentas_boton = QPushButton(self)
    vercuentas_boton.setText("Ver cuentas")
    vercuentas_boton.resize(120,24)
    vercuentas_boton.move(20,200)

    salir_boton = QPushButton(self)
    salir_boton.setText("Salir")
    salir_boton.resize(120,24)
    salir_boton.move(20,450)
    salir_boton.clicked.connect(self.salir)

  def salir(self):
    exit()

  def ingresar(self):
    self.ingres_form = IngresoView()
    self.ingres_form.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ventana = Inicio()
  sys.exit(app.exec())