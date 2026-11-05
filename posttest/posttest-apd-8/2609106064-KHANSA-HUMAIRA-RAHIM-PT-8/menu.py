import inquirer

from tema import tema_admin, tema_user
from utils import clear_terminal, enter
from dvd import tampilkan_koleksi, cari_dvd, tambah_dvd, ubah_dvd, hapus_dvd
from penyewa import tampilkan_penyewa, ubah_penyewa, hapus_penyewa
from transaksi import tampilkan_transaksi, pengembalian_dvd, tambah_durasi, sewa_dvd


def menu_admin():
    clear_terminal()
    print("Anda login sebagai admin!")
    enter("Tekan Enter untuk melanjutkan ke menu admin...")

    while True:
        clear_terminal()
        print("=====================================")
        print("              MENU ADMIN")
        print("=====================================")
        pertanyaan = [inquirer.List("pilihan", 
                                    message="Pilih menu", 
                                    choices=[" Lihat koleksi DVD", " Cari DVD", " Tambah DVD", " Ubah data DVD", " Hapus DVD", " Lihat data penyewa", " Ubah data penyewa", " Hapus data penyewa", " Lihat semua transaksi", " Pengembalian DVD", " Tambah durasi peminjaman DVD", " Logout"])
                     ]

        jawaban = inquirer.prompt(pertanyaan, theme=tema_admin())

        if jawaban["pilihan"] == " Lihat koleksi DVD":
            clear_terminal()
            print("============================= KOLEKSI DVD =============================")
            tampilkan_koleksi()
            enter("Tekan Enter untuk kembali ke menu admin...")

        elif jawaban["pilihan"] == " Cari DVD":
            cari_dvd()

        elif jawaban["pilihan"]  == " Tambah DVD":
            tambah_dvd()

        elif jawaban["pilihan"] == " Ubah data DVD":
            ubah_dvd()

        elif jawaban["pilihan"] == " Hapus DVD":
            hapus_dvd()

        elif jawaban["pilihan"] == " Lihat data penyewa":
            clear_terminal()
            print("=============== DATA PENYEWA ===============")
            tampilkan_penyewa()
            enter("Tekan Enter untuk kembali ke menu admin...")

        elif jawaban["pilihan"] == " Ubah data penyewa":
            ubah_penyewa()

        elif jawaban["pilihan"] == " Hapus data penyewa":
            hapus_penyewa()

        elif jawaban["pilihan"] == " Lihat semua transaksi":
            clear_terminal()
            print("=============== SEMUA TRANSAKSI ===============")
            tampilkan_transaksi()
            enter("Tekan Enter untuk kembali ke menu admin...")
            
        elif jawaban["pilihan"] == " Pengembalian DVD":
            pengembalian_dvd()

        elif jawaban["pilihan"] == " Tambah durasi peminjaman DVD":
            tambah_durasi()

        elif jawaban["pilihan"] == " Logout":
            clear_terminal()
            print("Logout berhasil.")
            enter("Tekan Enter untuk melanjutkan...")
            break

        else:
            print("Opsi tidak valid! Masukkan pilihan 1 sampai 12.")
            enter("Tekan Enter untuk mencoba lagi...")

def menu_pengguna(username):
    while True:
        clear_terminal()
        print("=============================")
        print("        MENU PENGGUNA")
        print("=============================")
        pertanyaan = [inquirer.List("pilihan", 
                                    message="Pilih menu", 
                                    choices=[" Lihat koleksi DVD", " Cari DVD", " Sewa DVD", " Lihat transaksi saya", " Logout"])
                    ]

        jawaban = inquirer.prompt(pertanyaan, theme=tema_user())

        if jawaban["pilihan"] == " Lihat koleksi DVD":
            clear_terminal()
            print("============================= KOLEKSI DVD =============================")
            tampilkan_koleksi()
            enter()

        elif jawaban["pilihan"] == " Cari DVD":
            cari_dvd()

        elif jawaban["pilihan"] == " Sewa DVD":
            sewa_dvd(username)

        elif jawaban["pilihan"] == " Lihat transaksi saya":
            clear_terminal()
            print("=============== TRANSAKSI SAYA ===============")
            tampilkan_transaksi(username)
            enter()

        elif jawaban["pilihan"] == " Logout":
            clear_terminal()
            print("Logout berhasil.")
            enter("Tekan Enter untuk melanjutkan...")
            break

        else:
            print("\nOpsi tidak valid! Masukkan pilihan 1 sampai 5.")
            enter("Tekan Enter untuk mencoba lagi...")