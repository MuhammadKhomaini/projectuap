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

nama_anggota = [
            ("Umay", "fotoumay.png"),
            ("Zahra", "fotozahra.png"),
            ("Feliza", "fotofeliza.png"),
            ("Daffa", "fotodaffa.png"),
        ]
 
        for nama, file in nama_anggota:
            f = Frame(isi_frame, bg="white")
            f.pack(side="left", padx=10)
            try:
                img = Image.open(file).resize((100, 130))
                img_tk = ImageTk.PhotoImage(img)
                self.foto_perkenalan.append(img_tk)
                Label(f, image=img_tk, bg="white").pack()
            except:
                Label(f, text="(No Image)", bg="white").pack()
            Label(f, text=nama, font=("Arial", 10, "bold"), bg="white").pack()
 
        Button(konten_perkenalan, text="Kembali ke Menu", command=self.kembali_menu).pack(pady=10)
        Button(konten_perkenalan, text="Lanjut ke Project", command=self.buka_project).pack()
if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    root.mainloop()
