from prettytable import PrettyTable

from data import koleksi_dvd, data_penyewa, data_transaksi, counter
from utils import clear_terminal, enter, input_teks, input_angka, total_harga
from dvd import tampilkan_koleksi
from penyewa import buat_id_penyewa


def tampilkan_transaksi(username=None):
    tabel = PrettyTable()
    tabel.field_names = ["No", "ID Penyewa", "ID DVD", "Durasi Sewa", "Status", "Jumlah"]
    ada = False

    for no_transaksi, transaksi in data_transaksi.items():
        if username is None or transaksi["username"] == username:
            tabel.add_row([
                no_transaksi,
                transaksi["id_penyewa"],
                transaksi["id_dvd"],
                f"{transaksi['durasi']} hari",
                transaksi["status"],
                transaksi["jumlah"]
            ])
            ada = True

    if ada:
        print(tabel)
    else:
        print("Belum ada transaksi.")

def pengembalian_dvd():
    clear_terminal()
    print("=============== PENGEMBALIAN DVD ===============")
    tampilkan_transaksi()

    if len(data_transaksi) == 0:
        enter("Tekan Enter untuk kembali ke menu admin...")
        return
    
    try:
        no_transaksi = input_teks("Nomor transaksi: ").upper()
        transaksi = data_transaksi[no_transaksi]

        if transaksi["status"] == "Dikembalikan":
            raise ValueError("DVD pada transaksi ini sudah dikembalikan.")
        
    except KeyError:
        print("\nNomor transaksi tidak ditemukan!")

    except ValueError as e:
        print(f"\n{e}")

    else:
        transaksi["status"] = "Dikembalikan"

        if transaksi["id_dvd"] in koleksi_dvd:
            koleksi_dvd[transaksi["id_dvd"]]["stok"] += transaksi["jumlah"]
        print("\nPengembalian berhasil diproses. Stok DVD telah ditambah.")

    finally:
        enter("Tekan Enter untuk kembali ke menu admin...")

def tambah_durasi():
    clear_terminal()
    print("======== MENAMBAH DURASI PEMINJAMAN DVD ========")
    tampilkan_transaksi()

    if len(data_transaksi) == 0:
        enter("Tekan Enter untuk kembali ke menu admin...")
        return
    
    try:
        no_transaksi = input_teks("Nomor transaksi: ").upper()
        transaksi = data_transaksi[no_transaksi]

        if transaksi["status"] == "Dikembalikan":
            raise ValueError("Durasi tidak bisa ditambah karena DVD sudah dikembalikan!")
        
        tambahan = input_angka("Tambahan durasi peminjaman (hari): ", 1)

    except KeyError:
        print("\nNomor transaksi tidak ditemukan!")

    except ValueError as e:
        print(f"\n{e}")

    else:
        durasi_lama = transaksi["durasi"]
        transaksi["durasi"] = durasi_lama + tambahan
        print("\nDurasi peminjaman berhasil ditambah!")
        print("Durasi sebelumnya: ", durasi_lama, "hari")
        print("Tambahan durasi: ", tambahan, "hari")
        print("Total durasi: ", transaksi["durasi"], "hari")

    finally:
        enter("Tekan Enter untuk kembali ke menu admin...")

def buat_id_transaksi():
    nomor = counter["transaksi"]
    id_baru = "Y" + str(nomor)

    if nomor < 10:
        id_baru = "Y00" + str(nomor)

    elif nomor < 100:
        id_baru = "Y0" + str(nomor)

    counter["transaksi"] += 1
    return id_baru

def sewa_dvd(username):
    clear_terminal()
    print("============================== SEWA DVD ==============================")
    tampilkan_koleksi()

    try:
        id_dvd = input_teks("ID DVD yang ingin disewa: ").upper()
        dvd = koleksi_dvd[id_dvd]

        print(f"\nJudul: {dvd['judul']}")
        print("Harga sewa per DVD per hari: Rp", dvd["harga"])
        print("Stok tersedia:", dvd["stok"])

        jumlah = input_angka("\nJumlah DVD yang ingin disewa: ", 1)

        if jumlah > dvd["stok"]:
            raise ValueError("Stok DVD tidak cukup!")
        
        durasi = input_angka("Durasi sewa (hari): ", 1)
        nama = input_teks("Nama lengkap: ")
        telepon = input_teks("Nomor telepon: ")
        alamat = input_teks("Alamat: ")

    except KeyError:
        print("\nDVD tidak ditemukan!")

    except ValueError as e:
        print(f"\nPenyewaan gagal, {e}")

    else:
        id_penyewa = buat_id_penyewa()
        id_transaksi = buat_id_transaksi()

        data_penyewa[id_penyewa] = {"nama": nama, "telepon": telepon, "alamat": alamat, "username": username}
        data_transaksi[id_transaksi] = {
            "id_penyewa": id_penyewa,
            "id_dvd": id_dvd,
            "harga": dvd["harga"],
            "durasi": durasi,
            "status": "Dipinjam",
            "jumlah": jumlah,
            "username": username
        }

        dvd["stok"] -= jumlah

        print("\nPenyewaan berhasil!")
        print("Nomor transaksi:", id_transaksi)
        print("Durasi sewa:", durasi, "hari")
        print("Total harga sewa: Rp", total_harga(dvd["harga"], jumlah, durasi))

    finally:
        enter()