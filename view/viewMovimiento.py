# Form implementation generated from reading ui file 'view/viewMovimiento.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Movimiento(object):
    def setupUi(self, Movimiento):
        Movimiento.setObjectName("Movimiento")
        Movimiento.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Movimiento.resize(289, 259)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/../logo/Pempins.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Movimiento.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Movimiento)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelImporte = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelImporte.setFont(font)
        self.labelImporte.setObjectName("labelImporte")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelImporte)
        self.lineEditImporte = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditImporte.setFont(font)
        self.lineEditImporte.setObjectName("lineEditImporte")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditImporte)
        self.labelRazon = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelRazon.setFont(font)
        self.labelRazon.setObjectName("labelRazon")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelRazon)
        self.lineEditRazon = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditRazon.setFont(font)
        self.lineEditRazon.setObjectName("lineEditRazon")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditRazon)
        self.labelOrigen = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelOrigen.setFont(font)
        self.labelOrigen.setObjectName("labelOrigen")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelOrigen)
        self.comboBoxOrigen = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxOrigen.setFont(font)
        self.comboBoxOrigen.setObjectName("comboBoxOrigen")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBoxOrigen)
        self.labelFecha = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelFecha.setFont(font)
        self.labelFecha.setObjectName("labelFecha")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelFecha)
        self.dateEditFecha = QtWidgets.QDateEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEditFecha.setFont(font)
        self.dateEditFecha.setCalendarPopup(True)
        self.dateEditFecha.setObjectName("dateEditFecha")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEditFecha)
        self.labelDestino = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelDestino.setFont(font)
        self.labelDestino.setObjectName("labelDestino")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelDestino)
        self.comboBoxDestino = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxDestino.setFont(font)
        self.comboBoxDestino.setObjectName("comboBoxDestino")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBoxDestino)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Movimiento)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 200, 271, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonGuardarEnCache = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonGuardarEnCache.setFont(font)
        self.pushButtonGuardarEnCache.setObjectName("pushButtonGuardarEnCache")
        self.horizontalLayout.addWidget(self.pushButtonGuardarEnCache)
        self.pushButtonCancelar = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonCancelar.setFont(font)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)

        self.retranslateUi(Movimiento)
        QtCore.QMetaObject.connectSlotsByName(Movimiento)

    def retranslateUi(self, Movimiento):
        _translate = QtCore.QCoreApplication.translate
        Movimiento.setWindowTitle(_translate("Movimiento", "Movimiento"))
        self.labelImporte.setText(_translate("Movimiento", "Importe :"))
        self.labelRazon.setText(_translate("Movimiento", "Razon:"))
        self.labelOrigen.setText(_translate("Movimiento", "Origen:"))
        self.labelFecha.setText(_translate("Movimiento", "Fecha:"))
        self.dateEditFecha.setDisplayFormat(_translate("Movimiento", "dd/MM/yyyy"))
        self.labelDestino.setText(_translate("Movimiento", "Destino:"))
        self.pushButtonGuardarEnCache.setText(_translate("Movimiento", "Guardar en Caché"))
        self.pushButtonCancelar.setText(_translate("Movimiento", "Cancelar"))
