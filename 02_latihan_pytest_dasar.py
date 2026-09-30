"""
MODUL 2: Mengubah Basic Python Menjadi Skill QA dengan Pytest
-------------------------------------------------------------
Di dunia QA, kita menguji kode/aplikasi yang dibuat oleh Developer.
Inti dari Automation Testing di Python adalah perintah `assert`.

Rumus QA di Python:
    assert actual_result == expected_result
"""


# =====================================================================
# BAGIAN A: Simulasi Fungsi Aplikasi Buatan Developer (Misal: Kasir Toko)
# =====================================================================
def hitung_total_belanja(harga_barang: int, jumlah_beli: int, diskon_persen: int = 0) -> float:
    """Fungsi buatan developer untuk menghitung total bayar."""
    if jumlah_beli <= 0:
        raise ValueError("Jumlah beli harus lebih dari 0")

    subtotal = harga_barang * jumlah_beli
    potongan = subtotal * (diskon_persen / 100)

    # SENGAJA DIBUAT BUG OLEH DEVELOPER:
    # Jika diskon 50%, developer salah tulis rumus malah ditambah potongan, bukan dikurang!
    if diskon_persen == 50:
        return subtotal + potongan

    return subtotal - potongan


# =====================================================================
# BAGIAN B: Tugas Anda Sebagai QA Engineer (Menulis Test Case Otomatis)
# Perhatikan: Semua nama fungsi test di Pytest WAJIB diawali kata `test_`
# =====================================================================

def test_TC01_belanja_normal_tanpa_diskon():
    """Positive Test: Beli 2 barang seharga 10.000 tanpa diskon -> Harus 20.000"""
    expected_result = 20000
    actual_result = hitung_total_belanja(harga_barang=10000, jumlah_beli=2, diskon_persen=0)

    assert actual_result == expected_result


def test_TC02_belanja_dengan_diskon_10_persen():
    """Positive Test: Beli 1 barang seharga 100.000 diskon 10% -> Harus 90.000"""
    expected_result = 90000
    actual_result = hitung_total_belanja(harga_barang=100000, jumlah_beli=1, diskon_persen=10)

    assert actual_result == expected_result


def test_TC03_belanja_dengan_diskon_50_persen():
    """
    Positive Test: Beli 1 barang seharga 100.000 diskon 50% -> Seharusnya 50.000.
    Saat dijalankan, Pytest akan otomatis menangkap BUG buatan developer di atas!
    """
    expected_result = 50000
    actual_result = hitung_total_belanja(harga_barang=100000, jumlah_beli=1, diskon_persen=50)

    assert actual_result == expected_result, f"BUG DITEMUKAN! Harusnya {expected_result}, tapi hasilnya malah {actual_result}"
