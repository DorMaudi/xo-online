import socket
import struct

PORT = 8989

live_connections = {} # connection, addr

def handle_client(con: socket.socket):
    while True:
        data = con.recv(6)
        op, size = struct.unpack(">2si", data)
        print("op: {}, data: {}".format(op, int(data)))

if __name__ == '__main__':
    s = socket.socket()
    print ("Socket successfully created")
 
    s.bind(('', PORT))
    print ("socket binded to {}".format(PORT))

    s.listen()
    print ("socket is listening")

    while True:
        c, addr = s.accept()
        print ('user connected from', addr)
        live_connections[c] = addr
        handle_client(c)