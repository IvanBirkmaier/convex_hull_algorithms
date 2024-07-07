# ConvexHull
This is a simple example for the implementation and visualization of the gitwrapping and the quickhull algohrithms. Everything is coded in python.
The code an the readme for the project setup is in the project folder. 
# Setup

## Python Environment

Es wird empfohlen, eine Python-Umgebung mit Conda zu verwenden.

## Installation von Pygame

Nachdem Sie Ihr Conda-Environment eingerichtet haben, können Sie Pygame mit dem folgenden Befehl installieren:

pip install pygame


# Anleitung

## 1. Starten des Programms 

Führen Sie die Hauptdatei  `main.py` aus, um das Programm zu starten.

## 2. Auswahl des Modus

- **Performance Modus**: Beide Algorithmen, Quickhull und Giftwrapping, werden hinsichtlich ihrer Performance gemessen. Das Ergebnis wird über die Konsole ausgegeben.

- **Visualisierungs Modus**: Hier wird die Funktionsweise der Algorithmen visualisiert. Ein neues Fenster wird geöffnet, in dem Sie die Algorithmen in Aktion sehen können.

## 3. Datenquelle auswählen 

Sie haben die Möglichkeit, entweder zufällig generierte Punkte zu verwenden oder ein CSV-File mit Datenpunkten einzulesen.

## 4. Navigation im Visualisierungsmodus 

Sie können mit den Tasten `Q` und `G` zwischen den Algorithmen Quickhull und Giftwrapping wechseln.

## 5. Anmerkung zur Darstellung 

Der Koordinatenursprung (0,0) ist zentriert in der Mitte des quadratischen Fensters. Die positive Richtung der y-Achse geht wegen Pygame nach unten. Wenn die Punkte zu klein dargestellt werden (z.B. als eine kleine Punktmenge), können Sie den Wert `coord_tresh` in der Hauptdatei an die maximalen x bzw. y Werte der Punkte anpassen.

## 6. Datengenerator 

Mit dem integrierten Datengenerator können Sie verschiedene Datenmuster, z.B. Kreisdaten, generieren.
