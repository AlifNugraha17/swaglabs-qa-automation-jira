# 🎯 Daftar Lengkap To-Do & Skenario Pengujian Swag Labs (`saucedemo.com`) untuk Jira

Website **[https://www.saucedemo.com/](https://www.saucedemo.com/)** memiliki **5 akun rahasia** dan **6 Bug Asli** yang sengaja disembunyikan di berbagai halaman (Login, Filter Harga, Keranjang, hingga Checkout).

Masukkan daftar tiket di bawah ini ke kolom **`To Do`** di papan **Jira** Anda (Klik tombol biru **`+ Create`** di atas layar Jira, atau klik tanda **`+ Create`** di bawah kolom **`To Do`**), lalu uji satu per satu!

---

## 🟦 KELOMPOK 1: Tiket `Task` (Tugas Pengujian Normal / Positive & Negative Test)
*(Saat membuat di Jira, pilih **Work Type: `Task` ☑️**)*

### 📋 To-Do 1: Menguji Akun yang Diblokir (`locked_out_user`)
- **Summary (Judul di Jira)**:
  `[Auth QA] Verify error message when logging in with a locked_out_user account`
- **Cara Anda Menguji di `saucedemo.com`**:
  1. Buka `https://www.saucedemo.com/`
  2. Isi Username: `locked_out_user` | Password: `secret_sauce`
  3. Klik **Login**.
  4. **Cek Hasilnya**: Apakah muncul pesan merah `"Epic sadface: Sorry, this user has been locked out."`? Jika ya, pindahkan tiket ini dari `To Do` $\rightarrow$ **`Done`**!

### 📋 To-Do 2: Menguji Belanja dari Awal sampai Selesai Checkout (`standard_user`)
- **Summary (Judul di Jira)**:
  `[E2E Checkout] Verify complete shopping flow from Add to Cart until Order Confirmation`
- **Cara Anda Menguji di `saucedemo.com`**:
  1. Login dengan `standard_user` | `secret_sauce`
  2. Klik **Add to cart** pada *Sauce Labs Backpack*.
  3. Klik ikon **Keranjang Belanja (`🛒 1`)** di pojok kanan atas $\rightarrow$ klik **Checkout**.
  4. Isi First Name: `Alif`, Last Name: `Nugraha`, Zip Code: `12345` $\rightarrow$ klik **Continue** $\rightarrow$ klik **Finish**.
  5. **Cek Hasilnya**: Jika muncul tulisan `"Thank you for your order!"`, ambil *screenshot*, lampirkan di komentar Jira, lalu geser ke **`Done`**!

---

## 🟥 KELOMPOK 2: Tiket `Bug` (5 Bug Rahasia Lainnya di `saucedemo.com`!)
*(Saat membuat di Jira, pilih **Work Type: `Bug` 🔴**)*

### 🐞 To-Do 3 (BUG CRITICAL): Kotak "Last Name" Rusak Saat Mau Bayar Checkout!
Ini adalah **Bug paling parah (Highest Priority)** di Swag Labs! Coba Anda buktikan sendiri di Chrome:
- **Cara Membuktikan Bug Ini di `saucedemo.com`**:
  1. Login dengan Username: `problem_user` | Password: `secret_sauce`
  2. Klik **Add to cart** pada barang pertama (`Sauce Labs Backpack`).
  3. Klik ikon **Keranjang (`🛒`)** di kanan atas $\rightarrow$ klik **Checkout**.
  4. Coba ketik nama Anda di kotak **First Name** (`Alif`), lalu coba ketik di kotak **Last Name** (`Nugraha`)!
  5. **LIHAT APA YANG TERJADI!** Saat Anda mengetik di kotak **Last Name**, hurufnya malah **masuk ke kotak First Name dan menghapus nama depan Anda**! Akibatnya, pelanggan **tidak akan pernah bisa membayar belanjaannya** (`Error: Last Name is required`)!
- **Summary (Judul Tiket Jira)**:
  `[Checkout Step 1] Typing into Last Name field overwrites First Name and blocks checkout for problem_user`
- **Priority**: `Highest`
- **Description (Copy-Paste ke Jira)**:
  ```text
  Steps to Reproduce:
  1. Log in as "problem_user" (Password: secret_sauce).
  2. Add "Sauce Labs Backpack" to the cart and navigate to Cart -> Checkout.
  3. Type "Alif" into the First Name field.
  4. Attempt to type "Nugraha" into the Last Name field and click Continue.

  Expected Result:
  Both First Name and Last Name fields accept input independently, allowing the user to proceed to Checkout Step 2.

  Actual Result:
  Typing into the Last Name field redirects keystrokes to the First Name field. The Last Name field remains empty, triggering "Error: Last Name is required" and completely blocking checkout.
  ```

---

### 🐞 To-Do 4 (BUG HIGH): Filter Urutan Harga (Low to High) Tidak Berfungsi!
- **Cara Membuktikan Bug Ini di `saucedemo.com`**:
  1. Login dengan `problem_user` | `secret_sauce`
  2. Di pojok kanan atas daftar produk, klik kotak filter **`Name (A to Z)`**, lalu ubah menjadi **`Price (low to high)`** (Harga termurah ke termahal).
  3. **LIHAT APA YANG TERJADI!** Urutan barangnya **sama sekali tidak berubah** (Tas seharga `$29.99` tetap di paling atas, padahal ada barang seharga `$7.99`)!
- **Summary (Judul Tiket Jira)**:
  `[Product Filter] Sorting dropdown (Price low to high) fails to reorder inventory items for problem_user`
- **Priority**: `High`
- **Description (Copy-Paste ke Jira)**:
  ```text
  Steps to Reproduce:
  1. Log in as "problem_user" on https://www.saucedemo.com/.
  2. On the Inventory page, click the sort dropdown in the top-right corner.
  3. Select "Price (low to high)".

  Expected Result:
  Products should be sorted in ascending order by price (starting from $7.99 Sauce Labs Onesie up to $49.99 Fleece Jacket).

  Actual Result:
  The product order remains unchanged ($29.99 Backpack stays first). Sorting filter fails silently.
  ```

---

### 🐞 To-Do 5 (BUG HIGH): Tombol "Remove" di Halaman Katalog Macet!
- **Cara Membuktikan Bug Ini di `saucedemo.com`**:
  1. Login dengan `problem_user` | `secret_sauce`
  2. Klik **Add to cart** pada *Sauce Labs Backpack*. Tombol berubah menjadi merah bertuliskan **`Remove`**.
  3. Sekarang klik tombol **`Remove`** tersebut untuk membatalkan belanja!
  4. **LIHAT APA YANG TERJADI!** Tombol **`Remove`** tidak bisa diklik sama sekali! Barang tetap nyangkut di keranjang!
- **Summary (Judul Tiket Jira)**:
  `[Product Catalog] Remove button on inventory cards fails to remove item from cart for problem_user`
- **Priority**: `Medium`

---

### 🐞 To-Do 6 (BUG PERFORMANCE): Loading Login Sangat Lambat (> 5 Detik)!
Ini adalah jembatan sempurna menuju **Grafana (Performance Testing)** nanti!
- **Cara Membuktikan Bug Ini di `saucedemo.com`**:
  1. Logout dulu ke halaman depan `https://www.saucedemo.com/`
  2. Login menggunakan Username: `performance_glitch_user` | Password: `secret_sauce`
  3. Klik tombol **Login** dan hitung berapa detik loadingnya!
  4. **LIHAT APA YANG TERJADI!** Halaman macet (*freeze*) selama **5 sampai 6 detik** sebelum terbuka (padahal standar SLA perusahaan harus di bawah 2 detik)!
- **Summary (Judul Tiket Jira)**:
  `[Performance] Login response time exceeds 5000ms SLA threshold for performance_glitch_user`
- **Priority**: `High`

---

### 🐞 To-Do 7 (BUG HIGH): Tombol "Finish" Saat Bayar Akhir Tidak Merespons (`error_user`)
- **Cara Membuktikan Bug Ini di `saucedemo.com`**:
  1. Login menggunakan Username: `error_user` | Password: `secret_sauce`
  2. Klik **Add to cart** pada *Sauce Labs Backpack* $\rightarrow$ buka **Keranjang (`🛒`)** $\rightarrow$ klik **Checkout**.
  3. Isi First Name `Alif`, Zip Code `12345` *(perhatikan: di `error_user` Last Name juga tidak bisa diketik, tapi anehnya masih bisa lanjut klik Continue!)*.
  4. Di halaman terakhir (**Checkout: Overview**), klik tombol **`Finish`**!
  5. **LIHAT APA YANG TERJADI!** Tombol **`Finish`** mati total! Pesanan tidak selesai!
- **Summary (Judul Tiket Jira)**:
  `[Checkout Overview] Clicking Finish button fails to submit order and throws JS error for error_user`
- **Priority**: `Highest`
