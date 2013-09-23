#!/usr/bin/python2

import socket, sys
import gflags
import proto.net_pb2 as proto

FLAGS = gflags.FLAGS

gflags.DEFINE_string("host", None, "the server to connect to",
        short_name="h")
gflags.DEFINE_integer("port", None, "the port to connect on",
        short_name="p")

class NetworkClient:
    def __init__(self, argv):
        FLAGS(argv)
        self.host = FLAGS.host
        self.port = FLAGS.port

        if not (self.host and self.port):
            raise Exception("must include the flags --host and --port")

    def join(self):
        request = proto.Request()
        request.type = proto.Request.JOIN_GAME
        return self.sendRequestGetResponse(request)

    def quit(self):
        request = proto.Request()
        request.type = proto.Request.QUIT_GAME
        return self.sendRequestGetResponse(request)

    def sendMoveGetState(self, move):
        request = proto.Request()
        request.type = proto.Request.GET_STATE
        return self.sendRequestGetResponse(request)

    def sendRequestGetResponse(self, request):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print "...connecting"
            sock.connect((self.host, self.port))
            sock.send(request.SerializeToString())

            received = sock.recv(1024)
            response = proto.Response()
            response.ParseFromString(received)
            sock.close()
            return response
        except socket.error as e:
            if e.errno != socket.errno.ECONNREFUSED:
                #some other error
                raise e
            else:
                print "couldn't connect to server"
            return None

def main():
    client = NetworkClient(sys.argv)
    print str(client.join())

if __name__ == "__main__":
    main()
