#!/usr/bin/python2

import sys
import signal
import time
import proto.net_pb2 as proto
import net.networkserver
        
#    def start(self, state):
#    def stop(self):
#    def setState(self, state):
#    def getRequests(self):

class State():
    def __init__(self):
        self.gamestate = "running"
        self.tick = 0

    def updateState(self, requests):
        self.tick = self.tick + 1

instance = None
def getServer():
    global instance
    if (instance == None):
        instance = Server()
    return instance

class Server():
    def __init__(self):
        self.state = State()
        self.server = net.networkserver.getNetworkServer()
        self.server.setState(self.state)

    def run(self):
        while (self.state.gamestate == "running"):
            requests = self.server.getRequests()
            self.state.updateState(requests)
            self.server.setState(self.state)
            time.sleep(1/60.0)
        #pause for clients to learn about shutdown
        time.sleep(5)

    def stop(self):
        self.state.gamestate = "stopped"

def signalHandler(signal, frame):
    print "got interrupt"
    server = getServer()
    server.stop()

def main():
    signal.signal(signal.SIGINT, signalHandler)
    server = getServer()
    server.run()

if __name__ == "__main__":
    main()
