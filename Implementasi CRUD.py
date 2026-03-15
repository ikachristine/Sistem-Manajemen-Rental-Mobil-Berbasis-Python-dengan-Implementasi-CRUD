# CAPSTONE PROJECT MODULE 1 

# Sistem Manajemen Rental Mobil “Medantour” Berbasis Python dengan Implementasi CRUD



print("==========Selamat datang di Medantour==========")
mobil_dict = {
    "1":
        {"Merk": "Agya", "Transmisi": "Manual", "Kapasitas": 1000, "Kursi": 5, "Unit": 5, "Sewa": "Lepas Kunci", "Harga": 300000},
    "2" :
        {"Merk": "Agya", "Transmisi": "Matic", "Kapasitas": 1000, "Kursi": 5, "Unit": 6, "Sewa": "Lepas Kunci", "Harga": 365000},
    "3" :
        {"Merk": "Ayla", "Transmisi": "Manual", "Kapasitas": 1000, "Kursi": 5, "Unit": 4, "Sewa": "Lepas Kunci", "Harga": 250000},
    "4":
        {"Merk": "Ayla", "Transmisi": "Matic", "Kapasitas": 1000, "Kursi": 5, "Unit": 6, "Sewa": "Lepas Kunci", "Harga": 300000},
    "5" :
        {"Merk": "Ertiga", "Transmisi": "Manual", "Kapasitas": 1500, "Kursi": 7, "Unit": 5, "Sewa": "Lepas Kunci", "Harga": 350000},
    "6" :
       {"Merk": "Ertiga", "Transmisi": "Matic", "Kapasitas": 1500, "Kursi": 7, "Unit": 4, "Sewa": "Lepas Kunci", "Harga":400000},
    "7":
        {"Merk": "Mobilio", "Transmisi": "Manual", "Kapasitas": 1500, "Kursi": 7, "Unit": 3, "Sewa": "Lepas Kunci", "Harga": 350000},
    "8" :
        {"Merk": "Mobilio", "Transmisi": "Matic", "Kapasitas": 1500, "Kursi": 7, "Unit": 4, "Sewa": "Lepas Kunci", "Harga":400000},
    "9":
        {"Merk": "Honda Brio", "Transmisi": "Manual", "Kapasitas": 1200, "Kursi": 5, "Unit": 8, "Sewa": "Lepas Kunci", "Harga": 300000},
    "10":
        {"Merk": "Honda Brio", "Transmisi": "Matic", "Kapasitas": 1200, "Kursi": 5, "Unit": 10, "Sewa": "Lepas Kunci", "Harga": 350000},
    "11":
        {"Merk": "Innova", "Transmisi": "Manual", "Kapasitas": 1300, "Kursi": 7, "Unit": 3, "Sewa": "Lepas Kunci", "Harga": 450000},
    "12":
        {"Merk": "Innova", "Transmisi": "Matic", "Kapasitas": 1300, "Kursi": 7, "Unit": 2, "Sewa": "Lepas Kunci", "Harga": 500000},
    "13":
        {"Merk": "Calya", "Transmisi": "Manual", "Kapasitas": 1200, "Kursi": 7, "Unit": 4, "Sewa": "Lepas Kunci", "Harga": 350000},
    "14":
        {"Merk": "Calya", "Transmisi": "Matic", "Kapasitas": 1200, "Kursi": 7, "Unit": 4, "Sewa": "Lepas Kunci", "Harga": 415000},
    "15":
        {"Merk": "Sigra", "Transmisi": "Manual", "Kapasitas": 1200, "Kursi": 7, "Unit": 6, "Sewa": "Lepas Kunci", "Harga": 350000},
    "16":
        {"Merk": "Innova Reborn", "Transmisi": "Manual", "Kapasitas": 2000, "Kursi": 7, "Unit": 9, "Sewa": "Lepas Kunci", "Harga": 500000},
    "17":
        {"Merk": "Avanza", "Transmisi": "Manual", "Kapasitas": 1300, "Kursi": 7, "Unit": 12, "Sewa": "Lepas Kunci", "Harga": 350000},
    "18":
        {"Merk": "Toyota HIACE", "Transmisi": "Matic", "Kapasitas": 2500, "Kursi": 14, "Unit": 2, "Sewa": "Sopir + BBM", "Harga": 1500000},
    "19":
        {"Merk": "Hiace PREMIO", "Transmisi": "Matic", "Kapasitas": 2800, "Kursi": 12, "Unit": 4, "Sewa": "Sopir + BBM", "Harga": 2000000},
    "20":
        {"Merk": "Fortuner", "Transmisi": "Manual", "Kapasitas": 2400, "Kursi": 7, "Unit": 5, "Sewa": "Sopir + BBM", "Harga": 2000000},
        }
recycle_bin = {}

#function
def tampilkan_menu():
    print (""""
      ==========List Menu:==========
        1. Menampilkan Daftar Sewa Mobil
        2. Melakukan Tambah Daftar Mobil
        3. Update Data Mobil
        4. Menghapus Daftar Mobil
        5. Sewa Mobil
        6. Exit Program 
      ===============================
         """)

def menu_lihat_mobil():

    while True:

        print("\n=== SUB MENU LIHAT DATA MOBIL ===")
        print("1. Tampilkan Semua Mobil")
        print("2. Cari Mobil")
        print("3. Sortir Mobil")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tampilkan_daftar_mobil()

        elif pilihan == "2":
            cari_mobil()

        elif pilihan == "3":
            sortir_mobil()

        elif pilihan == "4":
            print("Kembali ke menu utama...")
            break

        else:
            print("Pilihan tidak valid!")

def tampilkan_daftar_mobil():
    header = "{:<6} | {:<15} | {:<12} | {:<13} | {:<5} | {:<4} | {:<12} | {:<10}".format(
        "Kode", "Merk Mobil", "Transmisi", "Kapasitas(cc)", "Kursi", "Unit", "Tipe Sewa", "Harga"
    )
    print(header)
    print("-" * 100)

    for kode, data in mobil_dict.items():
        row = "{:<6} | {:<15} | {:<12} | {:<13} | {:<5} | {:<4} | {:<12} | Rp {:<10}".format(
            kode,
            data["Merk"],
            data["Transmisi"],
            data["Kapasitas"],
            data["Kursi"],
            data["Unit"],
            data["Sewa"],
            data["Harga"]
        )
        print(row)

def cari_mobil():
    while True:

        print("\n=== MENU PENCARIAN MOBIL ===")
        print("1. Cari berdasarkan Merk")
        print("2. Cari berdasarkan Transmisi")
        print("3. Kembali")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":

            keyword = input("Masukkan merk mobil yang dicari: ").lower()

            found = False

            print("\nHasil Pencarian:")
            print("{:<6} | {:<15} | {:<12} | {:<13} | {:<5} | {:<4} | {:<12} | {:<10}".format(
                "Kode", "Merk", "Transmisi", "Kapasitas", "Kursi", "Unit", "Sewa", "Harga"
            ))
            print("-" * 90)

            for kode, data in mobil_dict.items():
                if keyword in data["Merk"].lower():
                    found = True
                    print("{:<6} | {:<15} | {:<12} | {:<13} | {:<5} | {:<4} | {:<12} | Rp {:<10}".format(
                        kode,
                        data["Merk"],
                        data["Transmisi"],
                        data["Kapasitas"],
                        data["Kursi"],
                        data["Unit"],
                        data["Sewa"],
                        data["Harga"]
                    ))

            if not found:
                print("Mobil dengan merk tersebut tidak ditemukan.")

        elif pilihan == "2":

            print("\nCari berdasarkan transmisi")
            print("1. Manual")
            print("2. Matic")

            pilih_transmisi = input("Pilih transmisi (1/2): ")

            if pilih_transmisi == "1":
                transmisi = "Manual"
            elif pilih_transmisi == "2":
                transmisi = "Matic"
            else:
                print("Pilihan tidak valid!")
                continue

            found = False

            print("\nHasil Pencarian:")
            print("{:<6} | {:<15} | {:<12} | {:<13} | {:<5} | {:<4} | {:<12} | {:<10}".format(
                "Kode", "Merk", "Transmisi", "Kapasitas", "Kursi", "Unit", "Sewa", "Harga"
            ))
            print("-" * 90)

            for kode, data in mobil_dict.items():
                if data["Transmisi"].lower() == transmisi.lower():
                    found = True
                    print("{:<6} | {:<15} | {:<12} | {:<13} | {:<5} | {:<4} | {:<12} | Rp {:<10}".format(
                        kode,
                        data["Merk"],
                        data["Transmisi"],
                        data["Kapasitas"],
                        data["Kursi"],
                        data["Unit"],
                        data["Sewa"],
                        data["Harga"]
                    ))

            if not found:
                print("Mobil dengan transmisi tersebut tidak ditemukan.")

        elif pilihan == "3":
            break

        else:
            print("Pilihan tidak valid!")

def sortir_mobil():
    print("\n=== Sortir Mobil Berdasarkan Harga Sewa ===")
    print("1. Sortir dari harga Termurah")
    print("2. Sortir dari harga Termahal")

    pilihan = input("Pilih Urutan(1/2): ")

    # reverse_setting : dipakai untuk mengatur apakah suatu data akan diurutkan secara normal atau terbalik
    if pilihan == "1":
        reverse_setting = False #-> urut normal
    elif pilihan == "2":
        reverse_setting = True
    else:
        print("Pilihan tidak valid!")
        return

    # Proses sorting
    hasil_sortir = sorted(
        mobil_dict.items(),
        key=lambda x: x[1]["Harga"],
        reverse=reverse_setting
    )

    # Header tabel
    print("\n=== Hasil Sortir Berdasarkan Harga ===\n")
    print(
        "{:<5} | {:<15} | {:<10} | {:<10} | {:<10} | {:<10}".format(
            "Kode", "Merk", "Transmisi", "CC", "Harga", "Unit"
        )
    )
    print("-" * 75)

    # Isi tabel
    for kode, data in hasil_sortir:
        print(
            "{:<5} | {:<15} | {:<10} | {:<10} | {:<10} | {:<10}".format(
                kode,
                data["Merk"],
                data["Transmisi"],
                data["Kapasitas"],
                data["Harga"],
                data["Unit"]
            )
        )

def tambah_mobil():
    while True:

        print("\n=== SUB MENU TAMBAH DAFTAR MOBIL ===")
        print("1. Tambah Mobil")
        print("2. Kembali")

        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":

            tampilkan_daftar_mobil()

            merk = input("Masukkan merk mobil: ")
            transmisi = input("Masukkan transmisi mobil (M/A): ")
            kapasitas = int(input("Masukkan kapasitas cc mobil: "))
            kursi = int(input("Masukkan jumlah kursi dalam mobil: "))
            unit = int(input("Masukkan jumlah unit mobil yang tersedia: "))
            sewa = input("Masukkan tipe sewa mobil (lepas kunci / dengan supir): ")
            harga = int(input("Masukkan harga sewa mobil: "))

            # ===== CEK DUPLIKAT =====
            duplicate = False

            for kode, data in mobil_dict.items():
                if (data["Merk"].lower() == merk.lower() and
                    data["Transmisi"].lower() == transmisi.lower() and
                    data["Kapasitas"] == kapasitas):

                    print("\n❗ Mobil", merk, "sudah ada dalam daftar! (Kode:", kode, ")")
                    duplicate = True
                    break

            if duplicate:
                continue

            # ===== KONFIRMASI =====
            konfirmasi = input("\nApakah Anda yakin ingin menambahkan mobil ini? (y/n): ")

            if konfirmasi.lower() != "y":
                print("Penambahan dibatalkan.")
                continue

            # ===== GENERATE INDEX BARU =====
            if mobil_dict:
                new_index = str(max(int(k) for k in mobil_dict.keys()) + 1)
            else:
                new_index = "1"

            # ===== SIMPAN DATA =====
            mobil_dict[new_index] = {
                "Merk": merk,
                "Transmisi": transmisi,
                "Kapasitas": kapasitas,
                "Kursi": kursi,
                "Unit": unit,
                "Sewa": sewa,
                "Harga": harga
            }

            print("\nMobil", merk, transmisi, "berhasil ditambahkan dengan kode:", new_index, "\n")
            tampilkan_daftar_mobil()

        elif pilihan == "2":
            print("Kembali ke menu utama...")
            break

        else:
            print("Pilihan tidak valid!")

def update_mobil():

    tampilkan_daftar_mobil()

    kode = input("\nMasukkan kode mobil yang ingin diupdate: ")

    if kode not in mobil_dict:
        print("Data mobil tidak ditemukan!")
        return

    print("\nPilih data yang ingin diubah:")
    print("1. Merk")
    print("2. Transmisi")
    print("3. Kapasitas")
    print("4. Kursi")
    print("5. Unit")
    print("6. Tipe Sewa")
    print("7. Harga")

    pilihan = input("Pilih menu (1-7): ")

    kolom = {
        "1": "Merk",
        "2": "Transmisi",
        "3": "Kapasitas",
        "4": "Kursi",
        "5": "Unit",
        "6": "Sewa",
        "7": "Harga"
    }

    if pilihan not in kolom:
        print("Pilihan tidak valid!")
        return

    field = kolom[pilihan]

    print("\nData lama:", mobil_dict[kode][field])

    nilai_baru = input("Masukkan nilai baru: ")

    konfirmasi = input("Yakin ingin mengubah data ini? (y/n): ")

    if konfirmasi.lower() != "y":
        print("Update dibatalkan.")
        return

    if field in ["Kapasitas","Kursi","Unit","Harga"]:
        nilai_baru = int(nilai_baru)

    mobil_dict[kode][field] = nilai_baru

    print("\nData berhasil diperbarui!")
    tampilkan_daftar_mobil()

def hapus_mobil():
    tampilkan_daftar_mobil()

    while True:

        print("\n=== MENU HAPUS MOBIL ===")
        print("1. Hapus Data Mobil")
        print("2. Lihat Recycle Bin")
        print("3. Restore Data Mobil")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-4): ")

        # =========================
        # HAPUS DATA
        # =========================
        if pilihan == "1":

            tampilkan_daftar_mobil()

            kode = input("Masukkan kode mobil yang ingin dihapus: ")

            if kode in mobil_dict:

                merk = mobil_dict[kode]["Merk"]
                transmisi = mobil_dict[kode]["Transmisi"]

                konfirmasi = input(
                    f"Apakah Anda yakin ingin menghapus {merk} {transmisi}? (y/n): "
                )

                if konfirmasi.lower() == "y":

                    # pindahkan ke recycle bin
                    recycle_bin[kode] = mobil_dict[kode]

                    # hapus dari data utama
                    mobil_dict.pop(kode)

                    print("Data berhasil dipindahkan ke Recycle Bin.")

                else:
                    print("Penghapusan dibatalkan.")

            else:
                print("Kode mobil tidak ditemukan.")

        # =========================
        # LIHAT RECYCLE BIN
        # =========================
        elif pilihan == "2":

            if not recycle_bin:
                print("Recycle Bin kosong.")
            else:
                print("\n=== DATA DI RECYCLE BIN ===")
                for kode, data in recycle_bin.items():
                    print(kode, "-", data["Merk"], data["Transmisi"], "- Rp", data["Harga"])

        # =========================
        # RESTORE DATA
        # =========================
        elif pilihan == "3":

            if not recycle_bin:
                print("Recycle Bin kosong.")
            else:

                print("\n=== DATA DI RECYCLE BIN ===")
                for kode, data in recycle_bin.items():
                    print(kode, "-", data["Merk"], data["Transmisi"], "- Rp", data["Harga"])

                kode = input("\nMasukkan kode mobil yang ingin direstore: ")

                if kode in recycle_bin:

                    mobil_dict[kode] = recycle_bin[kode]
                    recycle_bin.pop(kode)

                    print("\nData berhasil direstore!")

                    print("\n=== DAFTAR MOBIL TERBARU ===")
                    tampilkan_daftar_mobil()

                else:
                    print("Kode tidak ditemukan di recycle bin.")

        # =========================
        # KEMBALI KE MENU UTAMA
        # =========================
        elif pilihan == "4":
            break

        else:
            print("Menu tidak valid!")



def sewa_mobil():
    cart=[]
    total_harga = 0

    tampilkan_daftar_mobil()
    print("------------------------------------------------------------------------------------------------------------------")

    while True:
        kode_mobil = input("Masukkan kode mobil yang ingin dirental: ")
       
        if kode_mobil in mobil_dict:
            qty = int(input("Masukkan jumlah unit yang ingin dirental: "))

            if  qty <= mobil_dict[kode_mobil]['Unit']:
                merk = mobil_dict[kode_mobil]['Merk']
                transmisi = mobil_dict[kode_mobil]['Transmisi']
                kapasitas = mobil_dict[kode_mobil]['Kapasitas']
                kursi = mobil_dict[kode_mobil]['Kursi']
                sewa = mobil_dict[kode_mobil]['Sewa']
                harga = mobil_dict[kode_mobil]['Harga']

                #kurangi unit mobil
                mobil_dict[kode_mobil]['Unit'] -= qty

                #tambahkan ke cart
                cart.append({
                    "Merk": merk, 
                    "Transmisi": transmisi, 
                    "Kapasitas": kapasitas,
                    "Kursi": kursi, 
                    "qty": qty, 
                    "Sewa": sewa,
                    "Harga": harga})
                print(f"{qty} {merk} berhasil ditambahkan ke daftar rental!")
            else:
                print(f"Maaf, jumlah unit mobil {mobil_dict[kode_mobil]['Merk']} tidak mencukupi! Tersisa {mobil_dict[kode_mobil]['Unit']} unit. Silakan pilih mobil yang lain. ")

        print("Isi Cart :")
        header = "{:<15} | {:<10} | {:<10} | {:<5} | {:<5} | {:<12} | {:<10}".format(
            "Merk", "Transmisi", "Kapasitas", "Kursi", "Unit", "Sewa", "Harga"
        )
        print(header)
        print("-" * 80)

        for item in cart:
            row = "{:<15} | {:<10} | {:<10} | {:<5} | {:<5} | {:<12} | Rp {:<10}".format(
                item["Merk"],
                item["Transmisi"],
                item["Kapasitas"],
                item["Kursi"],
                item["qty"],           # jumlah unit yang disewa
                item["Sewa"],
                item["Harga"]
            )
            print(row)

        lagi = input("Mau rental mobil yang lain? (ya/tidak) = ")
        if lagi == "ya":
            continue
        else:
            break
    
    #tampilkan daftar rental
    print("Daftar Rental :")
    header = "{:<15} | {:<10} | {:<10} | {:<5} | {:<5} | {:<12} | {:<10}".format(
            "Merk", "Transmisi", "Kapasitas", "Kursi", "Unit", "Sewa", "Harga"
        )
    print(header)
    print("-" * 80)
    for item in cart:
        total_item = item["qty"] * item["Harga"]
        total_harga += total_item
        row = "{:<15} | {:<10} | {:<10} | {:<5} | {:<5} | {:<12} | Rp {:<10}".format(
                item["Merk"],
                item["Transmisi"],
                item["Kapasitas"],
                item["Kursi"],
                item["qty"],           # jumlah unit yang disewa
                item["Sewa"],
                item["Harga"]
            )
        print(row)

    print("Total Harus Dibayar = Rp", total_harga)

    #proses pembayaran
    while True:
        uang = int(input("Masukkan jumlah uang = "))
        if uang >= total_harga:
            kembalian = uang - total_harga
            print("Uang kembali anda =", kembalian)
            print("Terima kasih telah menggunakan layanan rental kami!")
              # Kosongkan cart setelah transaksi selesai
            cart.clear()
            print(" ")
            break
        else:
            print("Saldo Anda tidak mencukupi. Silakan coba kembali.")


#panggil function
while True:
    tampilkan_menu()
    menu_no = input("Masukkan angka menu yang ingin dijalankan: ")

    if menu_no == "1":
        menu_lihat_mobil()
    elif menu_no == "2":
        tambah_mobil()
    elif menu_no == "3":
        update_mobil()  
    elif menu_no == "4":
        hapus_mobil()
    elif menu_no == "5":
        sewa_mobil()  
    elif menu_no == "6": 
        print("Terima kasih sudah melakukan reservasi, pesanan Anda telah kami terima!")
        break
    
    else:
        print("Menu tidak tersedia!")

    print("\n-----------------------------------------------------------------------------\n")
