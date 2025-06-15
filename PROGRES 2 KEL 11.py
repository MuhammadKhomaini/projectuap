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
