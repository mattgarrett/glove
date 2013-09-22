import pygame
import graphics
import screen
import sprite_handler
import time
import room
import creature

graphics.Initialize()

window = screen.Screen()
window.display()

rectangle = pygame.Surface((40, 40))
rectangle.fill((33, 66, 99))

spriteHandler = sprite_handler.SpriteHandler("client/resources/sprites/")
stoneTileSprite = spriteHandler.getSprite(sprite_handler.Sprites.STONE_TILE)
woodenBoxSprite = spriteHandler.getSprite(sprite_handler.Sprites.WOODEN_BOX)

alexMillerCreature = creature.AlexMiller(3, 3, spriteHandler)
ghost = creature.Ghost(60, 60, spriteHandler)

room = room.Load("client/resources/rooms/first.room")
key = None

i = 1000
while True:
    i -= 1

    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        key = event.key
        alexMillerCreature.moving = True
    elif event.type == pygame.KEYUP:
        key = None
        alexMillerCreature.moving = False

    if key:
        if key == pygame.K_DOWN:
            alexMillerCreature.moveDown()
        if key == pygame.K_UP:
            alexMillerCreature.moveUp()
        if key == pygame.K_LEFT:
            alexMillerCreature.moveLeft()
        if key == pygame.K_RIGHT:
            alexMillerCreature.moveRight()

    for x in range(0, room.getWidth() - 1):
        for y in range(0, room.getHeight()):
            obj = room.getObject(x, y)
            if obj == "#":
                window.surface.blit(woodenBoxSprite, (10 + 32 * x, 10 + 32 * y))
            else:
                window.surface.blit(stoneTileSprite, (10 + 32 * x, 10 + 32 * y))

    alexMillerCreature.setTime(time.time())
    ghost.setTime(time.time())

    window.surface.blit(spriteHandler.getSprite(alexMillerCreature.getSpriteName()), (
        alexMillerCreature.x, alexMillerCreature.y))
    window.surface.blit(spriteHandler.getSprite(ghost.getSpriteName()), (
        ghost.x, ghost.y))

    window.update()
    graphics.UpdateScreen()
    time.sleep(0.05)
