"""
phase5_gotcha_labs - Bitwise Gotchas

TODO: lesson description and instructions.
"""
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bitwise Gotchas")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    # TODO: update and draw

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
