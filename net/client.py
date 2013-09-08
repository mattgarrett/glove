#!/usr/bin/python2

import socket, sys
import gflags

FLAGS = gflags.FLAGS

gflags.DEFINE_string("host", None, "the server to connect to",
        short_name="h")
gflags.DEFINE_integer("port", None, "the port to connect on",
        short_name="p")
gflags.DEFINE_string("data", "Hello World", "the string to send to the server",
        short_name="d")

class Client:
    def __init__(self, argv):
        FLAGS(argv)
        self.host = FLAGS.host
        self.port = FLAGS.port
        self.data = FLAGS.data

        if not (self.host and self.port):
            raise Exception("must include the flags --host and --port")

    def run(self):
        print "...joining server at"
        print ".....host: " + self.host
        print ".....port: " + str(self.port)

        while True:
            try:
                sock = socket.socket()
                print "...connecting"
                sock.connect((self.host, self.port))
                sock.send(self.data)
                receivedData = sock.recv(1024)
                print "...received data:"
                print receivedData
                sock.close()
            except socket.error as e:
                if e.errno != socket.errno.ECONNREFUSED:
                    #some other error
                    raise e
                
def main():
    client = Client(sys.argv)
    client.run()

if __name__ == "__main__":
    main()
