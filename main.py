import numpy as np


class AntColony:
    """
    Parameters
    ----------
    distances : List
        Square matrix of distances.
    n_ants : int
        Number of ants in each iteration
    n_best : int
        Number of the best ants with pheromone
    n_iters : int
        Number of iterations
    pheromone_decay : float
        Decay rate of pheromone. If rate is lower, decay is faster.*
    alpha : float
        Exponent on pheromone. Higher alpha = greater pheromone weight. Default = 1.
    beta: float
        Exponent on distance. Higher beta = greater distance weight. Default = 1.
    """
    def __init__(self, distances: list, n_ants: int, n_best: int, n_iters: int, pheromone_decay: int,
                 alpha: int = 1, beta: int = 1):
        self.distances = distances
        self.pheromone = ...
        self.points = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iters
        self.decay = pheromone_decay
        self.alpha = alpha
        self.beta = beta

    # TODO: Main function to run code

    # TODO: Function (two or three) to generate path, every iteration with different (random) start city

    # TODO: Function with spreading pheromone to choose better distance

    # TODO: Function to choose best path

    # TODO: ...


if __name__ == '__main__':
    d = np.array([[0, 10, 12, 11, 14],
                  [10, 0, 13, 15, 8],
                  [12, 13, 0, 9, 14],
                  [11, 15, 9, 0, 16],
                  [14, 8, 14, 16, 0]])

    iteration = 100
    ants = 5
    cities = 5
