from tkinter import Tk, Frame, Button
from PIL import Image, ImageTk

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Project UAP")
        self.root.geometry("500x500")
        self.root.resizable(True, True)

if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    root.mainloop()
