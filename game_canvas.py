import numpy as np
from tkinter import Canvas
from game_logic import gamedata

class GameCanvas(Canvas):
    def __init__(self, parent, width, height, pixelsize, background, animation_speed):
        Canvas.__init__(self, parent, width=width*pixelsize, height=height*pixelsize, background=background)
        self.width = width
        self.height = height
        self.pixelsize = pixelsize
        self.animation_speed = animation_speed
        self.gamedata = gamedata
        self.animating = False
        self.animation_task = None

        self.alivecolor = "orangered"
        self.deadcolor = "lightgray"

        self.squares = np.zeros((self.height, self.width), dtype=int)
        self.init_canvas()

        self.bind("<Button-1>", self.clicked)

    def init_canvas(self):
        for i in range(self.height):
            for j in range(self.width):
               self.draw_rectangle(j, i, self.deadcolor, 1) 

    def clicked(self, event):
        x = int(self.canvasx(event.x) // self.pixelsize)
        y = int(self.canvasy(event.y) // self.pixelsize)
        self.gamedata.grid[y, x] = not self.gamedata.grid[y, x]
        if self.gamedata.grid[y, x]:
            self.set_rectangle_alive(x, y)
        else:
            self.set_rectangle_dead(x, y)
        
    def draw_rectangle(self, x, y, color="red", outline=0):
        startx = x * self.pixelsize + 1
        starty = y * self.pixelsize + 1
        endx = startx + self.pixelsize + 1 
        endy = starty + self.pixelsize + 1
        self.squares[x, y] = self.create_rectangle(startx, starty, endx, endy, fill=color, width=outline, outline="gray")

    # def delete_rectangle(self, x, y):
    #     self.delete(self.squares[x, y])
    #     self.squares[x, y] = 0

    def set_rectangle_alive(self, x, y):
        # self.find_withtag(self.squares[x, y])["fill"] = self.alivecolor
        self.itemconfig(self.squares[x, y], fill=self.alivecolor)

    def set_rectangle_dead(self, x, y):
        # self.find_withtag(self.squares[x, y])["fill"] = self.deadcolor
        self.itemconfig(self.squares[x, y], fill=self.deadcolor)

    def load_grid(self):
        grid = self.gamedata.grid
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                if grid[y, x]:
                    self.set_rectangle_alive(x, y)
                elif not grid[y, x]:
                    self.set_rectangle_dead(x, y)

    def randomize(self):
        self.gamedata.randomize_grid()
        self.load_grid()

    def animate(self):
        if self.animating:
            gamedata.calculate_gen()
            self.load_grid()
            self.animation_task = self.after(self.animation_speed, self.animate)

    def stop_animating(self):
        self.animating = False
        if self.animation_task:
            print(self.animation_task)
            self.after_cancel(self.animation_task)

    def clear(self):
        self.gamedata.clear_grid()
        self.load_grid()
