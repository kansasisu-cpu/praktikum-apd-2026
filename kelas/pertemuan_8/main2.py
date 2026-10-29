# import inquirer
# from prettytable import PrettyTable

# # Deklarasi struktur dictionary untuk menampung data mahasiswa
# data_mahasiswa = {
#     "nim": [],
#     "nama": [],
#     "kelas": []
# }

# def tambah_data():
#     pertanyaan = [
#         inquirer.Text("nim", message="Input NIM kamu"),
#         inquirer.Text("nama", message="Input nama lengkapmu"),
#         inquirer.List("kelas", message="Pilih kelas", choices=["A", "B", "C"]),
#     ]

#     jawaban = inquirer.prompt(pertanyaan)

#     data_mahasiswa
#     data_mahasiswa["nim"].append(jawaban["nim"])
#     data_mahasiswa["nama"].append(jawaban["nama"])
#     data_mahasiswa["kelas"].append(jawaban["kelas"])

# def tampil_data():
#     tabel = PrettyTable()
#     tabel.field_names = ["No", "NIM", "Nama", "Kelas"]
#     for i in range(len(data_mahasiswa["nim"])):
#         tabel.add_row([
#             i + 1,
#             data_mahasiswa["nim"][i],
#             data_mahasiswa["nama"][i],
#             data_mahasiswa["kelas"][i]
#         ])
#     print(tabel)

# tambah_data()
# tampil_data()

data_akun = {
    "kansa" : {"password" : "64", "peran" : "admin"}
}

def enter(pesan="Tekan Enter untuk kembali..."):
    input("\n" + pesan)

def input_teks(pesan):
    teks = input(pesan).strip() 

    if teks == "":
        raise ValueError("Input tidak boleh kosong!")
    
    return teks

def login():
    hasil = None
    try:
        print("========== LOGIN ==========")
        username = input_teks("Username: ").lower()
        password = input_teks("Password: ").lower()
        print("============================")

        akun = data_akun[username]

        if akun["password"] != password:
            raise ValueError("Password salah! Silahkan login ulang.")
        
    except KeyError:
        print("\nAkun tidak terdaftar! Silahkan register.")
        enter("Tekan Enter untuk kembali ke menu utama...")

    except ValueError as e:
        print(f"\n{e}")
        enter("Tekan Enter untuk kembali ke menu utama...")

    else:
        hasil = (username, akun["peran"])

    return hasil

login()