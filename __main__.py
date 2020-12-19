import pygame, view, controller, model

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    controller.control()
    model.move_sharik()
    view.paint()

