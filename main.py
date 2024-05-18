import sys, sqlite3
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from view.view_winmain import Ui_MainWindow
from datetime import datetime
from view.viewIngresoGasto import Ui_IngresarGastar
from view.viewMovimiento import Ui_Movimiento
import os

user_home = os.path.expanduser('~')
if not os.path.exists(f'{user_home}/pempins'):
  os.makedirs(f'{user_home}/pempins')
db_path = f"{user_home}/pempins/pempins.db"

class MainWin(QMainWindow):
  def __init__(self):
    super().__init__()
    self.check_db()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.show()
    self.ui.versionPempins.setText('Version: v0.1')
    self.ui.botonSalir.clicked.connect(lambda:self.close())
    self.ui.botonIngresar.clicked.connect(lambda:self.ingresar())
    self.ui.botonGastar.clicked.connect(lambda:self.gastar())
    self.ui.botonMover.clicked.connect(lambda:self.mover())
    self.ui.botonGuardarCambios.clicked.connect(lambda:self.guardar())
    self.ui.botonVerMonedero.clicked.connect(lambda:self.verMonedero())
    self.ui.botonBuscar.clicked.connect(lambda:self.buscar())
    
    self.cached_mem = {}
    self.viewMonedero = False
    self.lista_tipos_de_registro = ['Diezmo', 'Ahorro', 'Comida', 'Capricho', 'Transporte', 'Vivienda', 'Todos']
    self.porcentages = {"Diezmo": 0.10, "Transporte": 0.10, "Ahorro": 0.18, "Comida": 0.30, "Capricho": 0.10, "Vivienda": 0.22}
    now = datetime.now()
    self.year = int(now.strftime("%Y"))
    self.month = int(now.strftime("%m"))
    self.day = int(now.strftime("%d"))
    self.ui.FechaDesde.setDate(QtCore.QDate(self.year, self.month, self.day))
    self.ui.FechaHasta.setDate(QtCore.QDate(self.year, self.month, self.day))

  def check_db(self):
    pempins_db = sqlite3.connect(db_path)
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
      Vivienda real,
      Total real
    )""")

    pempins_db.close()

  def guardar_cache_en_bbdd(self):
    pempins_db = sqlite3.connect(db_path)
    for id, datos in self.cached_mem.items():
      if datos["tipo"] == "ingreso":
        print("insertando en la tabla ingresos")
        pempins_db.execute("""
          insert into ingresos (Fecha,Importe,Razon,AplicarEn)
          values (?,?,?,?);
        """, (datos["fecha"], datos["importe"], datos["razon"], datos["cuenta"]))
        pempins_db.commit()
      elif datos["tipo"] == "gasto":
        print("insertando en la tabla gastos")
        pempins_db.execute("""
          insert into gastos (Fecha,Importe,Razon,AplicarEn)
          values (?,?,?,?);
        """, (datos["fecha"], datos["importe"], datos["razon"], datos["cuenta"]))
        pempins_db.commit()
      elif datos["tipo"] == "movimiento":
        print("insertando en la tabla movimiento")
        pempins_db.execute("""
          insert into movimientos (Fecha, Importe, Razon, Origen, Destino)
          values (?,?,?,?,?);
        """, (datos["fecha"], datos["importe"], datos["razon"], datos["origen"], datos["destino"]))
        pempins_db.commit()
    pempins_db.close()

  def calcular_porcentages(self):
    pempins_db = sqlite3.connect(db_path)
    pempins_db = pempins_db.cursor()
    pempins_db.execute("select * from cuentas order by id desc limit 1;")
    datos_db = pempins_db.fetchall()
    pempins_db.close()

    if datos_db == []:
      datos_dict = {"Fecha": 0, "Diezmo": 0, "Ahorro": 0, "Comida": 0, "Capricho": 0, "Transporte": 0, "Vivienda": 0}
    else:
      datos_dict = {"Fecha": datos_db[0][1], "Diezmo": float(datos_db[0][2]), "Ahorro": float(datos_db[0][3]), "Comida": float(datos_db[0][4]), "Capricho": float(datos_db[0][5]), "Transporte": float(datos_db[0][6]), "Vivienda": float(datos_db[0][7])}

    for fecha, datos_cache in self.cached_mem.items():
      if datos_cache["tipo"] == "ingreso": 
        if datos_cache["cuenta"] == "Todos":
          for cuenta in self.porcentages:
            calculo_cuenta = round(datos_cache["importe"] * self.porcentages[cuenta], 2)
            calculo_cuenta = round(datos_dict[cuenta] + calculo_cuenta, 2)
            datos_dict[cuenta] = calculo_cuenta
        else:
          cuenta = datos_cache["cuenta"]
          calculo_cuenta = round(datos_cache["importe"] + datos_dict[cuenta], 2)
          datos_dict[cuenta] = calculo_cuenta

      if datos_cache["tipo"] == "gasto": 
        if datos_cache["cuenta"] == "Todos":
          for cuenta in self.porcentages:
            calculo_cuenta = round(datos_cache["importe"] * self.porcentages[cuenta], 2)
            calculo_cuenta = round(datos_dict[cuenta] - calculo_cuenta)
            datos_dict[cuenta] = calculo_cuenta
            print(datos_dict)
        else:
          cuenta = datos_cache["cuenta"]
          calculo_cuenta = round(datos_dict[cuenta] - datos_cache["importe"], 2)
          datos_dict[cuenta] = calculo_cuenta
      
      if datos_cache["tipo"] == "movimiento":
        datos_dict[datos_cache["origen"]] -= datos_cache["importe"]
        datos_dict[datos_cache["destino"]] += datos_cache["importe"]

    now = datetime.now()
    fecha = now.strftime("%d/%m/%Y")
    pempins_db = sqlite3.connect(db_path)
    total = datos_dict["Diezmo"] + datos_dict["Ahorro"] + datos_dict["Comida"] + datos_dict["Capricho"] + datos_dict["Transporte"] + datos_dict["Vivienda"]
    pempins_db.execute("""insert into cuentas (Fecha,Diezmo,Ahorro,Comida,Capricho,Transporte,Vivienda,Total)
    values (?,?,?,?,?,?,?,?)""", (fecha,datos_dict["Diezmo"], datos_dict["Ahorro"], datos_dict["Comida"], datos_dict["Capricho"], datos_dict["Transporte"], datos_dict["Vivienda"], total))
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
    self.ui_ingresar = Ui_IngresarGastar()
    self.ui_ingresar.setupUi(self.ingreso)
    self.ingreso.show()
    self.ui_ingresar.dateEditFecha.setDate(QtCore.QDate(self.year, self.month, self.day))
    self.ui_ingresar.comboBoxAplicarEn.addItems(self.lista_tipos_de_registro[-1:] + self.lista_tipos_de_registro[:-1])
    self.ui_ingresar.pushButtonCancelar.clicked.connect(lambda:self.ingreso.close())
    self.ui_ingresar.pushButtonGuardarEnCache.clicked.connect(lambda:self.guardarEnCache("ingreso", self.ui_ingresar))

  def gastar(self):
    self.gasto = QtWidgets.QMainWindow()
    self.ui_gastar = Ui_IngresarGastar()
    self.ui_gastar.setupUi(self.gasto)
    self.ui_gastar.comboBoxAplicarEn.addItems(self.lista_tipos_de_registro[1:-1]) # Sin diezmo y sin Todos
    self.gasto.show()
    self.ui_gastar.dateEditFecha.setDate(QtCore.QDate(self.year, self.month, self.day))
    self.ui_gastar.pushButtonCancelar.clicked.connect(lambda:self.gasto.close())
    self.ui_gastar.pushButtonGuardarEnCache.clicked.connect(lambda:self.guardarEnCache("gasto", self.ui_gastar))

  def mover(self):
    self.movimiento = QtWidgets.QMainWindow()
    self.ui_mover = Ui_Movimiento()
    self.ui_mover.setupUi(self.movimiento)
    self.ui_mover.comboBoxOrigen.addItems(self.lista_tipos_de_registro[1:-1]) # Sin diezmo y sin Todos
    self.ui_mover.comboBoxDestino.addItems(self.lista_tipos_de_registro[1:-1]) # Sin diezmo y sin Todos
    self.movimiento.show()
    self.ui_mover.dateEditFecha.setDate(QtCore.QDate(self.year, self.month, self.day))
    self.ui_mover.pushButtonGuardarEnCache.clicked.connect(lambda:self.guardarEnCache("movimiento" , self.ui_mover))
    self.ui_mover.pushButtonCancelar.clicked.connect(lambda:self.movimiento.close())

  def guardarEnCache(self, tipo, ui):
    self.checkGuardadoEnCache(tipo, ui)
    timestamp = datetime.now()
    timestamp = timestamp.timestamp()
    if self.check and tipo in ["ingreso", "gasto"] :
      importe = float(ui.lineEditImporte.text())
      fecha = datetime.strptime(ui.dateEditFecha.text(), '%d/%m/%Y').strftime('%Y-%m-%d')
      razon = ui.lineEditRazon.text()
      cuenta = ui.comboBoxAplicarEn.currentText()
      self.cached_mem[timestamp] = {"fecha": fecha, "importe": importe, "razon": razon, "cuenta": cuenta, "tipo": tipo}
      print(self.cached_mem)
      if tipo == "ingreso":
        self.ingreso.close()
      else:
        self.gasto.close()
    elif self.check and tipo == "movimiento":
      print(tipo, 'movimiento')
      importe = float(ui.lineEditImporte.text())
      fecha = datetime.strptime(ui.dateEditFecha.text(), '%d/%m/%Y').strftime('%Y-%m-%d')
      razon = ui.lineEditRazon.text()
      destino = ui.comboBoxDestino.currentText()
      origen = ui.comboBoxOrigen.currentText()
      self.cached_mem[timestamp] = {"fecha": fecha, "importe": importe, "razon": razon, "origen": origen, "destino": destino, "tipo": tipo}
      print(self.cached_mem)
      self.movimiento.close()

  def checkGuardadoEnCache(self, tipo, ui):
    self.check = False
    contador = 0
    try:
      float(ui.lineEditImporte.text())
      contador += 1
    except:
      QMessageBox.information(self, 'Error', "Debes de escribir un numero. Ej: 12.00", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    razon = ui.lineEditRazon.text()
    if len(razon) > 30:
      QMessageBox.information(self, 'Error', "La razon debe de ser menos de 30 caracteres", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
    else:
      contador += 1

    if contador == 2 and tipo in ["gasto", "ingreso"]:
      self.check = True
    else:
      if ui.comboBoxOrigen.currentText() == ui.comboBoxDestino.currentText():
        QMessageBox.information(self, 'Error', "Origen y destino no puede ser iguales", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
      else:  
        contador += 1

    if contador == 3 and tipo == "movimiento":
      self.check = True
    
  def buscar(self):
    fecha_desde = self.ui.FechaDesde.text()
    fecha_hasta = self.ui.FechaHasta.text()
    fecha_desde = datetime.strptime(fecha_desde, "%d/%m/%Y").strftime('%Y-%m-%d')
    fecha_hasta = datetime.strptime(fecha_hasta, "%d/%m/%Y").strftime('%Y-%m-%d')

    if fecha_desde > fecha_hasta:
      QMessageBox.information(self, 'Error', 'La fecha "Desde" no puede ser mayor que la fecha "Hasta"', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
    else:
      self.ui.textoHistorial.setPlainText("")
      pempins_db = sqlite3.connect(db_path)
      pempins_db = pempins_db.cursor()
      pempins_db.execute(f"select * FROM ingresos where Fecha BETWEEN '{fecha_desde}' AND '{fecha_hasta}';")
      ingresos = pempins_db.fetchall()
      pempins_db.execute(f"select * FROM gastos where Fecha BETWEEN '{fecha_desde}' AND '{fecha_hasta}';")
      gastos = pempins_db.fetchall()
      pempins_db.execute(f"select * FROM movimientos where Fecha BETWEEN '{fecha_desde}' AND '{fecha_hasta}';")
      movimientos = pempins_db.fetchall()
      pempins_db.close()
      print(fecha_hasta, fecha_desde)
      self.ui.textoHistorial.appendPlainText("Ingresos:")
      for ingreso in ingresos:
        importe = ingreso[2]
        razon = ingreso[3]
        tipo = ingreso[4]
        fecha = datetime.strptime(ingreso[1], '%Y-%m-%d').strftime('%d/%m/%Y')
        self.ui.textoHistorial.appendPlainText(f" - {fecha}\n"
f"        Importe: +{importe}€\n"
f"        Razon: {razon}\n"
f"        Aplicado en: {tipo}")
      self.ui.textoHistorial.appendPlainText("Gastos:")
      for gasto in gastos:
        fecha = datetime.strptime(gasto[1], '%Y-%m-%d').strftime('%d/%m/%Y')
        importe = gasto[2]
        razon = gasto[3]
        tipo = gasto[4]
        self.ui.textoHistorial.appendPlainText(f" - {fecha}\n"
f"        Importe: -{importe}€\n"
f"        Razon: {razon}\n"
f"        Aplicado en: {tipo}")
      self.ui.textoHistorial.appendPlainText("Movimientos:")
      for movimiento in movimientos:
        fecha = datetime.strptime(movimiento[1], '%Y-%m-%d').strftime('%d/%m/%Y')
        importe = movimiento[2]
        razon = movimiento[3]
        origen = movimiento[4]
        destino = movimiento[5]
        self.ui.textoHistorial.appendPlainText(f" - {fecha}\n"
f"        Importe: ♻{importe}€\n"
f"        Razon: {razon}\n"
f"        Origen: {origen}\n"
f"        Destino: {destino}")

  def verMonedero(self):
    if self.viewMonedero == False:
      pempins_db = sqlite3.connect(db_path)
      pempins_db = pempins_db.cursor()
      pempins_db.execute("select * from cuentas order by id desc limit 1;")
      datos_db = pempins_db.fetchall()
      pempins_db.close()
      if datos_db == []:
        datos_db =[(0,0,0,0,0,0,0,0,0)]
      self.ui.textoMonedero.setPlainText("Ahorro:\n"
f"  {float(datos_db[0][3])}€\n"
"Diezmo:\n"
f"  {float(datos_db[0][2])}€\n"
"Comida:\n"
f"  {float(datos_db[0][4])}€\n"
"Capricho:\n"
f"  {float(datos_db[0][5])}€\n"
"Transporte:\n"
f"  {float(datos_db[0][6])}€\n"
"Vivienda:\n"
f"  {float(datos_db[0][7])}€\n"
"Total:\n"
f"  {float(datos_db[0][8])}€")
      self.viewMonedero = True
    else:
      self.ui.textoMonedero.setPlainText("Ahorro:\n"
"  xxx€\n"
"Diezmo:\n"
"  xxx€\n"
"Comida:\n"
"  xxx€\n"
"Capricho:\n"
"  xxx€\n"
"Transporte:\n"
"  xxx€\n"
"Vivienda:\n"
"  xxxx€\n"
"Total:\n"
"  xxxx€")
      self.viewMonedero = False

if __name__ == '__main__':
  print("Iniciando Pempins")
  app = QApplication(sys.argv)
  window = MainWin()
  sys.exit(app.exec())