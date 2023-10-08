# coding: utf-8

# returnt den min und den max Punkt aller Punkte von points.
# (Wenn zwei Punkte min oder max bezogen auf Ihre x koordinate darstellen, wird der erste nach Listenindex zurückgegeben).
def x_min_x_max(points):
    return min(points), max(points)

# Kreuzprodukt aus dem Internet
def kreuzprodukt(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

# Für Giftwrapping
def performance_finde_links_weitester_punkt(aktuellPunkt, punkte):
    nextPunkt = punkte[0]
    for p in punkte:
        if p == aktuellPunkt:
            continue
        kreuz = kreuzprodukt(aktuellPunkt, nextPunkt, p)
        if kreuz > 0 or (kreuz == 0 and distance(aktuellPunkt, p) > distance(aktuellPunkt, nextPunkt)):
            nextPunkt = p
    return nextPunkt

# Für Giftwrapping
def visualisation_finde_links_weitester_punkt(aktuellPunkt, punkte):
    nextPunkt = punkte[0]
    # steps wurden hinzugefügt um Liste die abfolge der Punkte aufnimmt.
    steps = []
    for p in punkte:
        if p == aktuellPunkt:
            continue
        kreuz = kreuzprodukt(aktuellPunkt, nextPunkt, p)
        if kreuz > 0 or (kreuz == 0 and distance(aktuellPunkt, p) > distance(aktuellPunkt, nextPunkt)):
            nextPunkt = p
            steps.append(nextPunkt)
    return nextPunkt, steps

# Für Giftwrapping
def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


#Für Quickhull
# Gibt die Linke Teilmenge der Punkte-Menge zurück
def linke_teile_punkte(min, max, punkte):
    menge = []
    for C in punkte:
        # min = A , max =B wie beim Dreieck
        cp = kreuzprodukt(min, max, C)
        if cp > 0:
            menge.append(C)  # C liegt links von AB
    return menge

#Für Quickhull
# Abstand berechnen zur linie ABC: ChatGPT
def abstand_von_linie(A, B, C):
    zaehler = abs((B[1]-A[1])*C[0] - (B[0]-A[0])*C[1] + B[0]*A[1] - B[1]*A[0])
    nenner = ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5
    return zaehler / nenner
