import tkinter as tk

class Button(tk.Tk):

    def __init__(self, text=""):
        super().__init__()
        self.button = tk.ttk.Label(self, text=text)
