import sys, sqlite3
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from view.view_winmain import Ui_MainWindow
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
    self.ui.botonGastar.clicked.connect(lambda:self.gastar())
    self.ui.botonMover.clicked.connect(lambda:self.mover())
    self.ui.botonGuardarCambios.clicked.connect(lambda:self.guardar())
    self.cached_mem = {}
    self.lista_tipos_de_registro = ['Diezmo', 'Ahorro', 'Comida', 'Capricho', 'Transporte', 'Vivienda', 'Todos']
    self.porcentages = {"Diezmo": 0.10, "Transporte": 0.10, "Ahorro": 0.18, "Comida": 0.30, "Capricho": 0.10, "Vivienda": 0.22}

  def check_db(self):
    pempins_db = sqlite3.connect("bbdd/pempins.db")
    pempins_db.execute("""
    create table if not exists gastos (
      Id integer primary key autoincrement,
      Fecha text,
      Importe real,
      Razon text,
      AplicarEn text
    )""")

    pempins_db.execute("""
    create table if not exists ingresos (
      Id integer primary key autoincrement,
      Fecha text,
      Importe real,
      Razon text,
      AplicarEn text
    )""")

    pempins_db.execute("""
    create table if not exists movimientos (
      Id integer primary key autoincrement,
      Fecha text,
      Importe real,
      Razon text,
      Origen text,
      Destino text
    )""")

    pempins_db.execute("""
    create table if not exists cuentas (
      Id integer primary key autoincrement,
      Fecha text,
      Diezmo real,
      Ahorro real,
      Comida real,
      Capricho real,
      Transporte real,
      Vivienda real
    )""")

    pempins_db.close()

  def guardar_cache_en_bbdd(self):
    pempins_db = sqlite3.connect("bbdd/pempins.db")
    for fecha, datos in self.cached_mem.items():
      if datos["tipo"] == "ingreso":
        print("insertando en la tabla ingresos")
        pempins_db.execute("""
          insert into ingresos (Fecha,Importe,Razon,AplicarEn)
          values (?,?,?,?);
        """, (fecha, datos["importe"], datos["razon"], datos["cuenta"]))
        pempins_db.commit()
      elif datos["tipo"] == "gasto":
        print("insertando en la tabla gastos")
        pempins_db.execute("""
          insert into gastos (Fecha,Importe,Razon,AplicarEn)
          values (?,?,?,?);
        """, (fecha, datos["importe"], datos["razon"], datos["cuenta"]))
        pempins_db.commit()
    pempins_db.close()

  def calcular_porcentages(self):
    pempins_db = sqlite3.connect("bbdd/pempins.db")
    pempins_db = pempins_db.cursor()
    pempins_db.execute("select * from cuentas order by id desc limit 1;")
    datos_db = pempins_db.fetchall()
    pempins_db.close()

    if datos_db == []:
      datos_dict = {"Fecha": 0, "Diezmo": 0, "Ahorro": 0, "Comida": 0, "Capricho": 0, "Transporte": 0, "Vivienda": 0}
    else:
      datos_dict = {"Fecha": datos_db[0][1], "Diezmo": float(datos_db[0][2]), "Ahorro": float(datos_db[0][3]), "Comida": float(datos_db[0][4]), "Capricho": float(datos_db[0][5]), "Transporte": float(datos_db[0][6]), "Vivienda": float(datos_db[0][7])}

    for fecha, datos_cache in self.cached_mem.items():
      if datos_cache["cuenta"] == "Todos" and datos_cache["tipo"] == "ingreso":
        for cuenta in self.porcentages:
          calculo_cuenta = round(datos_cache["importe"] * self.porcentages[cuenta], 2)
          calculo_cuenta = round(datos_dict[cuenta] + calculo_cuenta, 2)
          datos_dict[cuenta] = calculo_cuenta
      elif datos_cache["tipo"] == "ingreso":
        cuenta = datos_cache["cuenta"]
        calculo_cuenta = round(datos_cache["importe"] + datos_dict[cuenta], 2)
        datos_dict[cuenta] = calculo_cuenta

      if datos_cache["cuenta"] == "Todos" and datos_cache["tipo"] == "gasto":
        for cuenta in self.porcentages:
          calculo_cuenta = round(datos_cache["importe"] * self.porcentages[cuenta], 2)
          calculo_cuenta = round(datos_dict[cuenta] - calculo_cuenta)
          datos_dict[cuenta] = calculo_cuenta
          print(datos_dict)
      elif datos_cache["tipo"] == "gasto":
        cuenta = datos_cache["cuenta"]
        calculo_cuenta = round(datos_dict[cuenta] - datos_cache["importe"], 2)
        datos_dict[cuenta] = calculo_cuenta

    now = datetime.now()
    fecha = now.strftime("%d/%m/%Y %H:%M:%S")
    pempins_db = sqlite3.connect("bbdd/pempins.db")
    pempins_db.execute("""insert into cuentas (Fecha,Diezmo,Ahorro,Comida,Capricho,Transporte,Vivienda)
    values (?,?,?,?,?,?,?)""", (fecha,datos_dict["Diezmo"], datos_dict["Ahorro"], datos_dict["Comida"], datos_dict["Capricho"], datos_dict["Transporte"], datos_dict["Vivienda"]))
    pempins_db.commit()
    pempins_db.close()

  def guardar(self):
    if self.cached_mem == {}:
      QMessageBox.information(self, 'Error', "No hay nada en la caché", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
    else:
      self.guardar_cache_en_bbdd()
      self.calcular_porcentages()
      self.cached_mem = {}

  def ingresar(self):
    self.ingreso = QtWidgets.QMainWindow()
    self.ui = Ui_IngresarGastar()
    self.ui.setupUi(self.ingreso)
    self.ingreso.show()
    self.ui.comboBoxAplicarEn.addItems(self.lista_tipos_de_registro)
    self.ui.pushButtonCancelar.clicked.connect(lambda:self.ingreso.close())
    self.ui.pushButtonGuardarEnCache.clicked.connect(lambda:self.guardarEnCache("ingreso"))

  def gastar(self):
    self.gasto = QtWidgets.QMainWindow()
    self.ui = Ui_IngresarGastar()
    self.ui.setupUi(self.gasto)
    self.ui.comboBoxAplicarEn.addItems(self.lista_tipos_de_registro)
    self.gasto.show()
    self.ui.pushButtonCancelar.clicked.connect(lambda:self.gasto.close())
    self.ui.pushButtonGuardarEnCache.clicked.connect(lambda:self.guardarEnCache("gasto"))

  def mover(self):
    self.movimiento = QtWidgets.QMainWindow()
    self.ui = Ui_Movimiento()
    self.ui.setupUi(self.movimiento)
    self.ui.comboBoxOrigen.addItems(self.lista_tipos_de_registro[:-1])
    self.ui.comboBoxDestino.addItems(self.lista_tipos_de_registro[:-1])
    self.movimiento.show()

  def guardarEnCache(self, tipo):
    self.checkGuardadoEnCache()
    if self.check:
      now = datetime.now()
      importe = float(self.ui.lineEditImporte.text())
      fecha = now.strftime("%d/%m/%Y %H:%M:%S")
      razon = self.ui.lineEditRazon.text()
      cuenta = self.ui.comboBoxAplicarEn.currentText()
      self.cached_mem[fecha] = {"importe": importe, "razon": razon, "cuenta": cuenta, "tipo": tipo}
      print(self.cached_mem)
      if tipo == "ingreso":
        self.ingreso.close()
      else:
        self.gasto.close()

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