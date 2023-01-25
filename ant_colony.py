import numpy as np
from path import distance_calk


def ant_search(data, iterations=400, n_ants=50):
    # Create distance matrix from data
    distance_list = (distance_calk(data))
    distance_matrix = np.array(distance_list)

    # Initialization
    n_cities = len(data)
    e = .2  # evaporation rate
    alpha = 1  # pheromone factor
    beta = 2  # visibility factor

    # calculating the visibility of the next city visibility(i,j)=1/d(i,j)
    visibility = np.array([[1 / dist if dist != 0 else 0 for dist in distance_point]
                           for distance_point in distance_matrix])

    # initializing pheromone present at the paths to the cities
    pheromone = np.ones((n_cities, n_cities))

    # initializing the route of the ants with size rute(n_ants,n_cities+1)
    # note adding 1 because we want to come back to the source city

    route = np.ones((n_ants, n_cities + 1))
    best_route = 0
    dist_min_cost = 0

    for iteration in range(iterations):

        route[:, 0] = 1  # initial starting and ending positon of every ants '1' i.e city '1'

        for i in range(n_ants):

            temp_visibility = np.array(visibility)  # creating a copy of visibility

            for j in range(n_cities - 1):
                cur_loc = int(route[i, j] - 1)  # current city of the ant

                temp_visibility[:, cur_loc] = 0  # making visibility of the current city as zero

                p_feature = np.power(pheromone[cur_loc, :], beta)  # calculating pheromone feature
                v_feature = np.power(temp_visibility[cur_loc, :], alpha)  # calculating visibility feature

                p_feature = p_feature[:, np.newaxis]  # adding axis
                v_feature = v_feature[:, np.newaxis]  # adding axis

                combine_feature = np.multiply(p_feature, v_feature)  # calculating the combine feature
                total = np.sum(combine_feature)  # sum of all the feature

                probs = combine_feature / total  # finding probability of element probs(i) = combine_feature(i)/total

                cum_prob = np.cumsum(probs)  # calculating cumulative sum
                r = np.random.random_sample()  # random no in [0,1)
                # finding the next city having probability higher than random(r)
                city = np.nonzero(cum_prob > r)[0][0] + 1

                route[i, j + 1] = city  # adding city to route

            left = list(set([i for i in range(1, n_cities + 1)]) - set(route[i, :-2]))[
                0]  # finding the last untraversed city to route

            route[i, -2] = left  # adding untraversed city to route

        rute_opt = np.array(route)  # initializing optimal route

        dist_cost = np.zeros((n_ants, 1))  # initializing total_distance_of_tour with zero

        for i in range(n_ants):

            s = 0
            for j in range(n_cities - 1):
                s = s + distance_matrix[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1]
                # calcualating total tour distance

            dist_cost[i] = s  # storing distance of tour for 'i'th ant at location 'i'

        dist_min_loc = np.argmin(dist_cost)  # finding location of minimum of dist_cost
        dist_min_cost = dist_cost[dist_min_loc]  # finding min of dist_cost

        best_route = route[dist_min_loc, :]  # initializing current traversed as best route
        pheromone = (1 - e) * pheromone  # evaporation of pheromone with (1-e)

        for i in range(n_ants):
            for j in range(n_cities - 1):
                dt = 1 / dist_cost[i]
                pheromone[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1] = \
                    pheromone[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1] + dt
                # updating the pheromone with delta_distance
                # delta_distance will be more with min_dist i.e adding more weight to that route  pheromone

    best_cost = int(dist_min_cost[0]) + distance_matrix[int(best_route[-2]) - 1, 0]

    return best_route, best_cost
