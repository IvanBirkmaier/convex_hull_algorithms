# coding: utf-8
import pygame
import time

pygame.init()


class Visualizer:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    FONT = pygame.font.SysFont('comicsans', 30)
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        GREY,
        (160, 160, 160),
        (192, 192, 192)
    ]

    PAD = 50

    def __init__(self, width, height, coord_tresh, lst_points, hull, giftwrp_steps, quickhull_steps):
        self.lst = []
        self.hull = []
        self.giftwrp_steps = []
        self.quickhull_steps = []
        self.width = width
        self.height = height
        self.menue = self.FONT.render("Q for Quickhull | G for Giftwrapping | ESC for ending after run",1, self.BLACK)

        self.transform = (width - self.PAD) / coord_tresh

        self.window = pygame.display.set_mode((width, height))

        # # Schriftart erstellen
        # font_size = 36
        # font = pygame.font.Font(None, font_size)
        # # Text rendern und anzeigen
        # text_surface = font.render("Hallo, Pygame!", True, (0, 0, 0))  # Der Text, Anti-Aliasing, Textfarbe
        # text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2))  # Zentriert den Text auf dem Bildschirm
        # self.window.blit(text_surface, text_rect)

        pygame.display.set_caption("Convex Hull Algorithm Visualization")
        self.set_list(lst_points)
        self.hull = self.transform_hull(hull)
        self.giftwrp_steps = self.transform_steps(giftwrp_steps)
        self.quickhull_steps = self.transform_steps(quickhull_steps)

    def set_list(self, lst):
        for p in lst:
            x = (self.width // 2) + ((int(p[0]) * self.transform) / 2)
            y = (self.height // 2) + ((int(p[1]) * self.transform) / 2)
            self.lst.append([x, y])

    def transform_hull(self, lst):
        transformed_hull = []
        for p in lst:
            x = (self.width // 2) + ((int(p[0]) * self.transform) / 2)
            y = (self.height // 2) + ((int(p[1]) * self.transform) / 2)
            transformed_hull.append([x, y])
        return transformed_hull

    def transform_steps(self, lst):
        transformed_steps = []
        for li in lst:
            transform_step = []
            for p in li:
                x = (self.width // 2) + ((int(p[0]) * self.transform) / 2)
                y = (self.height // 2) + ((int(p[1]) * self.transform) / 2)
                transform_step.append([x, y])
            transformed_steps.append(transform_step)
        return transformed_steps

    def draw(self):
        self.window.fill(self.BACKGROUND_COLOR)
        self.window.blit(self.menue, (self.width/2 - self.menue.get_width()/2 , 5))
        self.draw_points()

    def draw_points(self):
        lst = self.lst
        for index, p in enumerate(lst):
            pygame.draw.circle(self.window, self.GREEN, (p[0], p[1]), 10)

    def draw_lines(self, lst):
        for index, point in enumerate(lst):
            if index < (len(lst) - 1):
                point2 = lst[index + 1]
            else:
                point2 = lst[-1]
            pygame.draw.line(self.window, self.RED, point, point2, 3)

    def draw_giftwrapping(self):
        hull_color = (0, 200, 200)
        end = 1

        for index, point in enumerate(self.hull):
            if index < (len(self.hull) - 1):
                point2 = self.hull[index + 1]
            else:
                point2 = self.hull[0]

            if index != len(self.hull) - 1:
                for p in self.giftwrp_steps[index]:
                    pygame.draw.line(self.window, hull_color, point, p, 2)
                    self.draw_lines(self.hull[:end])
                    self.draw_points()
                    pygame.display.flip()
                    self.window.fill(self.BACKGROUND_COLOR)
                    self.window.blit(self.menue, (self.width / 2 - self.menue.get_width() / 2, 5))
                    self.draw_lines(self.hull[:end])
                    if end == len(self.giftwrp_steps):
                        self.draw_lines(self.hull[:end + 1])
                    self.draw_points()
                    pygame.time.delay(200)

                end += 1

            if point2 == self.hull[0]:
                pygame.draw.line(self.window, self.RED, point, point2, 3)
                self.draw_points()
                pygame.display.flip()
                pygame.time.delay(2000)

    def draw_quickhull(self):
        line_Color = [(0, 200, 200), (255, 255, 255)]
        thickness = [3, 7]
        durchlauf = 0
        lastStep = []
        for pts in self.quickhull_steps:
            lastStep.append(pts)
            while durchlauf < 2:
                if pts == self.quickhull_steps[0]:
                    # Hauptline Min-Max DIE ALLER ERSTE
                    pygame.draw.line(self.window, self.BLACK, pts[0], pts[1], thickness[0])
                else:
                    # Hauptlinie A-B von für jedes Dreieck
                    if durchlauf == 0:
                        pygame.draw.line(self.window, line_Color[0], pts[0], pts[1], thickness[0])
                    if durchlauf == 1:
                        pygame.draw.line(self.window, line_Color[1], pts[0], pts[1], thickness[1])
                # Linie von B - C
                pygame.draw.line(self.window, line_Color[0], pts[1], pts[2], thickness[0])
                # Linie C-A
                pygame.draw.line(self.window, line_Color[0], pts[2], pts[0], thickness[0])
                self.draw_points()
                pygame.display.flip()
                durchlauf = durchlauf + 1
                pygame.time.delay(300)
            pygame.time.delay(500)
            durchlauf = 0
            if pts == self.quickhull_steps[-1]:
                # damit man noch die letzte veränderung sieht
                self.draw_points()
                pygame.display.flip()
                pygame.time.delay(2000)
            pygame.display.flip()
