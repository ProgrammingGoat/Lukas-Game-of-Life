import tkinter as tk
from tkinter import ttk

from game_logic import gamedata

class ConfigWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master=master)

        self.master=master

        self.grab_set()
        self.mainframe = ttk.Frame(self, padding=5)
        self.mainframe.grid(row=0, column=0, sticky="NWSE")

        
        self.grid_size = tk.IntVar()

        self.init_frame_size()
        self.init_buttons()
  
    def init_frame_size(self):
        self.size_input_label = ttk.Label(self.mainframe, text="Size of grid")
        self.size_input_label.grid(column=0, row=0)
        def validate_number(s):
            return s.isdecimal() or s == ""
        vcmd = (self.register(validate_number), "%P")
        self.size_input = ttk.Entry(self.mainframe, validate="all", validatecommand=vcmd, textvariable=self.grid_size)
        self.size_input.grid(column=1, row=0)

    def init_buttons(self):
        self.submit_button = ttk.Button(self.mainframe, text="Submit")
        self.submit_button.grid(column=1, row=1)
        self.submit_button.bind("<Button-1>", self.submit)

    def submit(self, event):
        grid_size = self.grid_size.get()
        gamedata.init_grid(grid_size, grid_size)
        self.master.init_canvas(grid_size)
        self.destroy()