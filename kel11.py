from tkinter import Tk, Frame, Button
from PIL import Image, ImageTk

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Project UAP")
        self.root.geometry("500x500")
        self.root.resizable(True, True)

        self.frame_menu = Frame(root, bg="white")
        self.frame_menu.pack(fill="both", expand=True)
        
        konten_menu = Frame(self.frame_menu, bg="white")
        konten_menu.pack(expand=True)

if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    root.mainloop()
