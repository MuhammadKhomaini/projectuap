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
Label(konten_menu, text="Selamat Datang di", font=("Rockwell", 30, "bold"), bg="white").pack()
        Label(konten_menu, text="Project UAP Kelompok ", font=("Rockwell", 25, "bold"), bg="white").pack()
 
        Button(konten_menu, text="Perkenalan", font=("Poppins", 14), command=self.buka_perkenalan).pack(pady=20)
 
        self.frame_perkenalan = Frame(root, bg="white")
       
        konten_perkenalan = Frame(self.frame_perkenalan, bg="white")
        konten_perkenalan.pack(expand=True)
 
        Label(konten_perkenalan, text="Perkenalan Kelompok", font=("Rockwell", 25, "bold"), bg="white").pack(pady=20)
 
        self.foto_perkenalan = []
        isi_frame = Frame(konten_perkenalan, bg="white")
        isi_frame.pack()
if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    root.mainloop()
