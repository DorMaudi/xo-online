import socket
import sys
from MyWidget import *

IP = "127.0.0.1"
PORT = 8989

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((IP, PORT))
    except ConnectionRefusedError:
        print("unable to connect to the server!")
        exit()

    print("Connected to the server IP: {}, PORT: {}.".format(IP, PORT))

    # start app welcome screen.
    app = QtWidgets.QApplication([])

    widget = MyWidget(s)
    widget.setFixedSize(400, 300)
    widget.show()

    sys.exit(app.exec())
