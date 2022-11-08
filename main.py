import numpy as np


class AntColony:
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

    # TODO: Function with spreading pheromone

    # TODO: Function to choose path

    # TODO: Function to save best path

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

    print(np.ones(d.shape) / len(d))
