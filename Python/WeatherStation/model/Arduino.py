from serial import Serial
from threading import Thread
from time import sleep


class Arduino:
    def __init__(self, com, br):
        self.port = Serial(port=com, baudrate=br, timeout=0.1)
        self.thread = Thread(target=self.listenSerialPort, daemon=True)
        self.thread.start()


    def listenSerialPort(self):
        while True:
            if self.port.in_waiting > 0:
                dataIn = self.port.read_until('\n').decode("utf-8")
                self.onMessageReceived(dataIn)
            sleep(1)

    def sendMessage(self, msg):
        self.port.write(msg.encode())

    def onMessageReceived(self, msg):
        print(msg)
