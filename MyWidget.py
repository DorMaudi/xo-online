import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.game_name = QtWidgets.QLabel("XO - Online", alignment=QtCore.Qt.AlignCenter)
        self.id_text = QtWidgets.QLabel("Username:", alignment=QtCore.Qt.AlignCenter)
        self.id_cont = QtWidgets.QLineEdit()
        self.id_cont.setPlaceholderText("username")
        self.pass_text = QtWidgets.QLabel("Password:", alignment=QtCore.Qt.AlignCenter)
        self.pass_cont = QtWidgets.QLineEdit()
        self.pass_cont.setPlaceholderText("password")
        self.pass_cont.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.game_name)
        self.layout.addWidget(self.id_text)
        self.layout.addWidget(self.id_cont)
        self.layout.addWidget(self.pass_text)
        self.layout.addWidget(self.pass_cont)
        self.layout.addWidget(self.login)

        self.login.clicked.connect(self.clk)

    @QtCore.Slot()
    def clk(self):
        self.login.setEnabled(False)
        print("ID: {}, Pass: {}".format(self.id_cont.text(), self.pass_cont.text()))