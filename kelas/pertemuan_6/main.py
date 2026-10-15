# kartu = {"merah", "merah", "biru", "hijau"}

# kartu.add("hytam")

# kartu.remove("hijau")

# for warna in kartu:
#     print(warna)

# print(kartu)

# matkul = ["apd", "orsikom", "apd", "kalkulus"]

# sks = set(matkul)
# print(matkul)
# print(sks)

# aslab1 = {"fina", "shasha", "risma", "haekal"}
# aslab2 = {"larry", "attar", "haekal"}

# gabung = aslab1.difference(aslab2)

# print(gabung)

# setHasilUpdate = aslab1.update(aslab2)

# print(f"nilai aslab1: {aslab1}")
# print(f"nilai setHasilUpdate: {setHasilUpdate}")

# matkul = {
#     "matkul_ganjil" : "kalkulus",
#     "matkul_genap" : "statistik"
# }

# print(matkul["matkul_ganjil"])

# List_game = dict(Genshin_Impact="Open World", Mole="Moba",
# Stardew_Valley="Farming Simulation")

# print(List_game["Genshin_Impact"])

game = {
"pou" : "chill",
"genshin impact" : "action",
"valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

# print("Panjang dictionary: ", len(game))
# print(len(game))

# game["resident evil"] = "horror"

# game.update({"resident evil" : "horror"})
# print(game)

# game.setdefault("pou", "horror")
# print(game)


# for i,j in game.items():
#     print(f"{i} | {j}")

# menu = {
# "ayam geprek" : 15000,
# "ayam goreng" : 13000,
# "ayam bakar" : 17000,
# "nasi goreng" : 12000,
# "mie goreng" : 10000
# }
# menu_baru = menu.copy()
# print(menu)
# print(menu_baru)
# print("==============")

# del menu_baru["ayam geprek"]
# del menu_baru["ayam bakar"]

# print(menu)
# print(menu_baru)

menu = {
    "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
    "nasi" : ["nasi goreng", "nasi uduk"],
    "mie" : ["mie goreng rendang", "mie goreng aceh"],
    "kuah" : ["soto", "rawon", "sop iga"]
}

for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
    for kategori in j:
        print(kategori)
    print("")