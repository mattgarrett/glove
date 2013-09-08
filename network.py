#!/usr/bin/python2

import socket

class networkManager:
    def __init__(self, argv):
        if len(argv) < 2:
            raise Exception("netMan missing args")
        if not (argv[1] == "host" or argv[1] == "join" or argv[1] == "dedicated"):
            raise Exception("netMan bad argv[1]")
        
        self.mode = argv[1]
        if argv[1] == "join":
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

        elif argv[1] == "host":
            #TODO(mattgarrett): figure out how to host
            print("hosting...")
        else: #argv[1] == "dedicated"
            #TODO(mattgarrett): figure out how to dedicated host
            print("dedicated hosting...")
            self.s = socket.socket()
            host = socket.gethostbyname(socket.gethostname())
            port = 12345
            print host
            self.s.bind((host, port))
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

    
