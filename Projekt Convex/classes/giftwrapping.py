# coding: utf-8
from utils.utils import x_min_x_max, \
    performance_finde_links_weitester_punkt,visualisation_finde_links_weitester_punkt


class GiftWrapping:

    def __init__(self, points):
        self.points = points
        self.hull = []

    def _initialize_hull(self):
        x_min, _ = x_min_x_max(self.points)
        self.hull = [x_min]

    # Performance Algorithmus um mit CProfil die Steps zu messen.
    def performance(self):
        self._initialize_hull()
        while True:
            next_point = performance_finde_links_weitester_punkt(self.hull[-1], self.points)
            if next_point == self.hull[0]:  # Überprüfung, ob wir zur Startposition zurückgekehrt sind
                break
            self.hull.append(next_point)
        return self.hull

    # Für die Visualisierung des Algorithmus
    def visualisation(self):
        self._initialize_hull()
        steps = []
        while True:
            next_point, step = visualisation_finde_links_weitester_punkt(self.hull[-1], self.points)
            if next_point == self.hull[0]:  # Überprüfung ob wir wieder am ersten Punkt x_min der Hülle angekommen sind.
                break
            self.hull.append(next_point)
            steps.append(step)
        return self.hull, steps
