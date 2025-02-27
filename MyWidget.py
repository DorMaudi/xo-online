from PySide6 import QtCore, QtWidgets
import hashlib
import socket
import struct
from vendor.opcodes import *

class MyWidget(QtWidgets.QWidget):
    def __init__(self, sock: socket.socket):
        super().__init__()

        self.s = sock

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
        hash_obj = hashlib.sha256()
        hash_obj.update(self.pass_cont.text().encode('utf-8'))
        enc_pass = hash_obj.hexdigest()
        user_name_to_send = self.id_cont.text().encode('utf-8')
        password_to_send = enc_pass.encode('utf-8')
        #print("ID: {}, Pass: {}".format(self.id_cont.text(), self.pass_cont.text()))
        header = struct.pack(">2si", opcode["login"], 1024)
        self.s.sendall(header)