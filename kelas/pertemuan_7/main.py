# def sapa():
#     return "Haloo Khansa"

# teks_sapaan = sapa()
# print(teks_sapaan)

# def hitung():
#     return 5 * 3

# print(hitung())

# def hitung(angka1, angka2):
#     hasil = angka1 * angka2
#     return hasil

# print(hitung(2, 3))

# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# print(faktorial(4))

# def sapa(nama = 200):
#     return f"Halo, {nama}"

# print(sapa(300))

# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input harus angka!")
# else:
#     print("Angka:", angka)
# finally:
#     print("Program selesai")

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as error:
    print(error)