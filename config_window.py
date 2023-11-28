import tkinter as tk
from tkinter import ttk

class ConfigWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        self.grab_set()

        self.mainframe = ttk.Frame(self, padding=5)
        self.mainframe.grid(row=0, column=0, sticky="NWSE")

        self.init_frame_size()
  
    def init_frame_size(self):
        def validate_number(string):
            return string.isdigit()
        self.canvas_size = tk.IntVar()
        self.size_input = ttk.Entry(self.mainframe, validatecommand=validate_number, textvariable=self.canvas_size)
        self.size_input.grid(column=0, row=0)