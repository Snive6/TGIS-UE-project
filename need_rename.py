from path import *

def initialize(path):
    start = path[0]

# TODO: CALCULATE DISTANCE BETWEEN POINTS


def calc_distance(distances, route):
    path_distance = []
    for i in range(len(distances)-1):
        path_distance.append(distances[route[i]][route[i+1]])
    return path_distance


if __name__ == '__main__':
    p = [(1.0, 3.0), (4.0, 1.0), (5.0, 9.0), (10.0, 6.0)]
    r = [1, 3, 0, 2]
    for i in range(4):
        print(distance_calk(p)[i])

    distances = distance_calk(p)
    print(calc_distance(distances, r))




