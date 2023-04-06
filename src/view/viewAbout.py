import tkinter as tk
import tkinter.ttk as ttk

class About(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        style = ttk.Style()
        style.theme_use("vista")
        