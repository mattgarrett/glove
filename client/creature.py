import sprite_handler
import time

class Creature(object):

    SPEED = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ticks = 0
        self.moving = False
        self.time = 0

    def moveLeft(self):
        self.x -= Creature.SPEED

    def moveRight(self):
        self.x += Creature.SPEED

    def moveUp(self):
        self.y -= Creature.SPEED

    def moveDown(self):
        self.y += Creature.SPEED

    def setTime(self, t):
        self.time = t

    def getSpriteName(self):
        breathing = int(self.time) % 2 == 0
        armSwings = int(self.moving) and (int(self.time * 4) % 2 == 0)
        return self.sprites[armSwings][breathing]

class Ghost(Creature):

    def __init__(self, x, y, spriteHandler):
        super(Ghost, self).__init__(x, y)
        self.sprites = [
                [sprite_handler.Sprites.GHOST11,
                    sprite_handler.Sprites.GHOST12],
                [sprite_handler.Sprites.GHOST21,
                    sprite_handler.Sprites.GHOST22]]

class AlexMiller(Creature):

    def __init__(self, x, y, spriteHandler):
        super(AlexMiller, self).__init__(x, y)
        self.sprites = [
                [sprite_handler.Sprites.ALEX_MILLER11,
                    sprite_handler.Sprites.ALEX_MILLER12],
                [sprite_handler.Sprites.ALEX_MILLER21,
                    sprite_handler.Sprites.ALEX_MILLER22]]
