#!/usr/bin/python2

import sys
import signal
import time
import proto.net_pb2 as proto
import net.networkclient


def signalHandler(signal, frame):
    print "got interrupt"
    server = getServer()
    server.stop()

class Move():
    def __init__(self, idNum):
        self.id = idNum

def main():
    signal.signal(signal.SIGINT, signalHandler)


    client = net.networkclient.getClient()
    joinResponse = client.join()
    #remember the joinResponse.id
    print (joinResponse)
    move = Move(joinResponse.id)
    move.up = True
    move.right = True
    move.left = False
    move.down = False
    sendMoveGetStateResponse = client.sendMoveGetState(move)
    print (sendMoveGetStateResponse)
    quitResponse = client.quit()
    print (quitResponse)

if __name__ == "__main__":
    main()
