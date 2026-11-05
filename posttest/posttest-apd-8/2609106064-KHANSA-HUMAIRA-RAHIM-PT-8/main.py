import inquirer

from tema import tema_awal
from utils import clear_terminal, enter
from auth import register, login
from menu import menu_admin, menu_pengguna


def main():
    try:
        while True:
            clear_terminal()
            print("======================================")
            print("        RENTAL DVD 'KANSASISU'")
            print("======================================")
            pertanyaan = [inquirer.List("pilihan", message="Pilih menu", choices=[" Register", " Login", " Keluar"])]

            jawaban = inquirer.prompt(pertanyaan, theme=tema_awal())

            if jawaban["pilihan"] == " Register":
                register()

            elif jawaban["pilihan"] == " Login":
                hasil = login()

                if hasil is not None:
                    username, peran = hasil

                    if peran == "admin":
                        menu_admin()

                    else:
                        menu_pengguna(username)

            elif jawaban["pilihan"] == " Keluar":
                break

            else:
                print("Opsi tidak valid! Masukkan pilihan 1 sampai 3.")
                enter("Tekan Enter untuk mencoba lagi...")

    finally:
        clear_terminal()
        print("Terima kasih telah mengakses program kami!")


if __name__ == "__main__":
    main()