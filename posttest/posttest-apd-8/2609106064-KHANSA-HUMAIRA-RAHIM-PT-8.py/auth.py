from data import data_akun
from utils import clear_terminal, enter, input_teks


def register():
    clear_terminal()
    try:
        print("========= REGISTER =========")
        username_baru = input_teks("Buat Username: ").lower()
        password_baru = input_teks("Buat Password: ").lower()
        print("============================")
        if username_baru in data_akun:
            raise ValueError("Username sudah terpakai!")
        
    except ValueError as e:
        print(f"\n{e}")

    else:
        data_akun[username_baru] = {"password": password_baru, "peran": "pengguna"}
        print("\nRegister berhasil! Silakan login.")

    finally:
        enter("Tekan Enter untuk kembali...")

def login():
    clear_terminal()
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