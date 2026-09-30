# 📋 Modul 1: Praktik Langsung Manual QA di Website Asli (Swag Labs) & Jira

Panduan ini menggunakan website latihan QA **asli** yang bisa langsung Anda klik dan coba di browser:
👉 **[https://www.saucedemo.com/](https://www.saucedemo.com/)** ( bernama **Swag Labs** )

---

## 1. Apa Tugas Anda Sekarang?
Bayangkan perusahaan Anda baru saja membuat website toko online **[Swag Labs (saucedemo.com)](https://www.saucedemo.com/)**.
Sebagai **QA Engineer**, tugas Anda adalah **mencoba Login ke website tersebut**, lalu mencatat hasilnya ke **Jira**.

---

## 2. Mari Coba 3 Percobaan Ini di Tab Browser "Swag Labs" Anda:

### Percobaan 1 (Positive Test — Harus Berhasil Masuk)
1. Buka tab **[https://www.saucedemo.com/](https://www.saucedemo.com/)** di Chrome Anda.
2. Ketik di kotak **Username**: `standard_user`
3. Ketik di kotak **Password**: `secret_sauce`
4. Klik tombol **Login**.
5. **Hasil**: Anda berhasil masuk ke halaman daftar produk tas & baju! (Artinya: **PASS / Lulus Uji**).

*(Klik menu garis tiga di pojok kiri atas $\rightarrow$ klik **Logout** untuk kembali ke halaman depan).*

---

### Percobaan 2 (Negative Test — Coba Login Tanpa Isi Password)
1. Di halaman depan **[https://www.saucedemo.com/](https://www.saucedemo.com/)**, ketik **Username**: `standard_user`
2. **Kosongkan** kotak **Password** (jangan diisi apa-apa).
3. Klik tombol **Login**.
4. **Hasil**: Muncul kotak merah bertuliskan: `Epic sadface: Password is required`. (Artinya: **PASS**, karena aplikasi berhasil mencegah orang masuk tanpa password).

---

### Percobaan 3 (Menemukan BUG Asli di Swag Labs!)
Website `saucedemo.com` sengaja menyediakan akun khusus yang **rusak (ada bug-nya)** agar Anda bisa merasakan bagaimana rasanya menemukan Bug sebagai QA!

1. Di halaman depan **[https://www.saucedemo.com/](https://www.saucedemo.com/)**, ketik **Username**: `problem_user`
2. Ketik **Password**: `secret_sauce`
3. Klik tombol **Login**.
4. **Perhatikan Halaman Produk yang Muncul!**:
   - Lihat foto-foto produknya! Semua foto barang (tas, baju, jaket) malah berubah menjadi **foto anjing yang sama semua**!
   - Coba klik tombol **Add to cart** pada barang *Sauce Labs Bolt T-Shirt* atau *Sauce Labs Fleece Jacket* — tombolnya **macet tidak bisa diklik**!

🎉 **SELAMAT!** Anda baru saja menemukan **BUG ASLI** di aplikasi!

---

## 3. Cara Melaporkan Bug Tersebut ke Tab JIRA Anda

Sekarang, pindah ke tab **Jira (`Board - SCRUM Sprint...`)** yang sudah terbuka di browser Chrome Anda:

1. Klik tombol biru **`+ Create`** di bagian atas layar Jira.
2. Pada bagian **Issue Type**, pilih **`Bug`** (atau `Task` jika opsi Bug tidak muncul).
3. Pada kotak **Summary (Judul)**, copy-paste kalimat ini:
   `[Halaman Produk] Semua foto produk salah tampil menjadi gambar anjing pada akun problem_user`
4. Pada kotak **Description (Deskripsi)**, copy-paste laporan QA berikut ini:
   ```text
   Langkah Memunculkan Bug (Steps to Reproduce):
   1. Buka website https://www.saucedemo.com/
   2. Login menggunakan Username: problem_user dan Password: secret_sauce
   3. Klik tombol Login dan perhatikan katalog produk.

   Harapan (Expected Result):
   Setiap produk menampilkan foto barang yang sesuai (tas, kaos, jaket).

   Kenyataan (Actual Result):
   Semua produk menampilkan foto anjing yang sama.
   ```
5. Klik tombol biru **`Create`** di pojok kanan bawah.
