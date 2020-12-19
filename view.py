import pygame
from pygame import draw, display, image, transform
import settings as set, model

pygame.init()
screen = display.set_mode([set.SCREEN_WIDTH, set.SCREEN_HEIGHT])
platforma = image.load('kartinki/genesis_sonicthehedgehog.png')
platforma = transform.scale(platforma, model.platforma.size)


def paint():
    screen.fill([0, 0, 0])
    screen.blit(platforma, model.platforma)
    draw.circle(screen, [0, 0, 255], model.sharik.center, model.sharik.w / 2)
    display.flip()
