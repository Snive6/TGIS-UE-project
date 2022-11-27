from math import sqrt
import plotly.express as px


def distance_calk(points: list):
    distance = []
    for p1 in points:
        dist_temp = []
        for p2 in points:
            dist_temp.append(round(sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2), 2))
        distance.append(dist_temp)
    return distance


def mapa(points: list):
    x1, x2 = map(list, zip(*points))
    figure = px.scatter(x=x1, y=x2)
    return figure


def route_add(figure, points: list, route: list):
    newlist = [points[i] for i in route]
    newlist.append(newlist[0])
    x1, x2 = map(list, zip(*newlist))

    trace = next(figure.select_traces())
    n = len(trace.x)
    color = [trace.marker.color] * n
    color[route[0]] = "blue"
    size = [8] * n
    size[route[0]] = 15
    symbol = [trace.marker.symbol] * n
    symbol[route[0]] = "star"
    fig.update_traces(marker=dict(color=color, size=size, symbol=symbol))

    figure.add_scatter(x=x1, y=x2, name='droga')


p = [(1.0, 2.0), (3.0, 2.0), (2.0, 4.0), (5.0, 1.0)]
r = [1, 3, 0, 2]
fig = mapa(p)
route_add(fig, p, r)
fig.show()
