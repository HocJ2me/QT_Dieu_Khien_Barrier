# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtCore import QFile, QTimer
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QPixmap


import time
import json
import serial
from pprint import pprint
import random

ser  = serial.Serial("COM8", baudrate= 9600,
       timeout=2.5,
       parity=serial.PARITY_NONE,
       bytesize=serial.EIGHTBITS,
       stopbits=serial.STOPBITS_ONE
    )


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        #../barrier_close.png
        self.picBarrier = self.findChild(QLabel, "imgApp")
        self.imClose = QPixmap("../barrier_close.png")
        self.imOpen = QPixmap("../barrier_open.png")
        self.picBarrier.setPixmap(self.imOpen)

        self.timer = QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(20)


    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
    def read_data(self):
        global ser
        serialLine = "";
        if ser.isOpen():
            serialLine = ser.read(50).decode('ascii')
            if (serialLine.find("{\"status\":\"close\"}") >= 0):
                self.picBarrier.setPixmap(self.imClose)
                print(serialLine)
            else:
                self.picBarrier.setPixmap(self.imOpen)



if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
