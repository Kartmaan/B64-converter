# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(802, 593)
        MainWindow.setMinimumSize(QtCore.QSize(802, 593))
        MainWindow.setMaximumSize(QtCore.QSize(802, 593))
        MainWindow.setWindowTitle("Base64 Converter")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        # Input box
        self.input_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.input_box.setGeometry(QtCore.QRect(10, 60, 321, 431))
        self.input_box.setReadOnly(False)
        self.input_box.setAcceptRichText(False)
        self.input_box.setObjectName("input_box")

        # Output box
        self.output_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_box.setGeometry(QtCore.QRect(450, 60, 341, 431))
        self.output_box.setObjectName("output_box")
        self.output_box.setText("<Result will appear here>")

        # Label INPUT
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(80, 35, 171, 21))
        self.label_input.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input.setObjectName("label")

        # Label OUTPUT
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(540, 35, 171, 21))
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_2")

        # Bouton CODE
        self.button_code = QtWidgets.QPushButton(self.centralwidget)
        self.button_code.setGeometry(QtCore.QRect(340, 220, 101, 41))
        self.button_code.setObjectName("pushButton")
        self.button_code.setText("CODE")

        # Bouton DECODE
        self.button_decode = QtWidgets.QPushButton(self.centralwidget)
        self.button_decode.setGeometry(QtCore.QRect(340, 300, 101, 41))
        self.button_decode.setObjectName("pushButton_2")
        self.button_decode.setText("DECODE")

        # Bouton COPY
        self.button_copy = QtWidgets.QPushButton(self.centralwidget)
        self.button_copy.setGeometry(QtCore.QRect(580, 495, 80, 21))
        self.button_copy.setObjectName("pushButton_3")
        self.button_copy.setText("Copy")

        # Groupbox Status message
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 513, 781, 61)) # 10, 490, 781, 61
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Status message")
        self.groupBox.setEnabled(True)

        # Label Status message
        self.label_status = QtWidgets.QLabel(self.groupBox) # Encré sur groupBox
        self.label_status.setGeometry(QtCore.QRect(20, 20, 731, 31))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_status.setObjectName("label_4")

        # Label title
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(305, 10, 180, 31))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">INPUT</span></p></body></html>"))
        self.label_output.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">OUTPUT</span></p></body></html>"))
        self.label_status.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\"></span></p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Base64 Converter</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())