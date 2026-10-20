import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("520x620")
root.resizable(False, False)

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
)
judul.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=5)

mata_pelajaran = [
    "Nilai Matematika",
    "Nilai Bahasa Indonesia",
    "Nilai Bahasa Inggris",
    "Nilai Fisika",
    "Nilai Kimia",
    "Nilai Biologi",
    "Nilai Ekonomi",
    "Nilai Geografi",
    "Nilai Sejarah",
    "Nilai Informatika"
]

input_nilai = []

for i, mapel in enumerate(mata_pelajaran):
    label = tk.Label(
        frame,
        text=mapel,
        width=20,
        anchor="w",
        font=("Arial", 10)
    )
    label.grid(row=i, column=0, padx=10, pady=4)

    entry = ttk.Entry(frame, width=22)
    entry.grid(row=i, column=1, padx=10, pady=4)

    input_nilai.append(entry)

def hasil_prediksi():
    label_hasil.config(
        text="Prodi Pilihan: Teknologi Informasi"
    )

tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Arial", 11, "bold"),
    bg="green",
    fg="white",
    width=20,
    cursor="hand2"
)

tombol.pack(pady=18)

label_hasil = tk.Label(
    root,
    text="Hasil Prediksi: Belum tersedia",
    font=("Arial", 12, "bold"),
    fg="green"
)
label_hasil.pack(pady=5)

root.mainloop()
