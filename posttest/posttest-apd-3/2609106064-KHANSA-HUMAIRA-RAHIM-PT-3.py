nama = "kansa"
nim = "64"

print("===========================")
username = input("Masukkan username: ").lower().strip()
password = input("Masukkan password: ").lower().strip()
print("===========================")

if username == nama:
    if password == nim:
        print("Login berhasil! ✅")
        print("===========================")

        total_point = int(input("Masukkan total point anda: "))

        if total_point >= 0 and total_point <= 99:
            print("===========================")
            print(f"Hai, {username}! ^___^")
            print("Rank anda sekarang = Rokie")
            print("Rank selanjutnya = Warrior")
            print("===========================")
            print(f"⚠️  Untuk mendapatkan rank Warrior, anda membutuhkan {100 - total_point} point lagi :D ⚠️")
            print("===========================")

        elif total_point >= 100 and total_point <= 299:
            print("===========================")
            print(f"Hai, {username}! ^___^")
            print("Rank anda sekarang = Warrior")
            print("Rank selanjutnya = Master")
            print("===========================")
            print(f"⚠️  Untuk mendapatkan rank Master, anda membutuhkan {300 - total_point} point lagi :D ⚠️")
            print("===========================")

        elif total_point >= 300 and total_point <= 999:
            print("===========================")
            print(f"Hai, {username}! ^___^")
            print("Rank anda sekarang = Master")
            print("Rank selanjutnya = Grand Master")
            print("===========================")
            print(f"⚠️  Untuk mendapatkan rank Grand Master, anda membutuhkan {1000 - total_point} point lagi :D ⚠️")
            print("===========================")

        elif total_point >= 1000 and total_point <= 4999:
            print("===========================")
            print(f"Hai, {username}! ^___^")
            print("Rank anda sekarang = Grand Master")
            print("Rank selanjutnya = Legend")
            print("===========================")
            print(f"⚠️  Untuk mendapatkan rank Legend, anda membutuhkan {5000 - total_point} point lagi :D ⚠️")
            print("===========================")
    
        elif total_point >= 5000:
            print("===========================")
            print(f"Hai, {username}! ^___^")
            print("Rank anda sekarang = Legend")
            print("===========================")
            print("🎊 Selamat! Anda berada di rank tertinggi :D 🎊")
            print("===========================")

        else:
            print("===========================")
            print("Point tidak valid.. (┬┬﹏┬┬) Point tidak boleh kurang dari 0!")
            print("===========================")
    else:
        print("Password salah! (┬┬﹏┬┬)")
        print("===========================")
else:
    print("Username salah! (┬┬﹏┬┬)")
    print("===========================")