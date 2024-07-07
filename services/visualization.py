# coding: utf-8

import pygame
from pygame.locals import *
from classes.visualizer import Visualizer


# Methode eins zu eins wie Leo sie uns geschickt hat
def visualize(points_lst, coord_tresh, hull, giftwrp_steps, quickhull_steps):
    run = True
    clock = pygame.time.Clock()
    # only quadratic screens
    draw_info = Visualizer(800, 800, coord_tresh, points_lst, hull, giftwrp_steps, quickhull_steps)
    while run:
        clock.tick(60)
        draw_info.draw()
        pygame.display.update()

        for event in pygame.event.get():
            # for closing window
            if event.type == QUIT:
                run = False

            if event.type != KEYDOWN:
                continue

            if event.key == K_ESCAPE:
                run = False

            # Quickhull
            if event.key == K_q:
                draw_info.draw()
                draw_info.draw_quickhull()
                pygame.display.flip()

            # Giftwrapping
            if event.key == K_g:
                draw_info.draw()
                draw_info.draw_giftwrapping()
                pygame.display.flip()

    pygame.quit()
