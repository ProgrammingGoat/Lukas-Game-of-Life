import numpy as np

from config import WIDTH, HEIGHT

class GameData():
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid = np.zeros((self.height, self.width), dtype=bool)
        self.cache = dict()
        self.checked_coords = []
        # self.grid = np.random.choice(a=[False, True], size=(self.height, self.width))


    def sum_neighbors(self, i, j):
        top_bound = i-1 if i > 0 else 0
        bottom_bound = i+2 if i+1 < self.height else self.height
        left_bound = j-1 if j > 0 else 0
        right_bound = j+2 if j+1 < self.width else self.width

        # slice subarray around cell
        neighbors = self.grid[top_bound:bottom_bound, left_bound:right_bound]
        cell = self.grid[i, j]

        return np.sum(neighbors) - int(cell)


    def check_alive(self, i, j, new_grid, initial=False):
        if (i, j) in self.checked_coords:
            return
        self.checked_coords.append((i, j))
        alive = self.grid[i, j]
        number_of_neighbors = self.sum_neighbors(i, j)
        if alive and number_of_neighbors < 2:
            new_grid[i, j] = False
        if alive and number_of_neighbors in (2, 3):
            new_grid[i, j] = True
        if alive and number_of_neighbors > 3:
            new_grid[i, j] = False
        if not alive and number_of_neighbors == 3:
            new_grid[i, j] = True

        # recursive call
        if initial:
            top_bound = i-1 if i > 0 else 0
            bottom_bound = i+2 if i+1 < self.height else self.height
            left_bound = j-1 if j > 0 else 0
            right_bound = j+2 if j+1 < self.width else self.width

            for k in range(top_bound, bottom_bound):
                for l in range(left_bound, right_bound):
                    self.check_alive(k, l, new_grid)
        

    def calculate_gen(self):
        new_grid = np.copy(self.grid)
        for i in range(self.height):
            for j in range(self.width):
                if (self.grid[i, j]):
                    self.check_alive(i, j, new_grid, initial=True)
        self.grid = new_grid
        self.checked_coords = []
        

    

gamedata = GameData()