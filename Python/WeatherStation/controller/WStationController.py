import sys
import types
from PyQt5 import QtWidgets
from model.Arduino import Arduino
from model.WStationQueries import Queries
from view.WStationView import WStationView


def newArduinoMessage(msg):
    msg = msg[:-2]
    view.lbl_temperature.setText("Temperature: " + msg)
    queries.addMeasurement(msg)


def setMotorState(obj):
    if obj.tbtn_motor.isChecked():
        obj.tbtn_motor.setText("ON")
        arduino.sendMessage("M1")
    else:
        obj.tbtn_motor.setText("OFF")
        arduino.sendMessage("M0")


def setLedState(obj):
    if obj.tbtn_led.isChecked():
        obj.tbtn_led.setText("ON")
        arduino.sendMessage("L1")
    else:
        obj.tbtn_led.setText("OFF")
        arduino.sendMessage("L0")


def setUpdateFrequency(obj):
    arduino.sendMessage("F" + obj.tf_upFreq.text())
    obj.tf_upFreq.clear()


queries = Queries()

arduino = Arduino('COM2', 9600)
arduino.onMessageReceived = newArduinoMessage

app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
view = WStationView()
view.onLedBtnClicked = types.MethodType(setLedState, view)
view.onMotorBtnClicked = types.MethodType(setMotorState, view)
view.onUpdateFreqBtnClicked = types.MethodType(setUpdateFrequency, view)
view.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
