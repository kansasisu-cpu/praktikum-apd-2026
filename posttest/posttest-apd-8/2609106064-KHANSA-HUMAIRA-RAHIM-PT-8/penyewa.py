from prettytable import PrettyTable

from data import data_penyewa, data_transaksi, counter
from utils import clear_terminal, enter, input_teks, konfirmasi


def tampilkan_penyewa():
    if len(data_penyewa) == 0:
        print("Belum ada penyewa.")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Telepon", "Alamat"]

    for id_penyewa, penyewa in data_penyewa.items():
        tabel.add_row([
            id_penyewa,
            penyewa["nama"],
            penyewa["telepon"],
            penyewa["alamat"]
        ])

    print(tabel)

def ubah_penyewa():
    clear_terminal()
    print("=============== UBAH DATA PENYEWA ===============")
    tampilkan_penyewa()

    if len(data_penyewa) == 0:
        enter("Tekan Enter untuk kembali ke menu admin...")
        return
    
    try:
        id_penyewa = input_teks("ID penyewa yang ingin diubah: ").upper()
        penyewa = data_penyewa[id_penyewa]
        nama_baru = input("\nNama baru (Enter jika tidak ingin diubah): ").strip()
        telepon_baru = input("Nomor telepon baru (Enter jika tidak ingin diubah): ").strip()
        alamat_baru = input("Alamat baru (Enter jika tidak ingin diubah): ").strip()

    except KeyError:
        print("\nData penyewa tidak ditemukan!")

    except ValueError as e:
        print(f"\n{e}")

    else:
        if nama_baru != "":
            penyewa["nama"] = nama_baru

        if telepon_baru != "":
            penyewa["telepon"] = telepon_baru

        if alamat_baru != "":
            penyewa["alamat"] = alamat_baru

        print("\nData penyewa berhasil diperbarui!")

    finally:
        enter("Tekan Enter untuk kembali ke menu admin...")

def hapus_penyewa():
    clear_terminal()
    print("=============== HAPUS DATA PENYEWA ===============")
    tampilkan_penyewa()

    if len(data_penyewa) == 0:
        enter("Tekan Enter untuk kembali ke menu admin...")
        return
    
    try:
        id_penyewa = input_teks("ID penyewa yang ingin dihapus: ").upper()
        if id_penyewa not in data_penyewa:
            raise KeyError(id_penyewa)
        for t in data_transaksi.values():
            if t["id_penyewa"] == id_penyewa and t["status"] == "Dipinjam":
                raise ValueError("Penyewa masih memiliki transaksi aktif dan tidak bisa dihapus!")
            
    except KeyError:
        print("Data penyewa tidak ditemukan!")

    except ValueError as e:
        print(f"{e}")

    else:
        if konfirmasi("Yakin hapus data penyewa?"):
            del data_penyewa[id_penyewa]
            print("Data penyewa berhasil dihapus!")

        else:
            print("Penghapusan dibatalkan.")

    finally:
        enter("Tekan Enter untuk kembali ke menu admin...")

def buat_id_penyewa():
    nomor = counter["penyewa"]
    id_baru = "Z" + str(nomor)

    if nomor < 10:
        id_baru = "Z00" + str(nomor)

    elif nomor < 100:
        id_baru = "Z0" + str(nomor)

    counter["penyewa"] += 1
    return id_baru