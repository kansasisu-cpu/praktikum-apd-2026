import os
import inquirer

from tema import tema_awal


def clear_terminal():
    os.system("cls")

def enter(pesan="Tekan Enter untuk kembali..."):
    input("\n" + pesan)

def input_teks(pesan):
    teks = input(pesan).strip() 

    if teks == "":
        raise ValueError("Input tidak boleh kosong!")
    
    return teks

def input_angka(pesan, min = 0, boleh_kosong = False):
    teks = input(pesan).strip()

    if teks == "":
        if boleh_kosong:
            return None
        raise ValueError("Input tidak boleh kosong!")
    
    if not teks.isdigit():
        raise ValueError("Input harus berupa angka bulat positif!")
    
    nilai = int(teks)

    if nilai < min:
        raise ValueError(f"Nilai minimal yang diperbolehkan adalah {min}!")
    
    return nilai

def total_harga(harga, jumlah, durasi):
    return harga * jumlah * durasi

def konfirmasi(pesan):
    pertanyaan = [inquirer.List("pilihan", 
                                message=pesan, 
                                choices=[" Hapus", " Batal"])
                ]

    jawaban = inquirer.prompt(pertanyaan, theme=tema_awal())

    if jawaban["pilihan"] == " Hapus":
        return True
    
    if jawaban["pilihan"] == " Batal":
        return False
    
    return konfirmasi(pesan)