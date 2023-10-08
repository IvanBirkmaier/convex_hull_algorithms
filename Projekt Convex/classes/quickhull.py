# coding: utf-8
from utils.utils import x_min_x_max, abstand_von_linie, linke_teile_punkte


class QuickHull:

    def __init__(self, points):
        self.points = points
        self.hull = []
        self.steps = []

    def visualisation(self):
        x_min, x_max = x_min_x_max(self.points)
        self.hull = [x_min, x_max]
        self.quickhull_visualsation(x_min, x_max, self.points)
        self.quickhull_visualsation(x_max, x_min, self.points)
        return self.hull, self.steps

    def performance(self):
        x_min, x_max = x_min_x_max(self.points)
        self.hull = [x_min, x_max]
        self.quickhull_performance(x_min, x_max, self.points)
        self.quickhull_performance(x_max, x_min, self.points)
        return self.hull

    def quickhull_performance(self, min, max, points):
        # Finde die Menge von Punkten, die links von der Linie von min nach max liegen
        linkeMenge = linke_teile_punkte(min, max, points)

        if not linkeMenge:  # Wenn die Menge leer ist, sind wir fertig für diese Iteration
            return

        weitester_punkt = self.max_distance_point_from_line(min, max, linkeMenge)

        # Fügen Sie den Punkt zur Hülle hinzu, direkt nach min
        index = self.hull.index(min)
        self.hull.insert(index + 1, weitester_punkt)

        # Teile das Problem auf und finde Hüllenpunkte für die Teilprobleme
        self.quickhull_performance(min, weitester_punkt, linkeMenge)
        self.quickhull_performance(weitester_punkt, max, linkeMenge)

    def quickhull_visualsation(self, min, max, points):
        # Finde die Menge von Punkten, die links von der Linie von min nach max liegen
        linkeMenge = linke_teile_punkte(min, max, points)

        if not linkeMenge:  # Wenn die Menge leer ist, sind wir fertig für diese Iteration
            return
        weitester_punkt = self.max_distance_point_from_line(min, max, linkeMenge)
        triangle = [min, max, weitester_punkt]

        # Fügen Sie den Punkt zur Hülle hinzu, direkt nach min
        index = self.hull.index(min)
        self.hull.insert(index + 1, weitester_punkt)
        self.steps.append(triangle)
        # Teile das Problem auf und finde Hüllenpunkte für die Teilprobleme
        self.quickhull_visualsation(min, weitester_punkt, linkeMenge)
        self.quickhull_visualsation(weitester_punkt, max, linkeMenge)

    def max_distance_point_from_line(self, min, max, points):
        max_abstand = float('-inf')
        weitester_punkt = None

        for p in points:
            abstand = abstand_von_linie(min, max, p)
            if abstand > max_abstand:
                max_abstand = abstand
                weitester_punkt = p

        return weitester_punkt
