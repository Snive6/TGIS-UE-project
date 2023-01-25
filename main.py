from path import draw_path
from ant_colony import ant_search
from read_data import read_data

data = read_data("p01.csv")
print(data)
best_route, best_cost = ant_search(data)
print('Chosen path:', best_route)
print('Cost of the chosen path: ', best_cost)

route = [int(x)-1 for x in best_route.tolist()]
print(route)

draw_path(data, route)
