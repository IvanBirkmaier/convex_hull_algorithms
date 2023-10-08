# coding: utf-8
import random
import csv
import numpy as np

# generiert für eine Nummer X-viele random Punkte
def generate_random_points(number, coord_tresh, type = "uniform"):
    # type = ["uniform", "hline", "tiltline", "circle", "rectangle"]
    points_lst = []

    if type == "uniform":
        for i in range(number):
            rnd_coordinate = []
            for j in range(0, 2):
                #rnd_float = round(random.randint(-coord_tresh, coord_tresh), 2)
                rnd_float = random.randrange(-coord_tresh, coord_tresh)
                rnd_coordinate.append(rnd_float)
            points_lst.append(rnd_coordinate)
        return points_lst

    if type == "hline":
        for i in range(number):
            rnd_coordinate = []

            rnd_float = random.randrange(-coord_tresh, coord_tresh)
            rnd_coordinate.append(rnd_float)
            rnd_coordinate.append(0)
            points_lst.append(rnd_coordinate)
        return points_lst

    if type == "tiltline":
        slope = random.randrange(-5, 5)
        offset = random.randrange(-5, 5)
        for i in range(number):
            rnd_coordinate = []
            rnd_float = random.randrange(-coord_tresh, coord_tresh)
            rnd_coordinate.append(rnd_float)

            y_coord = slope*rnd_float + offset

            rnd_coordinate.append(y_coord)
            points_lst.append(rnd_coordinate)
        return points_lst

    if type == "circle":

        for i in range(number):
            rnd_coordinate = []

            rnd_float = random.randrange(-coord_tresh, coord_tresh)
            rnd_coordinate.append(rnd_float)

            sign = round(random.randint(0, 1)*2-1)
            y_coord = sign * np.sqrt(coord_tresh**2 - rnd_float**2 )

            rnd_coordinate.append(y_coord)
            points_lst.append(rnd_coordinate)
        return points_lst


    if type == "rectangle":
        width= int(coord_tresh*0.8)
        height= coord_tresh - width
        for i in range(number):
            rnd_coordinate = []

            rnd_float = random.randrange(-coord_tresh, coord_tresh)

            if abs(rnd_float) < width:
                rnd_coordinate.append(rnd_float)
                sign = round(random.randint(0, 1)*2-1)
                y_coord = sign * height
            else:
                rnd_coordinate.append(np.sign(rnd_float) * width)
                y_coord = random.randrange(-height, height)

            rnd_coordinate.append(y_coord)
            points_lst.append(rnd_coordinate)
        return points_lst

def detect_delimiter(path, possible_delimiters=[';', ',', '\t']):
    with open(path, 'r') as f:
        first_line = f.readline()
    delimiter_counts = [(delim, first_line.count(delim)) for delim in possible_delimiters]
    delimiter_counts.sort(key=lambda x: x[1], reverse=True)
    return delimiter_counts[0][0]

def load_data_csv(path):
    delimiter = detect_delimiter(path)
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        num_rows = int(next(reader)[0])
        data = [tuple(map(float, row)) for row in reader]
    return num_rows, data