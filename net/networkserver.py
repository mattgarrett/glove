#!/usr/bin/python2

import sys
import gflags
import socket
import threading
import signal
import SocketServer
import proto.state_pb2
import proto.request_pb2

FLAGS = gflags.FLAGS

gflags.DEFINE_string("host", None, "host to run the dedicated service on",
        short_name="h")
gflags.DEFINE_integer("port", None, "port to run the dedicated service on",
        short_name="p")

class GloveThreadedUDPHandler(SocketServer.DatagramRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        payload = proto.request_pb2.Request()
        payload.ParseFromString(data)
        socket = self.request[1]
        
        print "received:" + str(payload)
        response = payload #for now just echo the request
        
        print "response: " + str(response)
        socket.sendto(response.SerializeToString(), self.client_address)

class GloveThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

class NetworkServer():
    def __init__(self):
        FLAGS(sys.argv)
        self.host = FLAGS.host
        self.port = FLAGS.port

        if not (self.host and self.port):
            raise Exception("must include flags --host and --port")
        
    def start(self, state):        
        self.state = state

        self.server = GloveThreadedUDPServer((self.host, self.port), GloveThreadedUDPHandler)
        self.serverThread = threading.Thread(target=self.server.serve_forever)
        self.serverThread.daemon = False
        self.serverThread.start()

        print "...hosting dedicated server"
        print ".....host: " + self.host
        print ".....port: " + str(self.port)
    
    def stop(self):
        self.server.shutdown()

    def setState(self, state):
        #TODO(mattgarrett): figure out how to get state into the socket
        self.state = state
    
if __name__ == "__main__":
    server = GloveServer()
    state = proto.state_pb2.State()
    state.gameState = proto.state_pb2.State.INITIAL
    server.start(state)
    var = raw_input("Enter to exit...")
    server.stop()
