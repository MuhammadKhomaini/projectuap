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