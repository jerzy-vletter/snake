import tkinter as tk

class createMainWindow(tk.Tk):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("SNAKE")
        self.attributes("-topmost", True)
        self.frame = tk.Frame(self)
        self.state = False
        self.minsize(900, 900)
        self.eval("tk::PlaceWindow . center")
        self.configure(background="black")

