from itertools import permutations
import math
import time
from Tkinter import Tk
from tkFileDialog import askopenfilename


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


def distance(p1, p2):  # Find distance between two coordinate pairs
    x1, y1 = p1  # P1 to x1,y1 coordinates
    x2, y2 = p2  # P2 to x2,y2 coordinates
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Using math library for distance formula


def total_distance(node_list):
    return sum([distance(point, node_list[index + 1]) for index, point in enumerate(node_list[:-1])])  # Generic total distance function of all permutations added


def valid_permutation(node_list):
    perm_list = []
    for i in permutations(node_list):  # All possible permutation values
        if i[0] == node_list[0]:    # If it starts with first node
            perm_list.append(i)  # Possible optimal permutation
    return perm_list  # Can be done through list comp, but for my readability, did not.


def minimum_value(perm_list):
    return min(perm_list, key=total_distance)  # Find minimum overall distance of given permutation list.


def main():
    Tk().withdraw()  # Do not want weight of full tkinter GUI class
    tsp_file = open(askopenfilename(), 'r')  # Open TSP file
    nodelist = parse_file(tsp_file)
    start = time.time()  # Start timing of program
    valid_perm = valid_permutation(nodelist)  # Retrieve permutations with same initial coordinate pair
    print("""Given these node coordinates: {} \nStarting At: {}\nThe total optimal distance is: {}
            \nOrder being: {} """.format(
        nodelist,
        nodelist[0],
        total_distance(minimum_value(valid_perm)),
        minimum_value(valid_perm),
    ))
    end = time.time()   # End of execution time

    print("Total Run Time: {}".format(end - start))


if __name__ == "__main__":
    main()
