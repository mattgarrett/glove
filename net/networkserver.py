#!/usr/bin/python2

#from __future__ import with_statment

import sys
import gflags
import socket
import threading
import signal
import SocketServer
import proto.net_pb2 as proto

FLAGS = gflags.FLAGS

gflags.DEFINE_string("host", None, "host to run the dedicated service on",
        short_name="h")
gflags.DEFINE_integer("port", None, "port to run the dedicated service on",
        short_name="p")

class GloveThreadedUDPHandler(SocketServer.DatagramRequestHandler):
    def handle(self):
        request, socket = self.getRequestAndSocket()
        manager = getNetworkServer()
        connections = manager.connections
        
        #deal with locking later
        #with lock:
        response = proto.Response()
        if (request.type == proto.Request.JOIN_GAME):
            #log that the user wants in
            #somehow assign a ID?
            connections.append([])
            response.id = len(connections) - 1
            response.type = proto.Response.OKAY
        elif (request.type == proto.Request.GET_STATE):
            connections[request.id] = request.moves
            response.id = request.id
            response.state = manager.getState()
            response.type = proto.Response.STATE
        elif (request.type == proto.Request.QUIT_GAME):
            connections[request.id] = "quit"
            response.response = proto.Response.OKAY
        else:
            print "unknown request: " + str(request)
            response = proto.Response()
            response.response = proto.Response.BAD
        
        socket.sendto(response.SerializeToString(), self.client_address)

    #returns the Request proto and the socket to respond with
    def getRequestAndSocket(self):
        request = proto.Request()
        request.ParseFromString(self.request[0].strip())
        return request, self.request[1]

class GloveThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

#A singleton for the server network manager.
#I can't really enforce the singleton pattern because
#I dont' know much about python.
instance = None
def getNetworkServer():
    global instance
    if (instance == None):
        instance = NetworkServer()
    return instance

#The server side of the network manager.
#It is expected that setState be called
#often with the state of the game.
#It is also expected that getRequests
#be called often.
class NetworkServer():
    def __init__(self):
        FLAGS(sys.argv)
        self.host = FLAGS.host
        self.port = FLAGS.port
        self.connections = []

        if not (self.host and self.port):
            raise Exception("must include flags --host and --port")
        
    # todo(matt): remove the state param here
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

    def getState(self):
        return self.state

    # use this to get things like players waiting to join
    # or moves that players have made
    def getRequests(self):
        tempConnections = []
        for x in self.connections:
            tempConnections.append(x)
        filter(lambda x: x != "quit", self.connections)
        return tempConnections
    
def main():
    server = getNetworkServer()
    state = proto.State()
    state.gameState = proto.State.INITIAL
    server.start(state)
    var = raw_input("Enter to exit...")
    server.stop()

if __name__ == "__main__":
    main()
