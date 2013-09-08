import pygame
import graphics
import screen

graphics.Initialize()

window = screen.Screen()
window.display()

rectangle = pygame.Surface((40, 40))
rectangle.fill((33, 66, 99))

i = 1000
while i > 0:
    i -= 1
    window.update()
    window.surface.blit(rectangle, (10, 10))
    graphics.UpdateScreen()
