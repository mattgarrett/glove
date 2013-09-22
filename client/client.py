import pygame
import graphics
import screen
import sprite_handler
import time
import room

graphics.Initialize()

window = screen.Screen()
window.display()

rectangle = pygame.Surface((40, 40))
rectangle.fill((33, 66, 99))

spriteHandler = sprite_handler.SpriteHandler("client/resources/sprites/")
stoneTileSprite = spriteHandler.getSprite(sprite_handler.Sprites.STONE_TILE)
woodenBoxSprite = spriteHandler.getSprite(sprite_handler.Sprites.WOODEN_BOX)

room = room.Load("client/resources/rooms/first.room")

alexMiller = [
        [sprite_handler.Sprites.ALEX_MILLER11,
            sprite_handler.Sprites.ALEX_MILLER12],
        [sprite_handler.Sprites.ALEX_MILLER21,
            sprite_handler.Sprites.ALEX_MILLER22]]

steps = 0
alex_miller_x = 3
alex_miller_y = 3

i = 1000
while True:
    i -= 1

    armSwings = int(steps % 2 == 0)
    breathing = int(int(time.time()) % 2 == 0)

    alexMillerSprite = spriteHandler.getSprite(alexMiller[armSwings][breathing])

    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        steps += 1
        if event.key == pygame.K_DOWN:
            alex_miller_y += 1
        elif event.key == pygame.K_UP:
            alex_miller_y -= 1
        elif event.key == pygame.K_LEFT:
            alex_miller_x -= 1
        elif event.key == pygame.K_RIGHT:
            alex_miller_x += 1

    for x in range(0, room.getWidth() - 1):
        for y in range(0, room.getHeight()):
            obj = room.getObject(x, y)
            if obj == "#":
                window.surface.blit(woodenBoxSprite, (10 + 32 * x, 10 + 32 * y))
            else:
                window.surface.blit(stoneTileSprite, (10 + 32 * x, 10 + 32 * y))

    window.surface.blit(alexMillerSprite, (10 + 32 * alex_miller_x, 10 + 32 * alex_miller_y))

    window.update()
    graphics.UpdateScreen()
    time.sleep(0.1)
