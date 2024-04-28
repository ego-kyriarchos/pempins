from PyQt6.QtWidgets import (QMessageBox, QDialog)
import json
from . import config
from datetime import datetime

class Guardar(QDialog):
  def __init__(self):
    super().__init__()
  def checkear_dict(self):
    if config.cache == {}:
      QMessageBox.information(self, 'Error', "No hay nada que guardar", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
    else:
      self.guardar_en_registro()
      self.calcular_y_anadir_a_cuentas()
      config.cache = {}

  def guardar_en_registro(self):
    with open('bbdd/registros.json', 'r') as registro_file:
      registro_dict = json.load(registro_file)
    with open('bbdd/registros.json', 'w') as registro_file:
      registro_dict.update(config.cache)
      json.dump(registro_dict, registro_file, indent=2)
    
  def calcular_y_anadir_a_cuentas(self):
    with open('bbdd/cuentas.json', 'r') as cuentas_file:
      cuentas_dict = json.load(cuentas_file)
    for ingreso_gasto_movimineto in config.cache.values():
      if ingreso_gasto_movimineto["tipo"] == "Ingreso":
        if ingreso_gasto_movimineto["cuenta"] == "Todos":
          for cuenta in config.porcentages:
            calculo_cuenta = round(ingreso_gasto_movimineto["importe"] * config.porcentages[cuenta], 2)
            calculo_cuenta = round(cuentas_dict[cuenta] + calculo_cuenta)
            cuentas_dict[cuenta] = calculo_cuenta
        else:
          cuenta = ingreso_gasto_movimineto["cuenta"]
          calculo_cuenta = round(cuentas_dict[cuenta] + ingreso_gasto_movimineto["importe"],2)
          cuentas_dict[cuenta] = calculo_cuenta

    for ingreso_gasto_movimineto in config.cache.values():
      if ingreso_gasto_movimineto["tipo"] == "Gasto":
        if ingreso_gasto_movimineto["cuenta"] == "Todos":
          for cuenta in config.porcentages:
            calculo_cuenta = round(ingreso_gasto_movimineto["importe"] * config.porcentages[cuenta], 2)
            calculo_cuenta = round(cuentas_dict[cuenta] - calculo_cuenta)
            cuentas_dict[cuenta] = calculo_cuenta
        else:
          cuenta = ingreso_gasto_movimineto["cuenta"]
          calculo_cuenta = round(cuentas_dict[cuenta] - ingreso_gasto_movimineto["importe"],2)
          cuentas_dict[cuenta] = calculo_cuenta
          
    for ingreso_gasto_movimineto in config.cache.values():
      if ingreso_gasto_movimineto["tipo"] == "Movimiento":
        pass

    now = datetime.now()
    fecha = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('bbdd/cuentas.json', 'w') as registro_file:
      cuentas_dict["ultima_modificacion"] = fecha
      json.dump(cuentas_dict, registro_file, indent=2)