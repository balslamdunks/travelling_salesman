import numpy as np
from Tkinter import Tk, Canvas
import math
from tkFileDialog import askopenfilename
import time
__WINDOW__ = 500

root = Tk()
canvas = Canvas(root, width=__WINDOW__ + 50, height=__WINDOW__ + 100, bg='white')
canvas.create_text(100, 10, fill="purple", font="Times 20 bold",
                   text="TSP: 30 ")

canvas.pack()


def greedy_algorithm(nodes):
    __SAVECOST__ = float('inf')  # finding most efficient in pythong
    optimal_path = []

    for i, start in enumerate(nodes):
        growing_list = [i] # Start out with initial city value, ca   n be manually altered, or chooses variable cities
        length = 0

        next, neighbor, dist = closest_edge(start, nodes, growing_list) # Find closest edge attributes
        length += dist # Increase overall length by distance travelled
        growing_list.append(next) # Move to next coordinate

        while len(growing_list) < nodes.shape[0]: # Append to list as long as overall lingth of lest is less than the total nodes possible
            next, neighbor, dist = closest_edge(neighbor, nodes, growing_list)
            length += dist
            growing_list.append(next)

        # print(order)

        if length < __SAVECOST__:
            __SAVECOST__= length
            optimal_path = growing_list # Find optimal path based on 'inf'

    return optimal_path, __SAVECOST__

def distance_for_length(p1, p2):
    x = p2[0] - p1[0]   # Distance formula to get from edge to edge
    y = p2[1] - p1[1]

    return (x ** 2 + (y** 2))


def closest_edge(node, total_cities, visited):
    __SAVECOST__ = float('inf')  # finding most efficient in python
    next_neighbor = float
    current_closest = float

    for i, c in enumerate(total_cities):

        if i in visited:
            pass
        if i not in visited:
            distance = distance_for_length(node, c) # Append to visited values

            if distance < __SAVECOST__:
                current_closest = c
                next_neighbor = i
                __SAVECOST__ = distance


    return next_neighbor, current_closest, __SAVECOST__





def distance(p1, p2):  # Find distance between two coordinate pairs
    x1, y1 = p1  # P1 to x1,y1 coordinates
    x2, y2 = p2  # P2 to x2,y2 coordinates
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Using math library for distance formula

def points_for_path(search_list, coordinate_list):
        coordinate_vals = [] # Generate values that associate with given path found
        final_vals = []
        for l in search_list:
            for m in coordinate_list:
                if l in m:
                    coordinate_vals.append(m)
        for h in coordinate_vals:
            final_vals.append((h[1], h[2]))

        return final_vals


def strip_list(given_list):
    for h in given_list:
        given_list.strip([h[0]])




def total_distance(node_list):
    return sum([distance(point, node_list[index + 1]) for index, point in enumerate(node_list[:-1])])  # Generic total distance function of all permutations added


def drawPath(path, cities, length):
    cities = cities[path]
    addToCanvas(cities)
    canvas.update()
    root.mainloop()


def parse_file(file_tsp):
    node_list = []  # List for Empty Node Coordinates
    int_dimension = 0
    for i, line in enumerate(file_tsp):  # Read through file lines
        if i == 4: # Fourth line in file is Dimension
            dimension_val = line.strip().split()[1]  # Grab corresponding dimension value
            int_dimension = int(dimension_val) + 7  # Change dimension value from str -> int
        if i in range(7, int_dimension):  # Read each coordinate value, starting at line 7 until final coordinate
            x, y = line.strip().split()[1:]  # Assign as coordinate pair values
            node_list.append([float(x), float(y)])  # Append coordinate values to node list
    return node_list


def addToCanvas(cities):
    min_x = np.min(cities[:, 0])
    min_y = np.min(cities[:, 1])

    max_x = np.max(cities[:, 0])
    max_y = np.max(cities[:, 1])

    for i in range(len(cities)):
        c = cities[i - 1]
        c_next = cities[i]

        scaled_x = (c[0] - min_x) / (max_x - min_x) * __WINDOW__ + 60
        scaled_y = (c[1] - min_y) / (max_y - min_y) * __WINDOW__ + 60

        scaled_x_next = (c_next[0] - min_x) / (max_x - min_x) * __WINDOW__ + 60
        scaled_y_next = (c_next[1] - min_y) / (max_y - min_y) * __WINDOW__ + 60

        canvas.create_oval(scaled_x/1.3 - 4, scaled_y/1.3 - 4, scaled_x/1.3 + 4, scaled_y/1.3 + 4, fill='pink', outline='black')
        canvas.create_oval(scaled_x_next/1.3 - 4, scaled_y_next/1.3 - 4, scaled_x_next/1.3 + 4, scaled_y_next/1.3 + 4, fill='pink',
                           outline='black')

        canvas.create_line(scaled_x/1.3, scaled_y/1.3, scaled_x_next/1.3, scaled_y_next/1.3, fill='black')



if __name__ == "__main__":
    Tk().withdraw()  # Do not want weight of full tkinter GUI class
    f = open(askopenfilename(), 'r').read().splitlines()[7:]
    nodes = np.array([tuple(map(float, coord.split())) for coord in f])
    start = time.time()
    path, length = greedy_algorithm(nodes)

    order = points_for_path(path, nodes)
    overall_distance = total_distance(order)

    end = time.time()
    print ("Total time of: {}, Overall Path Length: {} \n and pathway being: {} ".format(end - start, overall_distance, path))

    drawPath(path, nodes, length)
