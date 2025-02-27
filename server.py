import socket
import struct

PORT = 8989

def e_send():
    pass

def e_recv():
    pass

if __name__ == '__main__': 
    s = socket.socket()		 
    print ("Socket successfully created")
 
    s.bind(('', PORT))		 
    print ("socket binded to %s" %(PORT)) 

    s.listen()	 
    print ("socket is listening")		 

    while True: 
        c, addr = s.accept()	 
        print ('Got connection from', addr )
        



