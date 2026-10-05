nama = "kansa"
nim = "64"

percobaan = 0
maksimal_percobaan = 3
login_berhasil = False

while percobaan < maksimal_percobaan:
    print("============= 👤 LOGIN 👤 ================")   
    username = input("Masukkan username: ").lower().strip()
    password = input("Masukkan password: ").strip()
    print("==========================================")

    if username == "" or password =="":
        print("Username dan password tidak boleh kosong!")
        continue

    if username == nama and password == nim:
        print("Login berhasil!")
        login_berhasil = True
        break

    elif username != nama and password == nim:
        print("Username salah!")

    elif username == nama and password != nim:
        print("Password salah!")

    else:
        print("Username dan password salah!")

    percobaan += 1
    print(f"Sisa percobaan login: {maksimal_percobaan - percobaan}")

if not login_berhasil:
    print("Anda mencapai batas maksimum percobaan login!")
    print("Program dihentikan.")

else:
    while True:
        print("========== 🍽️  PILIHAN PAKET 🍽️  ===========")
        print("1. Paket Reguler - 1 Porsi")
        print("2. Paket Anak - 1 Porsi")
        print("3. Paket Keluarga - 4 Porsi")
        print("4. Keluar")
        print("==========================================")

        opsi = input("Masukkan pilihan anda (1 - 4): ")
        print("==========================================")

        if opsi == "":
            print("Pilihan tidak boleh kosong!")
            continue

        if not opsi.isdigit():
            print("Pilihan harus berupa angka!")
            continue

        opsi = int(opsi)

        if opsi < 1 or opsi > 4:
            print("Pilihan tidak valid! Masukkan angka 1 - 4.")
            continue

        if opsi == 1:
            paket = "Paket Reguler"
            porsi = 1

        elif opsi == 2:
            paket = "Paket Anak"
            porsi = 1

        elif opsi == 3:
            paket = "Paket Keluarga"
            porsi = 4

        else:
            print("Terima kasih telah menggunakan program ini!")
            print("========= 👋  Program Berakhir 👋  =========")
            break

        while True:
            jumlah_input = input(f"Jumlah {paket} yang ingin anda distribusikan: ")

            if jumlah_input == "":
                print("==========================================")
                print("Jumlah tidak boleh kosong!")
                continue

            if not jumlah_input.isdigit():
                print("==========================================")
                print("Jumlah harus berupa angka!")
                continue

            jumlah_paket = int(jumlah_input)

            if jumlah_paket <= 0:
                print("==========================================")
                print("Jumlah paket untuk didistribusikan harus lebih dari 0!")
                continue

            break

        total_porsi = 0

        for i in range(jumlah_paket):
            total_porsi += porsi

        jumlah_penerima = total_porsi

        if total_porsi >= 20:
            bonus = "5 Paket Buah"

        elif total_porsi >= 10 and total_porsi < 20:
            bonus = "3 Botol Susu" 

        elif total_porsi >= 5 and total_porsi < 10:
            bonus = "1 Paket Vitamin"

        else:
            bonus = "-"

        print("== 🍔 PAKET YANG AKAN DIDISTRIBUSIKAN 🍔 ==")
        print(f"Jenis Paket: {paket}")
        print(f"Jumlah Paket: {jumlah_paket} Paket")
        print(f"Total Porsi: {total_porsi} Porsi")
        print(f"Penerima Manfaat: {jumlah_penerima} Orang")
        print(f"Bonus: {bonus}")