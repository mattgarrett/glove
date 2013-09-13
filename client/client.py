import pygame
import graphics
import screen
import sprite_handler
import time

graphics.Initialize()

window = screen.Screen()
window.display()

rectangle = pygame.Surface((40, 40))
rectangle.fill((33, 66, 99))

spriteHandler = sprite_handler.SpriteHandler("client/resources/sprites/")

i = 1000
while i > 0:
    i -= 1

    stoneTileSprite = spriteHandler.getSprite(sprite_handler.Sprites.STONE_TILE)
    for x in range(0, 20):
        for y in range(0, 15):
            window.surface.blit(stoneTileSprite, (10 + 32 * x, 10 + 32 * y))

    window.update()
    graphics.UpdateScreen()
    time.sleep(0.1)
