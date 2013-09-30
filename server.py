#!/usr/bin/python2

import sys
import signal
import time
import proto.net_pb2 as proto
import net.networkserver
import state.statemanager

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
        self.stateManager = state.statemanager.getStateManager()
        self.networkManager = net.networkserver.getNetworkServer()

    def run(self):
        state = self.stateManager.getState()
        while (state.gameState == "running"):
            requests = self.networkManager.getRequests()
            self.stateManager.updateState(requests)
            state = self.stateManager.getState()
            self.networkManager.setState(state)
            time.sleep(1/60.0)
        #pause for clients to learn about shutdown
        time.sleep(5)

    def stop(self):
        self.stateManager.stop()

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
