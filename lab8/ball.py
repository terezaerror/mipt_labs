import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((226, 226, 210))

circle(screen, (0, 0, 0), (200, 200), 102, 1)
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (160, 180), 16)
circle(screen, (255, 0, 0), (240, 180), 20)
circle(screen, (0, 0, 0), (160, 180), 8)
circle(screen, (0, 0, 0), (240, 180), 10)
rect(screen, (0, 0, 0), (155, 240, 90, 15))
pygame.draw.line(screen, (0, 0, 0), (100, 140), (190, 170), 8)
pygame.draw.line(screen, (0, 0, 0), (300, 135), (215, 170), 8)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()