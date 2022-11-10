from math import sqrt


def path(points: list):
    distance = []
    for p1 in points:
        dist_temp = []
        for p2 in points:
            dist_temp.append(round(sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2), 2))
        distance.append(dist_temp)
    return distance

