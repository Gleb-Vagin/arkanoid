import pygame, settings as set

platforma = pygame.Rect(100, set.SCREEN_HEIGHT - 100, 100, 25)
platforma.centerx = set.SCREEN_WIDTH / 2

sharik = pygame.Rect(50, 50, 50, 50)

speed_x = 3
speed_y = -3


def move_platform_right():
    platforma.x += 5
    if platforma.right > set.SCREEN_WIDTH:
        platforma.right = set.SCREEN_WIDTH


def move_platform_left():
    platforma.x -= 5
    if platforma.left < 0:
        platforma.left = 0


def move_sharik():
    global speed_x, speed_y
    sharik.x += speed_x
    if sharik.right > set.SCREEN_WIDTH:
        sharik.right = set.SCREEN_WIDTH
        speed_x = - speed_x
    if sharik.left < 0:
        sharik.left = 0
        speed_x = - speed_x
    sharik.y += speed_y
    if sharik.top < 0:
        sharik.top = 0
        speed_y = - speed_y
