import os

koleksi_dvd = [
    ["X001", "I Origins", "Sci-Fi", 2014, 3000, 2],
    ["X002", "The Notebook", "Romance", 2004, 5000, 5],
    ["X003", "Vivarium", "Horror", 2019, 3000, 3],
    ["X004", "The Housemaid", "Thriller", 2025, 8000, 6],
    ["X005", "The Shadow Strays", "Action", 2024, 4000, 3],
    ["X006", "(500) Days of Summer", "Rom-Com", 2009, 8000, 7],
    ["X007", "HxH, The Last Mission", "Action", 2013, 4000, 10],
    ["X008", "DC, The Scarlet Bullet", "Action", 2021, 3000, 5],
    ["X009", "The Conjuring", "Horror", 2013, 8000, 11],
    ["X010", "Hereditary", "Horror", 2018, 8000, 7]
]

data_akun = [
    ["kansa", "64", "admin"]
]
data_penyewa = []
data_transaksi = []

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

        username_terpakai = False

        for akun in data_akun:
            if akun[0] == username_baru:
                username_terpakai = True
                break

        if username_terpakai:
            print("\nUsername sudah terpakai!")

        elif username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong!")

        else:
            data_akun.append([username_baru, password_baru, "pengguna"])
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

        akun_ditemukan = False
        peran = ""

        for akun in data_akun:
            if akun[0] == username and akun[1] == password:
                akun_ditemukan = True
                peran_login = akun[2]
                break

        if not akun_ditemukan:
            akun_terdaftar = False

            for akun in data_akun:
                if akun[0] == username:
                    akun_terdaftar = True
                    break

            if not akun_terdaftar:
                print("\nAkun tidak terdaftar! Silahkan register.")
                input("Tekan Enter untuk kembali ke menu utama...")
                continue

            else:
                print("\nPassword salah! Silahkan login ulang.")
                input("Tekan Enter untuk kembali ke menu utama...")
                continue

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
                        for dvd in koleksi_dvd:
                            print("ID:", dvd[0], "| Judul:", dvd[1], "| Genre:", dvd[2], "| Tahun:", dvd[3], "| Harga sewa: Rp", dvd[4], "| Stok:", dvd[5])
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

                    for dvd in koleksi_dvd:
                        if mencari in dvd[1].lower():
                            print("ID:", dvd[0], "| Judul:", dvd[1], "| Genre:", dvd[2], "| Tahun:", dvd[3], "| Harga: Rp", dvd[4], "| Stok:", dvd[5])
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
                    id_ada = False

                    for dvd in koleksi_dvd:
                        if dvd[0] == id_dvd:
                            id_ada = True
                            break

                    if id_dvd == "" or id_ada:
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
                            koleksi_dvd.append([id_dvd, judul, genre, int(tahun_input), int(harga_input), int(stok_input)])
                            print("\nDVD berhasil ditambahkan!")

                    input("Tekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "4":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                         UBAH DATA DVD")
                    print("======================================================================================================")

                    for dvd in koleksi_dvd:
                        print("ID:", dvd[0], "| Judul:", dvd[1], "| Genre:", dvd[2], "| Tahun:", dvd[3], "| Harga sewa: Rp", dvd[4], "| Stok:", dvd[5])
                        print("======================================================================================================")

                    id_dvd = input("Masukkan ID DVD yang ingin diubah: ").strip().upper()
                    dvd_ditemukan = False

                    for dvd in koleksi_dvd:
                        if dvd[0] == id_dvd:
                            dvd_ditemukan = True

                            print("\nJudul:", dvd[1], "| Harga saat ini: Rp", dvd[4], "| Stok saat ini:", dvd[5])

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
                                    dvd[4] = int(harga_baru)
                                if stok_baru != "":
                                    dvd[5] = int(stok_baru)
                                print("\nData DVD berhasil diperbarui!")

                            break

                    if not dvd_ditemukan:
                        print("\nDVD tidak ditemukan!")

                    input("Tekan Enter untuk kembali ke menu admin...")

                elif menu_admin == "5":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                           HAPUS DVD")
                    print("======================================================================================================")

                    for dvd in koleksi_dvd:
                        print("ID:", dvd[0], "| Judul:", dvd[1], "| Genre:", dvd[2], "| Tahun:", dvd[3], "| Harga sewa: Rp", dvd[4], "| Stok:", dvd[5])
                        print("======================================================================================================")

                    id_dvd = input("ID DVD yang ingin dihapus: ").strip().upper()
                    indeks_hapus = -1
                    dvd_dipinjam = False

                    for i in range(len(koleksi_dvd)):
                        if koleksi_dvd[i][0] == id_dvd:
                            indeks_hapus = i
                            break

                    for transaksi in data_transaksi:
                        if transaksi[2] == id_dvd and transaksi[4] == "Dipinjam":
                            dvd_dipinjam = True

                    if indeks_hapus == -1:
                        print("\nDVD tidak ditemukan!")

                    elif dvd_dipinjam:
                        print("\nDVD tidak bisa dihapus karena masih dipinjam!")

                    else:
                        while True:
                            konfirmasi = input("\nYakin hapus DVD ini? (ya/tidak): ").strip().lower()
                            if konfirmasi == "ya":
                                del koleksi_dvd[indeks_hapus]
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
                        for penyewa in data_penyewa:
                            print("ID:", penyewa[0], "| Nama:", penyewa[1], "| Telepon:", penyewa[2], "| Alamat:", penyewa[3])
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
                        for penyewa in data_penyewa:
                            print("ID:", penyewa[0], "| Nama:", penyewa[1], "| Telepon:", penyewa[2], "| Alamat:", penyewa[3])
                            print("==========================================================")

                        id_penyewa = input("ID penyewa yang ingin diubah: ").strip().upper()
                        penyewa_ditemukan = False

                        for penyewa in data_penyewa:
                            if penyewa[0] == id_penyewa:
                                penyewa_ditemukan = True
                                nama_baru = input("\nNama baru (Enter jika tidak ingin diubah): ").strip()
                                telepon_baru = input("Nomor telepon baru (Enter jika tidak ingin diubah): ").strip()
                                alamat_baru = input("Alamat baru (Enter jika tidak ingin diubah): ").strip()
                                
                                if nama_baru != "":
                                    penyewa[1] = nama_baru

                                if telepon_baru != "":
                                    penyewa[2] = telepon_baru

                                if alamat_baru != "":
                                    penyewa[3] = alamat_baru

                                print("\nData penyewa berhasil diperbarui!")
                                break

                        if not penyewa_ditemukan:
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
                        for penyewa in data_penyewa:
                            print("ID:", penyewa[0], "| Nama:", penyewa[1], "| Telepon:", penyewa[2], "| Alamat:", penyewa[3])
                            print("==========================================================")

                        id_penyewa = input("ID penyewa yang ingin dihapus: ").strip().upper()
                        indeks_hapus = -1
                        masih_meminjam = False

                        for i in range(len(data_penyewa)):
                            if data_penyewa[i][0] == id_penyewa:
                                indeks_hapus = i
                                break

                        for transaksi in data_transaksi:
                            if transaksi[1] == id_penyewa and transaksi[4] == "Dipinjam":
                                masih_meminjam = True

                        if indeks_hapus == -1:
                            print("\nData penyewa tidak ditemukan!")

                        elif masih_meminjam:
                            print("\nPenyewa masih memiliki transaksi aktif dan tidak bisa dihapus!")

                        else:
                            while True:
                                konfirmasi = input("\nYakin hapus data penyewa? (ya/tidak): ").strip().lower()
                                if konfirmasi == "ya":
                                    del data_penyewa[indeks_hapus]
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
                        for transaksi in data_transaksi:
                            print("No:", transaksi[0], "| ID Penyewa:", transaksi[1], "| ID DVD:", transaksi[2], "| Durasi sewa:", transaksi[3], "| Status:", transaksi[4], "| Jumlah:", transaksi[5])
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
                        for transaksi in data_transaksi:
                            print("No:", transaksi[0], "| ID Penyewa:", transaksi[1], "| ID DVD:", transaksi[2], "| Durasi sewa:", transaksi[3], "| Status:", transaksi[4], "| Jumlah:", transaksi[5])
                            print("==========================================================")

                        no_transaksi = input("Nomor transaksi: ").strip().upper()
                        transaksi_ditemukan = False

                        for transaksi in data_transaksi:
                            if transaksi[0] == no_transaksi:
                                transaksi_ditemukan = True

                                if transaksi[4] == "Dikembalikan":
                                    print("\nDVD pada transaksi ini sudah dikembalikan.")

                                else:
                                    transaksi[4] = "Dikembalikan"
                                    
                                    for dvd in koleksi_dvd:
                                        if dvd[0] == transaksi[2]:
                                            dvd[5] += transaksi[5]
                                            break

                                    print("\nPengembalian berhasil diproses. Stok DVD telah ditambah.")

                                break

                        if not transaksi_ditemukan:
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
                        for transaksi in data_transaksi:
                            print("No:", transaksi[0], "| ID Penyewa:", transaksi[1], "| ID DVD:", transaksi[2], "| Durasi sewa:", transaksi[3], "| Status:", transaksi[4], "| Jumlah:", transaksi[5])
                            print("==========================================================")

                        no_transaksi = input("Nomor transaksi: ").strip().upper()

                        transaksi_ditemukan = False

                        for transaksi in data_transaksi:
                            if transaksi[0] == no_transaksi:
                                transaksi_ditemukan = True

                                if transaksi[4] == "Dikembalikan":
                                    print("\nDurasi tidak bisa ditambah karena DVD sudah dikembalikan!")

                                else:
                                    tambahan_input = input("Tambahan durasi peminjaman (hari): ").strip()

                                    if not tambahan_input.isdigit():
                                        print("Tambahan durasi harus berupa angka positif!")

                                    elif int(tambahan_input) <= 0:
                                        print("Tambahan durasi harus lebih dari 0!")

                                    else:
                                        durasi_lama = int(transaksi[3].split()[0])
                                        tambahan_durasi = int(tambahan_input)
                                        durasi_total = (durasi_lama + tambahan_durasi)
                                        transaksi[3] = (str(durasi_total) + " hari")

                                        print("\nDurasi peminjaman berhasil ditambah!")
                                        print("Durasi sebelumnya:", durasi_lama, "hari")
                                        print("Tambahan durasi:", tambahan_durasi, "hari")
                                        print("Total durasi sekarang:", durasi_total, "hari")

                                break

                        if not transaksi_ditemukan:
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
                        for dvd in koleksi_dvd:
                            print("ID:", dvd[0], "| Judul:", dvd[1], "| Genre:", dvd[2], "| Tahun:", dvd[3], "| Harga sewa: Rp", dvd[4], "| Stok:", dvd[5])
                            print("======================================================================================================")

                    input("\nTekan Enter untuk kembali...")

                elif menu_pengguna == "2":
                    os.system("cls")
                    print("==========================================")
                    print("                CARI DVD")
                    print("==========================================")

                    mencari = input("Masukkan judul film yang dicari: ").strip().lower()
                    ditemukan = False

                    for dvd in koleksi_dvd:
                        if mencari in dvd[1].lower():
                            print("\nID:", dvd[0], "| Judul:", dvd[1], "| Genre:", dvd[2], "| Tahun:", dvd[3], "| Harga: Rp", dvd[4], "| Stok:", dvd[5])
                            ditemukan = True

                    if not ditemukan:
                        print("DVD tidak ditemukan!")

                    input("\nTekan Enter untuk kembali...")


                elif menu_pengguna == "3":
                    os.system("cls")
                    print("======================================================================================================")
                    print("                                            SEWA DVD")
                    print("======================================================================================================")

                    for dvd in koleksi_dvd:
                        print("ID:", dvd[0], "| Judul:", dvd[1], "| Genre:", dvd[2], "| Tahun:", dvd[3], "| Harga sewa: Rp", dvd[4], "| Stok:", dvd[5])
                        print("======================================================================================================")

                    id_dvd = input("ID DVD yang ingin disewa: ").strip().upper()
                    dvd_ditemukan = False

                    for dvd in koleksi_dvd:
                        if dvd[0] == id_dvd:
                            dvd_ditemukan = True

                            print("\nJudul:", dvd[1])
                            print("Harga sewa per DVD per hari: Rp", dvd[4])
                            print("Stok tersedia:", dvd[5])

                            jumlah_input = input("\nJumlah DVD yang ingin disewa: ").strip()

                            if not jumlah_input.isdigit() or int(jumlah_input) <= 0:
                                print("Jumlah sewa harus berupa angka positif!")

                            elif int(jumlah_input) > dvd[5]:
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

                                        data_penyewa.append([id_penyewa, nama_penyewa, telepon, alamat, username])

                                        data_transaksi.append([id_transaksi, id_penyewa, id_dvd, str(durasi_sewa) + " hari", "Dipinjam", int(jumlah_input), username])

                                        dvd[5] -= int(jumlah_input)

                                        total_harga = dvd[4] * int(jumlah_input) * durasi_sewa

                                        nomor_penyewa += 1
                                        nomor_transaksi += 1

                                        print("\nPenyewaan berhasil!")
                                        print("Nomor transaksi:", id_transaksi)
                                        print("Durasi sewa:", durasi_sewa, "hari")
                                        print("Total harga sewa: Rp", total_harga)


                            break

                    if not dvd_ditemukan:
                        print("DVD tidak ditemukan!")

                    input("\nTekan Enter untuk kembali...")


                elif menu_pengguna == "4":
                    os.system("cls")
                    print("==========================================================")
                    print("                     TRANSAKSI SAYA")
                    print("==========================================================")
                    transaksi_pengguna = False
                    
                    for transaksi in data_transaksi:
                        if transaksi[6] == username:
                            print("No:", transaksi[0], "| ID Penyewa:", transaksi[1], "| ID DVD:", transaksi[2], "| Durasi sewa:", transaksi[3], "| Status:", transaksi[4], "| Jumlah:", transaksi[5])
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