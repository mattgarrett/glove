#!/usr/bin/python2

import socket, sys
import gflags

FLAGS = gflags.FLAGS

gflags.DEFINE_string("host", None, "host to run the dedicated service on",
        short_name="h")
gflags.DEFINE_integer("port", None, "port to run the dedicated service on",
        short_name="p")

class Server:
    def __init__(self, argv):
        FLAGS(argv)
        self.host = FLAGS.host
        self.port = FLAGS.port

        if not (self.host and self.port):
            raise Exception("must include flags --host and --port")

    def run(self):
        print "...hosting dedicated server"
        print ".....host: " + self.host
        print ".....port: " + str(self.port)

        self.s = socket.socket()
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        while True:
            print "...accepting connection"
            connection, address = self.s.accept()
            data = connectio.recv(1024)
            if not data:
                break
            print "...received data:"
            print data
            connection.send(data)
            connection.close()

def main():
    server = Server(sys.argv)
    server.run()

if __name__ == "__main__":
    main()
