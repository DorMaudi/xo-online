import socket
import struct
import sys
from MyWidget import *

IP = "192.168.50.52"
PORT = 8989

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((IP, PORT))
    except ConnectionRefusedError:
        print("unable to connect to the server!")
        exit()

    print("Connected to the server {}, {}.", IP, PORT)

    # start app welcome screen.
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
