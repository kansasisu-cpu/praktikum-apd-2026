skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

harga_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]

total_pengeluaran = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + 12000

konversi_yen = total_pengeluaran / 112.99

rata_rata = total_pengeluaran / len(harga_skincare)

nim = 64

bolean = nim < rata_rata

print("Skincare 1: Rp" + str(skincare_1))
print("Skincare 2: Rp" + str(skincare_2))
print("Skincare 3: Rp" + str(skincare_3))
print("Skincare 4: Rp" + str(skincare_4))
print("Skincare 5: Rp" + str(skincare_5))
print("Skincare 6: Rp" + str(skincare_6))
print("Total Pengeluaran: Rp" + str(total_pengeluaran))

print("NIM : " + str(nim))

print("Bolean : " + str(bolean))

print("Total Pengeluaran dalam Yen: ¥" + str(konversi_yen))

print("Isi Skincare 3 - 5: " + str(harga_skincare[-4:-1]))