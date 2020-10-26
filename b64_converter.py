# -*- coding: utf-8 -*-

import sys
import base64 # Base64 algo
import binascii # Catch error
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from window import Ui_MainWindow
import pyperclip # Clipboard

__author__ = "Kartmaan"
__version__ = "1.0"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Link widgets to their functions
        self.button_code.clicked.connect(self.code_button)
        self.button_decode.clicked.connect(self.decode_button)
        self.button_copy.clicked.connect(self.copy_button)    

    def code_button(self):
        # Code button behaviour
        # Code to base64
        input = self.input_box.toPlainText() # Extract the input
        code = input.encode("utf-8")
        code = base64.b64encode(code)
        output = code.decode("utf-8")
        self.output_box.setText(output)

        if len(input) == 0:
            self.label_status.setText("NO ENTRY")
        if input == "Chewbacca":
            self.label_status.setText("UUrrggHHHHggGGGhhhHHH !")
        else :
            self.label_status.setText("Successful coded")
    
    def decode_button(self):
        # Decode button behaviour
        # Decode from base64
        input = self.input_box.toPlainText() # Extract the input
        try :
            code = base64.b64decode(input)
            output = code.decode("utf-8")
            self.output_box.setText(output)

            if len(input) == 0 :
                self.label_status.setText("NO ENTRY")
            if input == "Q2hld2JhY2Nh":
                self.label_status.setText("UUrrggHHHHggGGGhhhHHH !")
            else :
                self.label_status.setText("Successful decoded")

        except binascii.Error :
            self.label_status.setText("ERROR - INVALID B64 CODE (binascii.Error)")
        except UnicodeDecodeError :
            self.label_status.setText("ERROR - INVALID B64 CODE (UnicodeDecodeError)")
        except ValueError :
            self.label_status.setText("ERROR - INVALID B64 CODE (ValueError)")

    def copy_button(self) :
        # Copy button behaviour
        x = self.output_box.toPlainText()
        pyperclip.copy(x)
        self.label_status.setText("Copied to clipboard")

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) # []
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_()) # app.exec()