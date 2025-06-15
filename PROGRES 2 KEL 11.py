import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime

BIRU_score = 0
MERAH_score = 0

def update(label, val):
    global BIRU_score, MERAH_score
    if label == "BIRU":
        BIRU_score += val
        BIRU_label.config(text=str(BIRU_score))
    else:
        MERAH_score += val
        MERAH_label.config(text=str(MERAH_score))

def reset():
    global BIRU_score, MERAH_score
    BIRU_score = 0
    MERAH_score = 0
    BIRU_label.config(text="0")
    MERAH_label.config(text="0")

def tampilkan_info():
    BIRU_name = BIRU_name_entry.get()
    MERAH_name = MERAH_name_entry.get()
    juri = juri_entry.get()

    BIRU_name_display.config(text=f"BIRU: {BIRU_name if BIRU_name else '-'}")
    MERAH_name_display.config(text=f"MERAH: {MERAH_name if MERAH_name else '-'}")
    juri_display.config(text=f"JUMLAH JURI: {juri if juri else '-'}")
def simpan_riwayat():
    BIRU_name = BIRU_name_entry.get()
    MERAH_name = MERAH_name_entry.get()
    juri = juri_entry.get()
    now = datetime.now()
    tanggal = now.strftime("%Y-%m-%d")
    waktu = now.strftime("%H:%M:%S")

    data = [tanggal, waktu, BIRU_name, MERAH_name, juri, BIRU_score, MERAH_score]
    header = ["Tanggal", "Waktu", "BIRU", "MERAH", "JURI", "SKOR_BIRU", "SKOR_MERAH"]

    write_header = not os.path.exists("riwayat_pertandingan.csv")

    with open("riwayat_pertandingan.csv", mode="a", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if write_header:
def load_data():
    global BIRU_score, MERAH_score
    if os.path.exists("riwayat_pertandingan.csv"):
        with open("riwayat_pertandingan.csv", mode="r") as file:
            reader = csv.DictReader(file, delimiter=';')
            rows = list(reader)
            if rows:
                last = rows[-1]
                try:
                    BIRU_name_entry.insert(0, last["BIRU"])
                    MERAH_name_entry.insert(0, last["MERAH"])
                    juri_entry.insert(0, last["JURI"])
                    BIRU_score = int(last["SKOR_BIRU"])
                    MERAH_score = int(last["SKOR_MERAH"])
                    BIRU_label.config(text=str(BIRU_score))
                    MERAH_label.config(text=str(MERAH_score))
                    tampilkan_info()
                except KeyError:
                    messagebox.showerror("Error", "Struktur CSV tidak sesuai.\nSilakan hapus atau perbaiki file CSV.")

root = tk.Tk()
root.title("Scoring Pertandingan")
root.geometry("600x500")
root.resizable(False, False)

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="BIRU:").grid(row=0, column=0) 

BIRU_name_entry = tk.Entry(top_frame)
BIRU_name_entry.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="MERAH:").grid(row=0, column=2)
MERAH_name_entry = tk.Entry(top_frame)
MERAH_name_entry.grid(row=0, column=3, padx=5) 
tk.Label(top_frame, text="JUMLAH JURI:").grid(row=1, column=0, pady=5)
juri_entry = tk.Entry(top_frame)
juri_entry.grid(row=1, column=1, pady=5)

tk.Button(top_frame, text="Tampilkan Info", command=tampilkan_info).grid(row=1, column=3, padx=5)

info_frame = tk.Frame(root)
info_frame.pack(pady=5)
BIRU_name_display = tk.Label(info_frame, text="BIRU: -")
MERAH_name_display = tk.Label(info_frame, text="MERAH: -")
juri_display = tk.Label(info_frame, text="JUMLAH JURI: -")
BIRU_name_display.pack()
MERAH_name_display.pack()
juri_display.pack()

score_frame = tk.Frame(root)
score_frame.pack(expand=True, fill="both", padx=20, pady=10)

BIRU = tk.Frame(score_frame, bg="blue")
BIRU.pack(side="left", expand=True, fill="both", padx=10)
tk.Label(BIRU, text="BIRU", bg="blue", fg="white", font=("Arial", 20)).pack(pady=5)
BIRU_label = tk.Label(BIRU, text="0", bg="blue", fg="white", font=("Arial", 40))
BIRU_label.pack(pady=5)
tk.Button(BIRU, text="+1", command=lambda: update("BIRU", 1)).pack(pady=2)
tk.Button(BIRU, text="-1", command=lambda: update("BIRU", -1)).pack(pady=2)

MERAH = tk.Frame(score_frame, bg="red")
MERAH.pack(side="right", expand=True, fill="both", padx=10)
tk.Label(MERAH, text="MERAH", bg="red", fg="white", font=("Arial", 20)).pack(pady=5)
MERAH_label = tk.Label(MERAH, text="0", bg="red", fg="white", font=("Arial", 40))
MERAH_label.pack(pady=5)
tk.Button(MERAH, text="+1", command=lambda: update("MERAH", 1)).pack(pady=2)
tk.Button(MERAH, text="-1", command=lambda: update("MERAH", -1)).pack(pady=2)

tk.Button(root, text="Reset Skor", command=reset).pack(pady=5)
tk.Button(root, text="Simpan Riwayat", command=simpan_riwayat).pack(pady=5)
tk.Button(root, text="Hapus Semua Riwayat", bg="red", fg="white", command=hapus_riwayat).pack(pady=5)

load_data()
root.mainloop()
