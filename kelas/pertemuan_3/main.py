budget = 20000
cuaca = "hujan"

if budget > 30000 and cuaca == "cerah":
    print("Beli Yoshinoya")
else:
    print("Masak Indomie Aja")

kendaraan = input("Masukkan jenis kendaraan anda: ").lower().strip()

if kendaraan == "mobil":
    tarif_parkir = 10_000
elif kendaraan == "motor":
    tarif_parkir = 5_000
elif kendaraan == "sepeda":
    tarif_parkir = 6_700
else:
    tarif_parkir = 15_000

print("Tarif parkir yang harus anda bayar:", tarif_parkir)

umur = 20
status = "Dewasa" if umur >= 18 else "Belum Dewasa"

usia = int(input("Masukkan usia anda: "))
print("Dilarang masuk!") if usia < 16 else print("Selamat datang!")

bilangan = -5
status = "bilangan negatif" if bilangan < 0 else "bilangan positif"

print("Bilangan adalah", status)

username = input("Masukkan username: ").lower().strip()
password = input("Masukkan password: ").lower().strip()

if username == "kansasisu":
    if password == "064":
        print("Login berhasil!")
    else:
        print("Password salah!")
else:
    print("Username tidak ditemukan!")

angka = 10 / 6
print(f"angka {angka:.02f}")