# ConvexHull

This is a simple example for the implementation and visualization of the Giftwrapping and Quickhull algorithms. Everything is coded in Python.

## Setup

### Python Environment
It is recommended to use a Python environment with Conda.

### Installation of Pygame
After setting up your Conda environment, you can install Pygame with the following command:
```sh
pip install pygame
```

## Instructions

### 1. Starting the Program
Run the main file `main.py` to start the program.

### 2. Mode Selection
- **Performance Mode**: Both algorithms, Quickhull and Giftwrapping, are measured for their performance. The result is output to the console.
- **Visualization Mode**: The functioning of the algorithms is visualized. A new window opens where you can see the algorithms in action.

### 3. Selecting the Data Source
You can either use randomly generated points or read a CSV file with data points.

### 4. Navigation in Visualization Mode
You can switch between the Quickhull and Giftwrapping algorithms using the `Q` and `G` keys.

### 5. Note on Display
The coordinate origin (0,0) is centered in the middle of the square window. The positive direction of the y-axis goes downwards due to Pygame. If the points are displayed too small (e.g., as a small set of points), you can adjust the value `coord_tresh` in the main file to match the maximum x and y values of the points.

### 6. Data Generator
With the integrated data generator, you can generate various data patterns, e.g., circle data.

There is a test protocol that presents the results of the implementation.

