🚗 **Medantour Car Rental Management System**

**📌 Project Overview**

Medantour Car Rental Management System adalah mini aplikasi berbasis Python (CLI / Command Line Interface) yang dibuat untuk membantu pengelolaan data rental mobil secara sederhana.

Aplikasi ini dikembangkan sebagai Capstone Project Module 1 dengan menerapkan konsep dasar pemrograman Python seperti:

- Data Collection (Dictionary & List)
- Conditional Statement
- Looping
- Function
- CRUD (Create, Read, Update, Delete)

Sistem ini memungkinkan pengguna untuk mengelola daftar mobil rental, melakukan pencarian mobil, menyewa mobil, serta mengelola data mobil dengan fitur tambahan seperti Recycle Bin untuk menghindari penghapusan data secara permanen.

**⚙️ Features**

1️⃣ View Data **(Read)**

Menampilkan seluruh daftar mobil rental dalam bentuk tabel yang rapi.

Fitur tambahan:
- Melihat seluruh data mobil
- Pencarian mobil berdasarkan:
  - Merk mobil
  - Transmisi
- Sorting mobil berdasarkan harga

2️⃣ Add Data **(Create)**

Menambahkan mobil baru ke dalam sistem.

Fitur:
- Validasi untuk mencegah data duplikat
- Konfirmasi sebelum menambahkan data
- Menampilkan daftar mobil terbaru setelah data berhasil ditambahkan

3️⃣ **Update** Data

Mengubah data mobil berdasarkan kode mobil (ID).

User dapat memilih kolom yang ingin diubah, seperti:
- Merk mobil
- Transmisi
- Kapasitas mesin
- Jumlah kursi
- Unit mobil
- Tipe sewa
- Harga sewa

4️⃣ **Delete** Data

Menghapus data mobil dari sistem.

Fitur tambahan:
- Konfirmasi sebelum menghapus data
- Sistem Recycle Bin sehingga data yang dihapus tidak langsung hilang permanen

Submenu:
- Hapus mobil
- Lihat recycle bin
- Restore data mobil

5️⃣ Rental Transaction

Melakukan proses penyewaan mobil.

Fitur:
- Memilih mobil berdasarkan kode
- Menentukan jumlah unit mobil yang ingin disewa
- Sistem otomatis mengurangi jumlah unit mobil yang tersedia
- Keranjang (cart) rental
- Perhitungan total harga
- Sistem pembayaran dan kembalian

**🚀 Future Improvements**

Beberapa pengembangan yang dapat dilakukan:
- Sistem pengembalian mobil (return car)
- Penyimpanan data menggunakan database (MySQL / SQLite)
- Sistem login admin

