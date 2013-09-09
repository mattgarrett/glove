#!/usr/bin/python2

import socket, sys
import gflags
import proto.request_pb2

FLAGS = gflags.FLAGS

gflags.DEFINE_string("host", None, "the server to connect to",
        short_name="h")
gflags.DEFINE_integer("port", None, "the port to connect on",
        short_name="p")

class Client:
    def __init__(self, argv):
        FLAGS(argv)
        self.host = FLAGS.host
        self.port = FLAGS.port

        if not (self.host and self.port):
            raise Exception("must include the flags --host and --port")

    def run(self):
        print "...joining server at"
        print ".....host: " + self.host
        print ".....port: " + str(self.port)

        request = proto.request_pb2.Request()
        request.type = proto.request_pb2.Request.INFO

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print "...connecting"
            sock.connect((self.host, self.port))
            sock.send(request.SerializeToString())

            received = sock.recv(1024)
            payload = proto.request_pb2.Request()
            payload.ParseFromString(received)
            print "...received: " + str(payload)
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
