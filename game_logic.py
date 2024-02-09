import numpy as np

from config import WIDTH, HEIGHT

class GameData():
    def __init__(self, width: int, height: int):
        self.init_grid(width, height)
        self.cache = dict()
        self.checked_coords = []

    def init_grid(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((self.height, self.width), dtype=bool)
                

    def randomize_grid(self):
        self.grid = np.random.choice([True, False], (self.height, self.width))

    def clear_grid(self):
        self.init_grid(self.width, self.height)

    def get_neighbors(self, i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
            if j > 0:
                neighbors.append((i-1, j-1))
            if j+1 < self.width:
                neighbors.append((i-1, j+1))
        if i+1 < self.height:
            neighbors.append((i+1, j))
            if j > 0:
                neighbors.append((i+1, j-1))
            if j+1 < self.width:
                neighbors.append((i+1, j+1))
        if j > 0:
            neighbors.append((i, j-1))
        if j+1 < self.width:
            neighbors.append((i, j+1))
        return neighbors

    def sum_neighbors(self, i, j):
        neighbors = self.get_neighbors(i, j)
        sum = 0

        for x, y in neighbors:
            sum += self.grid[x, y]

        return sum


    def check_alive(self, i, j, new_grid, rec=0):
        if (i, j) in self.checked_coords:
            return
        alive = self.grid[i, j]
        number_of_neighbors = self.sum_neighbors(i, j)
        # if alive and number_of_neighbors < 2:
        #     new_grid[i, j] = False
        if alive and number_of_neighbors in (2, 3):
            new_grid[i, j] = True
        # if alive and number_of_neighbors > 3:
        #     new_grid[i, j] = False
        if not alive and number_of_neighbors == 3:
            new_grid[i, j] = True

        # recursive call
        if alive and rec < 2:
            self.checked_coords.append((i, j))
            neighbors = self.get_neighbors(i, j)
            for k, l in neighbors:
                self.check_alive(k, l, new_grid, rec+1)
        

    def calculate_gen(self):
        new_grid = np.zeros(self.grid.shape, dtype=bool)
        for i in range(self.height):
            for j in range(self.width):
                if (self.grid[i, j]):
                    self.check_alive(i, j, new_grid)
        self.grid = new_grid
        self.checked_coords = []
        

    

gamedata = GameData(WIDTH, HEIGHT)