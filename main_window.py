import tkinter as tk
from tkinter import ttk

from config import WIDTH, HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT
from game_canvas import GameCanvas

from config_window import ConfigWindow


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Luki's Game of Life")

        self.mainframe = ttk.Frame(self, padding=5)
        self.mainframe.grid(row=0, column=0, sticky="NWSE")

        self.animation_speed = tk.IntVar()
        self.animation_speed.set(3)

        self.demo_mode_active = False
        self.demo_mode_task = None

        self.init_canvas(HEIGHT)
        self.init_buttons()

    def init_canvas(self, grid_size):
        pixelsize = CANVAS_HEIGHT // grid_size
        self.canvas = GameCanvas(self.mainframe, width=grid_size, height=grid_size, pixelsize=pixelsize, background="white", animation_speed=1000//self.animation_speed.get())
        self.canvas.grid(column=0, row=0, rowspan=7)

    def init_buttons(self):
        self.start_button = ttk.Button(self.mainframe, text="Start!")
        self.start_button.grid(column=1, row=0)
        self.start_button.bind("<Button-1>", self.start_animating)

        self.speed_label = ttk.Label(self.mainframe, text="Ticks per second")
        self.speed_label.grid(column=1, row=1, sticky="S")

        self.speed_slider = ttk.Scale(self.mainframe, from_=1, to=10, variable=self.animation_speed, command=self.update_speed)
        self.speed_slider.grid(column=1, row=2, sticky="N")
        self.update_speed()

        self.randomize_button = ttk.Button(self.mainframe, text="Randomize grid!")
        self.randomize_button.grid(column=1, row=3)
        self.randomize_button.bind("<Button-1>", self.randomize_grid)

        self.clear_button = ttk.Button(self.mainframe, text="Clear grid!")
        self.clear_button.grid(column=1, row=4)
        self.clear_button.bind("<Button-1>", self.clear_grid)

        self.demo_button = ttk.Button(self.mainframe, text="Demo Mode")
        self.demo_button.grid(column=1, row=5)
        self.demo_button.bind("<Button-1>", self.enable_demo_mode)

        self.config_button = ttk.Button(self.mainframe, text="Config")
        self.config_button.grid(column=1, row=6)
        self.config_button.bind("<Button-1>", self.open_config)

        

    def update_speed(self, event=None):
        self.speed_label["text"] = f"Ticks per second: {self.animation_speed.get()}"
        self.canvas.animation_speed = 1000 // self.animation_speed.get()


    def start_animating(self, event=None):
        if not self.canvas.animating:
            self.canvas.animating = True
            self.canvas.animate()
            self.start_button["text"] = "Stop!"
        else:
            self.canvas.stop_animating()
            self.start_button["text"] = "Start!"
        
    def open_config(self, event=None):
        self.config_window = ConfigWindow(master=self)
        self.config_window.wait_window()

    def randomize_grid(self, event=None):
        self.canvas.randomize()

    def clear_grid(self, event=None):
        self.canvas.clear()

    def enable_demo_mode(self, event=None):
        if not self.demo_mode_active:
            self.demo_mode_active = True
            self.canvas.stop_animating()
            self.demo_mode()
            self.demo_button["text"] = "Disable demo mode"

        else:
            self.demo_mode_active = False
            self.canvas.stop_animating()
            if self.demo_mode_task:
                self.after_cancel(self.demo_mode_task)
            self.demo_button["text"] = "Demo mode"

    def demo_mode(self):
        if self.demo_mode_active:
            self.canvas.stop_animating()
            self.clear_grid()
            self.randomize_grid()
            self.start_animating()
            self.demo_mode_task = self.after(60 * 1000, self.demo_mode)