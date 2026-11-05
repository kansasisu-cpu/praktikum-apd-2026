from prettytable import PrettyTable

from data import koleksi_dvd, data_transaksi
from utils import clear_terminal, enter, input_teks, input_angka, konfirmasi


def tampilkan_koleksi():
    if len(koleksi_dvd) == 0:
        print("Belum ada koleksi DVD.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Judul", "Genre", "Tahun", "Harga Sewa", "Stok"]

    for id_dvd, dvd in koleksi_dvd.items():
        tabel.add_row([
            id_dvd,
            dvd["judul"],
            dvd["genre"],
            dvd["tahun"],
            f"Rp{dvd['harga']}",
            dvd["stok"],
        ])

    tabel.align["Judul"] = "l"
    tabel.align["Genre"] = "l"
    tabel.align["Tahun"] = "l"

    print(tabel)

def cari_dvd():
    clear_terminal()
    print("============================== CARI DVD ==============================")
    try:
        mencari = input_teks("Masukkan judul film yang dicari: ").lower()
        hasil = {a: b for a, b in koleksi_dvd.items() if mencari in b["judul"].lower()}

        if len(hasil) == 0:
            raise KeyError(mencari)
        
    except ValueError as e:
        print(f"\n{e}")

    except KeyError:
        print("\nDVD tidak ditemukan!")

    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Judul", "Genre", "Tahun", "Harga Sewa", "Stok"]

        for id_dvd, dvd in hasil.items():
            tabel.add_row([
                id_dvd,
                dvd["judul"],
                dvd["genre"],
                dvd["tahun"],
                f"Rp{dvd['harga']}",
                dvd["stok"],
            ])

        tabel.align["Judul"] = "l"
        tabel.align["Genre"] = "l"
        tabel.align["Tahun"] = "l"

        print(tabel)

    finally:
        enter()

def tambah_dvd():
    clear_terminal()
    print("==========================================")
    print("               TAMBAH DVD")
    print("==========================================")

    try:
        id_dvd = input_teks("ID DVD: ").upper()

        if id_dvd in koleksi_dvd:
            raise ValueError("ID DVD sudah digunakan!")
        
        judul = input_teks("Judul film: ")
        genre = input_teks("Genre: ")
        tahun = input_angka("Tahun rilis: ", 1888)
        harga = input_angka("Harga sewa (angka): Rp", 0)
        stok = input_angka("Stok (angka): ", 0)

    except ValueError as e:
        print(f"\nGagal menambah DVD, {e}")

    else:
        koleksi_dvd[id_dvd] = {"judul": judul, "genre": genre, "tahun": tahun, "harga": harga, "stok": stok}
        print("\nDVD berhasil ditambahkan!")

    finally:
        enter("Tekan Enter untuk kembali ke menu admin...")

def ubah_dvd():
    clear_terminal()
    print("============================ UBAH DATA DVD ============================")
    tampilkan_koleksi()
    
    if len(koleksi_dvd) == 0:
        enter("Tekan Enter untuk kembali ke menu admin...")
        return

    try:
        id_dvd = input_teks("Masukkan ID DVD yang ingin diubah: ").upper()
        dvd = koleksi_dvd[id_dvd]
        
        print(f"\nJudul: {dvd['judul']} | Harga saat ini: Rp {dvd['harga']} | Stok saat ini: {dvd['stok']}")

        harga_baru = input_angka("\nHarga baru (Enter jika tidak ingin diubah): ", 0, True)
        stok_baru = input_angka("Stok baru (Enter jika tidak ingin diubah): ", 0, True)

    except KeyError:
        print("\nDVD tidak ditemukan!")

    except ValueError as e:
        print(f"\nGagal mengubah DVD, {e}")

    else:
        if harga_baru is not None:
            dvd["harga"] = harga_baru
        if stok_baru is not None:
            dvd["stok"] = stok_baru
        print("\nData DVD berhasil diperbarui!")

    finally:
        enter("Tekan Enter untuk kembali ke menu admin...")

def hapus_dvd():
    clear_terminal()

    print("============================== HAPUS DVD ==============================")
    tampilkan_koleksi()

    if len(koleksi_dvd) == 0:
        enter("Tekan Enter untuk kembali ke menu admin...")
        return

    try:
        id_dvd = input_teks("ID DVD yang ingin dihapus: ").upper()

        if id_dvd not in koleksi_dvd:
            raise KeyError(id_dvd)
        
        for t in data_transaksi.values():
            if t["id_dvd"] == id_dvd and t["status"] == "Dipinjam":
                raise ValueError("DVD tidak bisa dihapus karena masih dipinjam!")
            
    except KeyError:
        print("DVD tidak ditemukan!")

    except ValueError as e:
        print(f"{e}")

    else:
        if konfirmasi("Yakin hapus DVD ini?"):
            del koleksi_dvd[id_dvd]
            print("DVD berhasil dihapus!")

        else:
            print("Penghapusan dibatalkan.")

    finally:
        enter("Tekan Enter untuk kembali ke menu admin...")