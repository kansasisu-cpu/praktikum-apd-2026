import os

koleksi_dvd = {
    "X001" : {"judul" : "I Origins", "genre" : "Sci-Fi", "tahun" : 2014, "harga" : 3000, "stok" : 2},
    "X002" : {"judul" : "The Notebook", "genre" : "Romance", "tahun" : 2004, "harga" : 5000, "stok" : 5},
    "X003" : {"judul" : "Vivarium", "genre" : "Horror", "tahun" : 2019, "harga" : 3000, "stok" : 3},
    "X004" : {"judul" : "The Housemaid", "genre" : "Thriller", "tahun" : 2025, "harga" : 8000, "stok" : 6},
    "X005" : {"judul" : "The Shadow Strays", "genre" : "Action", "tahun" : 2024, "harga" : 4000, "stok" : 3},
    "X006" : {"judul" : "(500) Days of Summer", "genre" : "Rom-Com", "tahun" : 2009, "harga" : 8000, "stok" : 7},
    "X007" : {"judul" : "HxH, The Last Mission", "genre" : "Anime", "tahun" : 2013, "harga" : 4000, "stok" : 10},
    "X008" : {"judul" : "DC, The Scarlet Bullet", "genre" : "Anime", "tahun" : 2021, "harga" : 3000, "stok" : 5},
    "X009" : {"judul" : "The Conjuring", "genre" : "Horror", "tahun" : 2013, "harga" : 8000, "stok" : 11},
    "X010" : {"judul" : "Hereditary", "genre" : "Horror", "tahun" : 2018, "harga" : 8000, "stok" : 7}
}

data_akun = {
    "kansa" : {"password" : "64", "peran" : "admin"}
}

data_penyewa = {}

data_transaksi = {}

nomor_penyewa = 1
nomor_transaksi = 1
 
while True:
    os.system("cls")
    print("======================================")
    print("        RENTAL DVD 'KANSASISU'")
    print("======================================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    print("======================================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        os.system("cls")
        print("========= REGISTER =========")
        username_baru = input("Buat Username: ").strip().lower()
        password_baru = input("Buat Password: ").strip().lower()
        print("============================")

        if username_baru in data_akun:
            print("\nUsername sudah terpakai!")

        elif username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong!")

        else:
            data_akun[username_baru] = {"password": password_baru, "peran": "pengguna"}
            print("\nRegister berhasil! Silakan login.")

        input("Tekan Enter untuk kembali...")

    elif pilihan == "2":
        os.system("cls")
        print("========== LOGIN ==========")
        username = input("Username: ").strip().lower()
        password = input("Password: ").strip().lower()

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        if username not in data_akun:
            print("\nAkun tidak terdaftar! Silahkan register.")
            input("Tekan Enter untuk kembali ke menu utama...")
            continue

        if data_akun[username]["password"] != password:
            print("\nPassword salah! Silahkan login ulang.")
            input("Tekan Enter untuk kembali ke menu utama...")
            continue

        peran_login = data_akun[username]["peran"]

        if peran_login == "admin":
            os.system("cls")
            print("Anda login sebagai admin!")
            input("\nTekan Enter untuk melanjutkan ke menu admin...")

            while True:
                os.system("cls")
                print("=================================")
                print("            MENU ADMIN")
                print("=================================")
                print("1. Lihat koleksi DVD")
                print("2. Cari DVD berdasarkan judul")
                print("3. Tambah DVD")
                print("4. Ubah data DVD")
                print("5. Hapus DVD")
                print("6. Lihat data penyewa")
                print("7. Ubah data penyewa")
                print("8. Hapus data penyewa")
                print("9. Lihat semua transaksi")
                print("10. Pengembalian DVD")
                print("11. Tambah Durasi Peminjaman DVD")
                print("12. Logout")
                print("=================================")
                menu_admin = input("Pilih menu: ").strip()

                if menu_admin == "1":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                           KOLEKSI DVD")
                    print("======================================================================================================")

                    if len(koleksi_dvd) == 0:
                        print("Belum ada koleksi DVD.")

                    else:
                        for id_dvd, dvd in koleksi_dvd.items():
                            print("ID:", id_dvd, "| Judul:", dvd["judul"], "| Genre:", dvd["genre"], "| Tahun:", dvd["tahun"], "| Harga sewa: Rp", dvd["harga"], "| Stok:", dvd["stok"])
                            print("======================================================================================================")

                    input("\nTekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "2":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                             CARI DVD")
                    print("======================================================================================================")

                    mencari = input("Masukkan judul film yang dicari: ").strip().lower()
                    print("======================================================================================================")
                    ditemukan = False

                    for id_dvd, dvd in koleksi_dvd.items():
                        if mencari in dvd["judul"].lower():
                            print("ID:", id_dvd, "| Judul:", dvd["judul"], "| Genre:", dvd["genre"], "| Tahun:", dvd["tahun"], "| Harga: Rp", dvd["harga"], "| Stok:", dvd["stok"])
                            print("======================================================================================================")
                            ditemukan = True

                    if not ditemukan:
                        print("\nDVD tidak ditemukan!")

                    input("Tekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "3":
                    os.system("cls")
                    print("==========================================")
                    print("               TAMBAH DVD")
                    print("==========================================")

                    id_dvd = input("ID DVD: ").strip().upper()

                    if id_dvd == "" or id_dvd in koleksi_dvd:
                        print("\nID DVD kosong atau sudah digunakan!")

                    else:
                        judul = input("Judul film: ").strip()
                        genre = input("Genre: ").strip()
                        tahun_input = input("Tahun rilis: ").strip()
                        harga_input = input("Harga sewa (angka): Rp").strip()
                        stok_input = input("Stok (angka): ").strip()

                        if judul == "" or genre == "":
                            print("\nJudul dan genre tidak boleh kosong!")

                        elif not tahun_input.isdigit() or not harga_input.isdigit() or not stok_input.isdigit():
                            print("\nTahun, harga, dan stok harus berupa angka!")

                        elif int(tahun_input) < 1888 or int(harga_input) < 0 or int(stok_input) < 0:
                            print("\nTahun atau harga atau stok yang anda masukkan tidak valid!")

                        else:
                            koleksi_dvd[id_dvd] = {
                                "judul": judul,
                                "genre": genre,
                                "tahun": int(tahun_input),
                                "harga": int(harga_input),
                                "stok": int(stok_input)
                            }
                            print("\nDVD berhasil ditambahkan!")

                    input("Tekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "4":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                         UBAH DATA DVD")
                    print("======================================================================================================")

                    for id_dvd, dvd in koleksi_dvd.items():
                        print("ID:", id_dvd, "| Judul:", dvd["judul"], "| Genre:", dvd["genre"], "| Tahun:", dvd["tahun"], "| Harga sewa: Rp", dvd["harga"], "| Stok:", dvd["stok"])
                        print("======================================================================================================")

                    id_dvd = input("Masukkan ID DVD yang ingin diubah: ").strip().upper()

                    if id_dvd in koleksi_dvd:
                        dvd = koleksi_dvd[id_dvd]

                        print("\nJudul:", dvd["judul"], "| Harga saat ini: Rp", dvd["harga"], "| Stok saat ini:", dvd["stok"])

                        harga_baru = input("\nHarga baru (Enter jika tidak ingin diubah): ").strip()
                        stok_baru = input("Stok baru (Enter jika tidak ingin diubah): ").strip()

                        if harga_baru != "" and not harga_baru.isdigit():
                            print("\nHarga harus berupa angka!")

                        elif stok_baru != "" and not stok_baru.isdigit():
                            print("\nStok harus berupa angka!")

                        elif harga_baru != "" and int(harga_baru) < 0:
                            print("\nHarga tidak boleh negatif!")

                        elif stok_baru != "" and int(stok_baru) < 0:
                            print("\nStok tidak boleh negatif!")

                        else:
                            if harga_baru != "":
                                dvd["harga"] = int(harga_baru)
                            if stok_baru != "":
                                dvd["stok"] = int(stok_baru)
                            print("\nData DVD berhasil diperbarui!")

                    else:
                        print("\nDVD tidak ditemukan!")

                    input("Tekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "5":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                           HAPUS DVD")
                    print("======================================================================================================")

                    for id_dvd, dvd in koleksi_dvd.items():
                        print("ID:", id_dvd, "| Judul:", dvd["judul"], "| Genre:", dvd["genre"], "| Tahun:", dvd["tahun"], "| Harga sewa: Rp", dvd["harga"], "| Stok:", dvd["stok"])
                        print("======================================================================================================")

                    id_dvd = input("ID DVD yang ingin dihapus: ").strip().upper()
                    dvd_dipinjam = False

                    for transaksi in data_transaksi.values():
                        if transaksi["id_dvd"] == id_dvd and transaksi["status"] == "Dipinjam":
                            dvd_dipinjam = True

                    if id_dvd not in koleksi_dvd:
                        print("\nDVD tidak ditemukan!")

                    elif dvd_dipinjam:
                        print("\nDVD tidak bisa dihapus karena masih dipinjam!")

                    else:
                        while True:
                            konfirmasi = input("\nYakin hapus DVD ini? (ya/tidak): ").strip().lower()
                            if konfirmasi == "ya":
                                del koleksi_dvd[id_dvd]
                                print("\nDVD berhasil dihapus!")
                                break

                            elif konfirmasi == "tidak":
                                print("\nPenghapusan dibatalkan.")
                                break

                            else:
                                print("\nPilihan tidak valid! Masukkan 'ya' atau 'tidak'.")
                                continue

                    input("Tekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "6":
                    os.system("cls")
                    print("==========================================================")
                    print("                      DATA PENYEWA")
                    print("==========================================================")

                    if len(data_penyewa) == 0:
                        print("Belum ada penyewa.")
                    else:
                        for id_penyewa, penyewa in data_penyewa.items():
                            print("ID:", id_penyewa, "| Nama:", penyewa["nama"], "| Telepon:", penyewa["telepon"], "| Alamat:", penyewa["alamat"])
                            print("==========================================================")

                    input("\nTekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "7":
                    os.system("cls")
                    print("==========================================================")
                    print("                    UBAH DATA PENYEWA")
                    print("==========================================================")

                    if len(data_penyewa) == 0:
                        print("Belum ada penyewa.")

                    else:
                        for id_penyewa, penyewa in data_penyewa.items():
                            print("ID:", id_penyewa, "| Nama:", penyewa["nama"], "| Telepon:", penyewa["telepon"], "| Alamat:", penyewa["alamat"])
                            print("==========================================================")

                        id_penyewa = input("ID penyewa yang ingin diubah: ").strip().upper()

                        if id_penyewa in data_penyewa:
                            penyewa = data_penyewa[id_penyewa]

                            nama_baru = input("\nNama baru (Enter jika tidak ingin diubah): ").strip()
                            telepon_baru = input("Nomor telepon baru (Enter jika tidak ingin diubah): ").strip()
                            alamat_baru = input("Alamat baru (Enter jika tidak ingin diubah): ").strip()

                            if nama_baru != "":
                                penyewa["nama"] = nama_baru

                            if telepon_baru != "":
                                penyewa["telepon"] = telepon_baru

                            if alamat_baru != "":
                                penyewa["alamat"] = alamat_baru

                            print("\nData penyewa berhasil diperbarui!")

                        else:
                            print("\nData penyewa tidak ditemukan!")

                    input("\nTekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "8":
                    os.system("cls")
                    print("==========================================================")
                    print("                    HAPUS DATA PENYEWA")
                    print("==========================================================")

                    if len(data_penyewa) == 0:
                        print("Belum ada penyewa.")

                    else:
                        for id_penyewa, penyewa in data_penyewa.items():
                            print("ID:", id_penyewa, "| Nama:", penyewa["nama"], "| Telepon:", penyewa["telepon"], "| Alamat:", penyewa["alamat"])
                            print("==========================================================")

                        id_penyewa = input("ID penyewa yang ingin dihapus: ").strip().upper()
                        masih_meminjam = False

                        for transaksi in data_transaksi.values():
                            if transaksi["id_penyewa"] == id_penyewa and transaksi["status"] == "Dipinjam":
                                masih_meminjam = True

                        if id_penyewa not in data_penyewa:
                            print("\nData penyewa tidak ditemukan!")

                        elif masih_meminjam:
                            print("\nPenyewa masih memiliki transaksi aktif dan tidak bisa dihapus!")

                        else:
                            while True:
                                konfirmasi = input("\nYakin hapus data penyewa? (ya/tidak): ").strip().lower()
                                if konfirmasi == "ya":
                                    del data_penyewa[id_penyewa]
                                    print("\nData penyewa berhasil dihapus!")
                                    break

                                elif konfirmasi == "tidak":
                                    print("\nPenghapusan dibatalkan.")
                                    break

                                else:
                                    print("\nPilihan tidak valid! Masukkan 'ya' atau 'tidak'.")
                                    continue

                    input("\nTekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "9":
                    os.system("cls")
                    print("==========================================================")
                    print("                     SEMUA TRANSAKSI")
                    print("==========================================================")

                    if len(data_transaksi) == 0:
                        print("Belum ada transaksi.")

                    else:
                        for no_transaksi, transaksi in data_transaksi.items():
                            print("No:", no_transaksi, "| ID Penyewa:", transaksi["id_penyewa"], "| ID DVD:", transaksi["id_dvd"], "| Durasi sewa:", transaksi["durasi"], "hari", "| Status:", transaksi["status"], "| Jumlah:", transaksi["jumlah"])
                            print("==========================================================")

                    input("\nTekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "10":
                    os.system("cls")
                    print("==========================================================")
                    print("                     PENGEMBALIAN DVD")
                    print("==========================================================")

                    if len(data_transaksi) == 0:
                        print("Belum ada transaksi.")

                    else:
                        for no_transaksi, transaksi in data_transaksi.items():
                            print("No:", no_transaksi, "| ID Penyewa:", transaksi["id_penyewa"], "| ID DVD:", transaksi["id_dvd"], "| Durasi sewa:", transaksi["durasi"], "hari", "| Status:", transaksi["status"], "| Jumlah:", transaksi["jumlah"])
                            print("==========================================================")

                        no_transaksi = input("Nomor transaksi: ").strip().upper()

                        if no_transaksi in data_transaksi:
                            transaksi = data_transaksi[no_transaksi]

                            if transaksi["status"] == "Dikembalikan":
                                print("\nDVD pada transaksi ini sudah dikembalikan.")

                            else:
                                transaksi["status"] = "Dikembalikan"

                                if transaksi["id_dvd"] in koleksi_dvd:
                                    koleksi_dvd[transaksi["id_dvd"]]["stok"] += transaksi["jumlah"]

                                print("\nPengembalian berhasil diproses. Stok DVD telah ditambah.")

                        else:
                            print("\nNomor transaksi tidak ditemukan!")

                    input("\nTekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "11":
                    os.system("cls")
                    print("==========================================================")
                    print("              MENAMBAH DURASI PEMINJAMAN DVD")
                    print("==========================================================")

                    if len(data_transaksi) == 0:
                        print("Belum ada transaksi.")

                    else:
                        for no_transaksi, transaksi in data_transaksi.items():
                            print("No:", no_transaksi, "| ID Penyewa:", transaksi["id_penyewa"], "| ID DVD:", transaksi["id_dvd"], "| Durasi sewa:", transaksi["durasi"], "hari", "| Status:", transaksi["status"], "| Jumlah:", transaksi["jumlah"])
                            print("==========================================================")

                        no_transaksi = input("Nomor transaksi: ").strip().upper()

                        if no_transaksi in data_transaksi:
                            transaksi = data_transaksi[no_transaksi]

                            if transaksi["status"] == "Dikembalikan":
                                print("\nDurasi tidak bisa ditambah karena DVD sudah dikembalikan!")

                            else:
                                tambahan_input = input("Tambahan durasi peminjaman (hari): ").strip()

                                if not tambahan_input.isdigit():
                                    print("Tambahan durasi harus berupa angka positif!")

                                elif int(tambahan_input) <= 0:
                                    print("Tambahan durasi harus lebih dari 0!")

                                else:
                                    durasi_lama = transaksi["durasi"]
                                    tambahan_durasi = int(tambahan_input)
                                    durasi_total = durasi_lama + tambahan_durasi
                                    transaksi["durasi"] = durasi_total

                                    print("\nDurasi peminjaman berhasil ditambah!")
                                    print("Durasi sebelumnya:", durasi_lama, "hari")
                                    print("Tambahan durasi:", tambahan_durasi, "hari")
                                    print("Total durasi sekarang:", durasi_total, "hari")

                        else:
                            print("Nomor transaksi tidak ditemukan!")

                    input("\nTekan Enter untuk kembali...")

                elif menu_admin == "12":
                    os.system("cls")
                    print("Logout berhasil.")
                    input("\nTekan Enter untuk melanjutkan...")
                    break

                else:
                    print("Opsi tidak valid!")
                    input("\nTekan Enter untuk mencoba lagi...")

        else:
            while True:
                os.system("cls")
                print("=============================")
                print("        MENU PENGGUNA")
                print("=============================")
                print("1. Lihat koleksi DVD")
                print("2. Cari DVD")
                print("3. Sewa DVD")
                print("4. Lihat transaksi saya")
                print("5. Logout")
                menu_pengguna = input("Pilih menu: ").strip()

                if menu_pengguna == "1":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                           KOLEKSI DVD")
                    print("======================================================================================================")

                    if len(koleksi_dvd) == 0:
                        print("Belum ada koleksi DVD.")

                    else:
                        for id_dvd, dvd in koleksi_dvd.items():
                            print("ID:", id_dvd, "| Judul:", dvd["judul"], "| Genre:", dvd["genre"], "| Tahun:", dvd["tahun"], "| Harga sewa: Rp", dvd["harga"], "| Stok:", dvd["stok"])
                            print("======================================================================================================")

                    input("\nTekan Enter untuk kembali...")

                elif menu_pengguna == "2":
                    os.system("cls")
                    print("==========================================")
                    print("                CARI DVD")
                    print("==========================================")

                    mencari = input("Masukkan judul film yang dicari: ").strip().lower()
                    ditemukan = False

                    for id_dvd, dvd in koleksi_dvd.items():
                        if mencari in dvd["judul"].lower():
                            print("\nID:", id_dvd, "| Judul:", dvd["judul"], "| Genre:", dvd["genre"], "| Tahun:", dvd["tahun"], "| Harga: Rp", dvd["harga"], "| Stok:", dvd["stok"])
                            ditemukan = True

                    if not ditemukan:
                        print("DVD tidak ditemukan!")

                    input("\nTekan Enter untuk kembali...")

                elif menu_pengguna == "3":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                            SEWA DVD")
                    print("======================================================================================================")

                    for id_dvd, dvd in koleksi_dvd.items():
                        print("ID:", id_dvd, "| Judul:", dvd["judul"], "| Genre:", dvd["genre"], "| Tahun:", dvd["tahun"], "| Harga sewa: Rp", dvd["harga"], "| Stok:", dvd["stok"])
                        print("======================================================================================================")

                    id_dvd = input("ID DVD yang ingin disewa: ").strip().upper()

                    if id_dvd in koleksi_dvd:
                        dvd = koleksi_dvd[id_dvd]

                        print("\nJudul:", dvd["judul"])
                        print("Harga sewa per DVD per hari: Rp", dvd["harga"])
                        print("Stok tersedia:", dvd["stok"])

                        jumlah_input = input("\nJumlah DVD yang ingin disewa: ").strip()

                        if not jumlah_input.isdigit() or int(jumlah_input) <= 0:
                            print("Jumlah sewa harus berupa angka positif!")

                        elif int(jumlah_input) > dvd["stok"]:
                            print("Stok DVD tidak cukup!")

                        else:
                            durasi_input = input("Durasi sewa (hari): ").strip()

                            if not durasi_input.isdigit() or int(durasi_input) <= 0:
                                print("Durasi harus berupa angka positif!")

                            else:
                                durasi_sewa = int(durasi_input)
                                nama_penyewa = input("Nama lengkap: ").strip()
                                telepon = input("Nomor telepon: ").strip()
                                alamat = input("Alamat: ").strip()

                                if nama_penyewa == "" or telepon == "" or alamat == "":
                                    print("Data penyewa tidak boleh kosong!")

                                else:
                                    id_penyewa = "Z" + str(nomor_penyewa)

                                    if nomor_penyewa < 10:
                                        id_penyewa = "Z00" + str(nomor_penyewa)

                                    elif nomor_penyewa < 100:
                                        id_penyewa = "Z0" + str(nomor_penyewa)

                                    id_transaksi = "Y" + str(nomor_transaksi)

                                    if nomor_transaksi < 10:
                                        id_transaksi = "Y00" + str(nomor_transaksi)

                                    elif nomor_transaksi < 100:
                                        id_transaksi = "Y0" + str(nomor_transaksi)

                                    data_penyewa[id_penyewa] = {
                                        "nama": nama_penyewa,
                                        "telepon": telepon,
                                        "alamat": alamat,
                                        "username": username
                                    }

                                    data_transaksi[id_transaksi] = {
                                        "id_penyewa": id_penyewa,
                                        "id_dvd": id_dvd,
                                        "durasi": durasi_sewa,
                                        "status": "Dipinjam",
                                        "jumlah": int(jumlah_input),
                                        "username": username
                                    }

                                    dvd["stok"] -= int(jumlah_input)

                                    total_harga = dvd["harga"] * int(jumlah_input) * durasi_sewa

                                    nomor_penyewa += 1
                                    nomor_transaksi += 1

                                    print("\nPenyewaan berhasil!")
                                    print("Nomor transaksi:", id_transaksi)
                                    print("Durasi sewa:", durasi_sewa, "hari")
                                    print("Total harga sewa: Rp", total_harga)

                    else:
                        print("DVD tidak ditemukan!")

                    input("\nTekan Enter untuk kembali...")

                elif menu_pengguna == "4":
                    os.system("cls")
                    print("==========================================================")
                    print("                     TRANSAKSI SAYA")
                    print("==========================================================")
                    transaksi_pengguna = False

                    for no_transaksi, transaksi in data_transaksi.items():
                        if transaksi["username"] == username:
                            print("No:", no_transaksi, "| ID Penyewa:", transaksi["id_penyewa"], "| ID DVD:", transaksi["id_dvd"], "| Durasi sewa:", transaksi["durasi"], "hari", "| Status:", transaksi["status"], "| Jumlah:", transaksi["jumlah"])
                            transaksi_pengguna = True
                            print("==========================================================")

                    if not transaksi_pengguna:
                        print("Kamu belum memiliki transaksi.")

                    input("\nTekan Enter untuk kembali...")

                elif menu_pengguna == "5":
                    os.system("cls")
                    print("Logout berhasil.")
                    input("\nTekan Enter untuk melanjutkan...")
                    break

                else:
                    print("\nOpsi tidak valid! Masukkan pilihan 1 sampai 5.")
                    input("Tekan Enter untuk mencoba lagi...")

    elif pilihan == "3":
        os.system("cls")
        print("Terima kasih telah mengakses program kami!")
        break

    else:
        print("Opsi tidak valid! Masukkan pilihan 1 sampai 3.")
        input("\nTekan Enter untuk mencoba lagi...")