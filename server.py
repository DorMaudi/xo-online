import socket
import struct

PORT = 8989

def e_send():
    pass

def e_recv():
    pass

if __name__ == '__main__':
    # next create a socket object 
    s = socket.socket()		 
    print ("Socket successfully created")

    # we have not typed any ip in the ip field 
    # instead we have inputted an empty string 
    # this makes the server listen to requests 
    # coming from other computers on the network 
    s.bind(('', PORT))		 
    print ("socket binded to %s" %(PORT)) 

    # put the socket into listening mode 
    s.listen()	 
    print ("socket is listening")		 

    # a forever loop until we interrupt it or 
    # an error occurs 
    while True: 
        # Establish connection with client. 
        c, addr = s.accept()	 
        print ('Got connection from', addr )

        # send a thank you message to the client. encoding to send byte type. 
        c.send('Thank you for connecting'.encode()) 

        # Close the connection with the client 
        c.close()

        # Breaking once connection closed
        break



