# CREATE
# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# print(formula1)

# print(formula1[0:5])

# for index,elemen in enumerate(formula1, start=1):
#     print(f"{index}. {elemen}")

# MENAMBAH
# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)

# sirkuit.append("Daniel")
# print(sirkuit)

# sirkuit.append("Nando")
# print(sirkuit)

# sirkuit.extend(["Larry", "Rendy"])
# print(sirkuit)

# sirkuit.insert(2, "Alfi")
# print(sirkuit)

# MENGUBAH
# sirkuit[3] = "Apip"
# print(sirkuit)

# # nama_list[start:stop:step]
# sirkuit[0:5:2] = ["Rizky", "Naufal", "Rizal"]
# print(sirkuit)

# # MENGHAPUS
# del sirkuit[0]
# print(sirkuit)

# sirkuit.remove("Apip")
# print(sirkuit)

# ambil_sirkuit = sirkuit.pop(2)
# print(ambil_sirkuit)
# print(sirkuit)

# SLICING LIST
# print(sirkuit[0:3:2])

# OPERATOR PENJUMLAHAN
# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]

# gabung_team = team1 + team2
# print(gabung_team)

# OPERATOR PENGULANGAN
# pemenang = team1 * 3
# print(pemenang)

# NESTED LIST
# lineup = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]
# print(lineup[3][0])

# for i in lineup:
#     print(i)

# for i in lineup:
#     for j in i:
#         print(j)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)

# print(type(listchara))

# listchara.append("Yui")

# chara = tuple(listchara)
# print(chara)

# data_harian = ["Senin", 36.5, "Selasa", 37.1, "Rabu", 36.8, "Kamis", 37.0, "Jumat", 36.6]

# for index,elemen in enumerate(data_harian[1:9:2], start=1):
#     print(f"{index}. {elemen}")