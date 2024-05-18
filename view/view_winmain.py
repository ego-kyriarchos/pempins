# Form implementation generated from reading ui file 'view/view_winmain.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 578)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/../logo/Pempins.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.botonIngresar = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botonIngresar.setFont(font)
        self.botonIngresar.setObjectName("botonIngresar")
        self.verticalLayout.addWidget(self.botonIngresar)
        self.botonGastar = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botonGastar.setFont(font)
        self.botonGastar.setObjectName("botonGastar")
        self.verticalLayout.addWidget(self.botonGastar)
        self.botonMover = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botonMover.setFont(font)
        self.botonMover.setObjectName("botonMover")
        self.verticalLayout.addWidget(self.botonMover)
        self.botonGuardarCambios = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botonGuardarCambios.setFont(font)
        self.botonGuardarCambios.setObjectName("botonGuardarCambios")
        self.verticalLayout.addWidget(self.botonGuardarCambios)
        self.botonVerMonedero = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botonVerMonedero.setFont(font)
        self.botonVerMonedero.setObjectName("botonVerMonedero")
        self.verticalLayout.addWidget(self.botonVerMonedero)
        self.botonSalir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botonSalir.setGeometry(QtCore.QRect(430, 540, 71, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botonSalir.setFont(font)
        self.botonSalir.setObjectName("botonSalir")
        self.textoHistorial = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.textoHistorial.setGeometry(QtCore.QRect(210, 170, 291, 361))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textoHistorial.setFont(font)
        self.textoHistorial.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.textoHistorial.setObjectName("textoHistorial")
        self.versionPempins = QtWidgets.QLabel(parent=self.centralwidget)
        self.versionPempins.setGeometry(QtCore.QRect(210, 530, 71, 20))
        self.versionPempins.setObjectName("versionPempins")
        self.boxBusquedaPorFecha = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.boxBusquedaPorFecha.setGeometry(QtCore.QRect(210, 30, 301, 131))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.boxBusquedaPorFecha.setFont(font)
        self.boxBusquedaPorFecha.setObjectName("boxBusquedaPorFecha")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.boxBusquedaPorFecha)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.FechaDesde = QtWidgets.QDateEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.FechaDesde.setFont(font)
        self.FechaDesde.setCalendarPopup(True)
        self.FechaDesde.setObjectName("FechaDesde")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.FechaDesde)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.FechaHasta = QtWidgets.QDateEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.FechaHasta.setFont(font)
        self.FechaHasta.setCalendarPopup(True)
        self.FechaHasta.setObjectName("FechaHasta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.FechaHasta)
        self.botonBuscar = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.botonBuscar.setFont(font)
        self.botonBuscar.setObjectName("botonBuscar")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.botonBuscar)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(190, 10, 16, 561))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.textoMonedero = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.textoMonedero.setGeometry(QtCore.QRect(10, 260, 171, 311))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textoMonedero.setFont(font)
        self.textoMonedero.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.textoMonedero.setObjectName("textoMonedero")
        self.labelHistorial = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelHistorial.setGeometry(QtCore.QRect(210, 10, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHistorial.setFont(font)
        self.labelHistorial.setObjectName("labelHistorial")
        self.githubPempins = QtWidgets.QLabel(parent=self.centralwidget)
        self.githubPempins.setGeometry(QtCore.QRect(210, 550, 191, 20))
        self.githubPempins.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Spanish, QtCore.QLocale.Country.Spain))
        self.githubPempins.setObjectName("githubPempins")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pempins"))
        self.botonIngresar.setText(_translate("MainWindow", "Ingresar"))
        self.botonGastar.setText(_translate("MainWindow", "Gastar"))
        self.botonMover.setText(_translate("MainWindow", "Mover"))
        self.botonGuardarCambios.setText(_translate("MainWindow", "Guardar Cambios"))
        self.botonVerMonedero.setText(_translate("MainWindow", "Ver monedero"))
        self.botonSalir.setText(_translate("MainWindow", "Salir"))
        self.versionPempins.setText(_translate("MainWindow", "Pempins: v1"))
        self.boxBusquedaPorFecha.setTitle(_translate("MainWindow", "Buscar movimientos por fecha:"))
        self.label_2.setText(_translate("MainWindow", "Desde:"))
        self.FechaDesde.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.label_3.setText(_translate("MainWindow", "Hasta:"))
        self.FechaHasta.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.botonBuscar.setText(_translate("MainWindow", "Buscar"))
        self.textoMonedero.setPlainText(_translate("MainWindow", "Ahorro:\n"
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
"  xxxx€"))
        self.labelHistorial.setText(_translate("MainWindow", "Historial:"))
        self.githubPempins.setText(_translate("MainWindow", "Github: ego-kyriarchos/pempins"))
