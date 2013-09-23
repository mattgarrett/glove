
def Load(filename):
    f = open(filename, "r")
    room = Room(f.readlines())
    f.close()
    return room

class Room(object):

    def __init__(self, tiles):
        self.tiles = tiles

    def getWidth(self):
        return len(self.tiles[0])

    def getHeight(self):
        return len(self.tiles)

    def getObject(self, x, y):
        return self.tiles[y][x]
