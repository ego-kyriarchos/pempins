from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout,QComboBox,QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QCheckBox)
import sys
from PyQt6.QtGui import QFont
from datetime import datetime
from . import config

class MovimientoView(QDialog):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Pempins-GUI")
    self.setGeometry(100,100,100,100)
    self.setModal(True)
    self.ingreso_form()
  
  def ingreso_form(self):
    #Importe
    importe_label = QLabel("importe:")
    self.importe_label = QLineEdit(self)
    #Razon
    razon_label = QLabel("razon:")
    self.razon_label = QLineEdit('self')

    #Donde aplicarlo
    origen_label = QLabel("Origen:")
    self.origen = QComboBox(self)
    self.origen.addItems(config.lista_tipos_de_registro[:-1][1:])
    destino_label = QLabel("Destino:")
    self.destino = QComboBox(self)
    self.destino.addItems(config.lista_tipos_de_registro[:-1][1:])

    cache_buton = QPushButton('Guardar en cache')
    cache_buton.clicked.connect(self.guardar_en_cache)
    cancelar_buton = QPushButton('Cancelar')
    cancelar_buton.clicked.connect(self.cancelar)

    vertical_layout_main = QVBoxLayout()
    h_layout_1 = QHBoxLayout()
    h_layout_2 = QHBoxLayout()
    h_layout_3 = QHBoxLayout()
    h_layout_4 = QHBoxLayout()
    h_layout_5 = QHBoxLayout()

    h_layout_1.addWidget(importe_label)
    h_layout_1.addWidget(self.importe_label)
    h_layout_2.addWidget(razon_label)
    h_layout_2.addWidget(self.razon_label)
    h_layout_3.addWidget(origen_label)
    h_layout_3.addWidget(self.origen)
    h_layout_4.addWidget(destino_label)
    h_layout_4.addWidget(self.destino)
    h_layout_5.addWidget(cache_buton)
    h_layout_5.addWidget(cancelar_buton)

    vertical_layout_main.addLayout(h_layout_1)
    vertical_layout_main.addLayout(h_layout_2)
    vertical_layout_main.addLayout(h_layout_3)
    vertical_layout_main.addLayout(h_layout_4)
    vertical_layout_main.addLayout(h_layout_5)

    self.setLayout(vertical_layout_main)

  def cancelar(self):
    self.close()
  
  def guardar_en_cache(self):
    self.check_form()
    if self.check:
      now = datetime.now()
      fecha = now.strftime("%d/%m/%Y %H:%M:%S")
      importe = float(self.importe_label.text())
      razon = self.razon_label.text()
      origen = self.origen.currentText()
      destino = self.destino.currentText()
      config.cache.update({fecha: {"importe": importe, "razon": razon, "origen": origen, "destino": destino, "tipo": "Movimiento"}})
      print(config.cache)
      self.close()

  def check_form(self):
    self.check = False
    contador = 0
    origen = self.origen.currentText()
    destino = self.destino.currentText()
    try:
      float(self.importe_label.text())
      contador += 1
    except:
      QMessageBox.information(self, 'Error', "Debes de escribir un numero. Ej: 12.00", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    if len(self.razon_label.text()) > 255:
      QMessageBox.information(self, 'Error', "La razon debe de ser menos de 255 caracteres", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
    else:
      contador += 1
    if origen == destino:
      QMessageBox.information(self, 'Error', "No pudes mover dinero en las mismas cuentas", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
    else:
      contador += 1
    if contador == 3:
      self.check = True
