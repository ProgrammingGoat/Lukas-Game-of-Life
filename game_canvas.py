from tkinter import Canvas
from game_logic import gamedata

class GameCanvas(Canvas):
    def __init__(self, parent, width, height, pixelsize, background):
        Canvas.__init__(self, parent, width=width*pixelsize, height=height*pixelsize, background=background)
        self.width = width
        self.height = height
        self.pixelsize = pixelsize
        self.gamedata = gamedata
        self.animation_speed = 100
        self.animating = False

        # self.init_grid()

        self.bind("<Button-1>", self.clicked)

    # def init_grid(self):
    #     for y in range(self.height):
    #         for x in range(self.width):
    #             self.draw_rectangle(x, y, None)

    def clicked(self, event):
        x = int(self.canvasx(event.x) // self.pixelsize)
        y = int(self.canvasy(event.y) // self.pixelsize)
        self.gamedata.grid[y, x] = not self.gamedata.grid[y, x]
        self.load_grid()
        
    def draw_rectangle(self, x, y, color="red"):
        startx = x * self.pixelsize + 1
        starty = y * self.pixelsize + 1
        endx = startx + self.pixelsize + 1 
        endy = starty + self.pixelsize + 1
        self.create_rectangle(startx, starty, endx, endy, fill=color, width=0)

    def load_grid(self):
        grid = self.gamedata.grid
        self.delete("all")
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                if grid[y, x]:
                    self.draw_rectangle(x, y)

    def animate(self):
        if self.animating:
            gamedata.calculate_gen()
            self.load_grid()
            self.after(self.animation_speed, self.animate)