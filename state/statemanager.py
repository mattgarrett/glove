#!/usr/bin/python2

instance = None
def getStateManager():
    global instance
    if (instance == None):
        instance = StateManager()
    return instance

class State():
    def __init__(self):
        self.gameState = "running"
        self.sizeX = 10
        self.sizeY = 10
        self.tick = 0
        self.players = []
        self.monsters = []

class StateManager():
    def __init__(self):
        self.state = State()

    def updateState(self, actions):
        self.state.tick = self.state.tick + 1
    
    def getState(self):
        return self.state

    def stop(self):
        self.state.gameState = "stopped"
