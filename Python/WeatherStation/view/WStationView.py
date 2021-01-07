# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WStation.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class WStationView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 310, 238, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setObjectName("gridLayout")
        self.tbtn_led = QtWidgets.QPushButton(self.layoutWidget)
        self.tbtn_led.setCheckable(True)
        self.tbtn_led.setObjectName("tbtn_led")
        self.gridLayout.addWidget(self.tbtn_led, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lbl_led = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_led.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_led.setObjectName("lbl_led")
        self.gridLayout.addWidget(self.lbl_led, 0, 1, 1, 1)
        self.lbl_motor = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_motor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_motor.setObjectName("lbl_motor")
        self.gridLayout.addWidget(self.lbl_motor, 0, 0, 1, 1)
        self.tbtn_motor = QtWidgets.QPushButton(self.layoutWidget)
        self.tbtn_motor.setCheckable(True)
        self.tbtn_motor.setObjectName("tbtn_motor")
        self.gridLayout.addWidget(self.tbtn_motor, 1, 0, 1, 1)
        self.lbl_temperature = QtWidgets.QLabel(self.centralwidget)
        self.lbl_temperature.setGeometry(QtCore.QRect(270, 70, 141, 20))
        self.lbl_temperature.setObjectName("lbl_temperature")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 170, 331, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tf_upFreq = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tf_upFreq.sizePolicy().hasHeightForWidth())
        self.tf_upFreq.setSizePolicy(sizePolicy)
        self.tf_upFreq.setObjectName("tf_upFreq")
        self.verticalLayout.addWidget(self.tf_upFreq)
        self.btn_upFreq = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upFreq.sizePolicy().hasHeightForWidth())
        self.btn_upFreq.setSizePolicy(sizePolicy)
        self.btn_upFreq.setObjectName("btn_upFreq")
        self.verticalLayout.addWidget(self.btn_upFreq, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ADDED CODE
        self.btn_upFreq.clicked.connect(self.onUpdateFreqBtnClicked)
        self.tbtn_led.clicked.connect(self.onLedBtnClicked)
        self.tbtn_motor.clicked.connect(self.onMotorBtnClicked)

    def onLedBtnClicked(self): pass
    def onMotorBtnClicked(self): pass
    def onUpdateFreqBtnClicked(self): pass


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tbtn_led.setText(_translate("MainWindow", "OFF"))
        self.lbl_led.setText(_translate("MainWindow", "LED"))
        self.lbl_motor.setText(_translate("MainWindow", "MOTOR"))
        self.tbtn_motor.setText(_translate("MainWindow", "OFF"))
        self.lbl_temperature.setText(_translate("MainWindow", "Temperature: ???"))
        self.btn_upFreq.setText(_translate("MainWindow", "Update"))
