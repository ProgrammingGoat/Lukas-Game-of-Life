import tkinter as tk
from tkinter import ttk

from config import WIDTH, HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT
from game_canvas import GameCanvas

from game_logic import gamedata
from config_window import ConfigWindow


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Luki's Game of Life")

        self.mainframe = ttk.Frame(self, padding=5)
        self.mainframe.grid(row=0, column=0, sticky="NWSE")

        self.init_canvas()
        self.init_buttons()

    def init_canvas(self):
        pixelsize = CANVAS_HEIGHT // HEIGHT
        self.canvas = GameCanvas(self.mainframe, width=WIDTH, height=HEIGHT, pixelsize=pixelsize, background="white")
        self.canvas.grid(column=0, row=0, rowspan=3)

    def init_buttons(self):
        self.start_button = ttk.Button(self.mainframe, text="Start!")
        self.start_button.grid(column=1, row=0)
        self.start_button.bind("<Button-1>", self.start_animating)

        self.animation_speed = tk.IntVar()
        self.animation_speed.set(10)

        self.speed_label = ttk.Label(self.mainframe, text="Ticks per second")
        self.speed_label.grid(column=1, row=1, sticky="S")

        self.speed_slider = ttk.Scale(self.mainframe, from_=1, to=100, variable=self.animation_speed, command=self.update_speed)
        self.speed_slider.grid(column=1, row=2, sticky="N")
        self.update_speed()

        self.config_button = ttk.Button(self.mainframe, text="Config")
        self.config_button.grid(column=1, row=3)
        self.config_button.bind("<Button-1>", self.open_config)

    def update_speed(self, event=None):
        self.speed_label["text"] = f"Ticks per second: {self.animation_speed.get()}"
        self.canvas.animation_speed = 1000 // self.animation_speed.get()


    def start_animating(self, event):
        if not self.canvas.animating:
            self.canvas.animating = True
            self.canvas.animate()
            self.start_button["text"] = "Stop!"
        else:
            self.canvas.animating = False
            self.start_button["text"] = "Start!"
        
    def open_config(self, event):
        self.config_window = ConfigWindow()
        self.config_window.wait_window()