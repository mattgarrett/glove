#!/usr/bin/python2

import socket

class networkManager:
    def __init__(self, mode, ip, port):
        self.mode = mode
        if mode == "join":
            #TODO(mattgarrett): figure out how to join
            print("joining...")
            host = "127.0.1.1"
            port = 12345
            self.s = socket.socket()
            self.s.connect((host, port))
            self.s.send("Hello")
            data = self.s.recv(1024)
            print data
            self.s.close()

        elif mode == "host":
            #TODO(mattgarrett): figure out how to host
            print("hosting...")
        else: #mode == "dedicated"
            #TODO(mattgarrett): figure out how to dedicated host
            print("dedicated hosting...")
            self.s = socket.socket()
            print host
            self.s.bind((ip, port))
            self.s.listen(5)
            while True:
                print "trying for connection..."
                connection, address = self.s.accept()
                data = connection.recv(1024)
                if not data: break
                connection.send(data)
                print data
                connection.close()

    def getMode(self):
        return self.mode

    
