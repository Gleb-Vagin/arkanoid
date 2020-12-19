import pygame, model
from pygame import event, key

pygame.init()
key.set_repeat(10)


def control():
    new_events = event.get()
    for e in new_events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                model.move_platform_right()
            if e.key == pygame.K_a:
                model.move_platform_left()
