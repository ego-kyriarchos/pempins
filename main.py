import sys, json, os, time
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,QPushButton)
from PyQt6.QtGui import QFont, QPixmap
#from transaccion.gasto import Gasto
from ventanas.ingreso_o_gasto import IngresoOGastoView
#from transaccion.movimiento import Movimiento
# from transaccion.guardar import Guardar
import ventanas.config as config
from datetime import datetime
from ventanas.guardar import Guardar
from ventanas.movimiento import MovimientoView


if not os.path.isfile("bbdd/registros.json"):
  with open('bbdd/registros.json', 'w') as registro_file:
    json.dump({}, registro_file, indent=2)

if not os.path.isfile("bbdd/cuentas.json"):
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
    gasto_boton.clicked.connect(self.gastar)

    mover_boton = QPushButton(self)
    mover_boton.setText("Mover dinero")
    mover_boton.resize(120,24)
    mover_boton.move(20,120)
    mover_boton.clicked.connect(self.mover)

    guardar_boton = QPushButton(self)
    guardar_boton.setText("Guardar cambios")
    guardar_boton.resize(120,24)
    guardar_boton.move(20,160)
    guardar_boton.clicked.connect(self.guardar)

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

  def guardar(self):
    self.accion = Guardar()
    self.accion.checkear_dict()
      
  def ingresar(self):
    self.ingress_form = IngresoOGastoView()
    self.ingress_form.tipo = 'Ingreso'
    self.ingress_form.show()

  def gastar(self):
    self.gasto_form = IngresoOGastoView()
    self.gasto_form.tipo = 'Gasto'
    self.gasto_form.show()
  
  def mover(self):
    self.movimiento_form = MovimientoView()
    self.movimiento_form.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ventana = Inicio()
  sys.exit(app.exec())