"""
MODUL 6: Full Automated Test Suite untuk Swag Labs (saucedemo.com)
------------------------------------------------------------------
File Python ini menguji SELURUH 6 Skenario & Bug yang ada di daftar To-Do Jira Anda:
1. TC01: Login Valid (standard_user) -> PASS
2. TC02: Login Akun Terkunci (locked_out_user) -> PASS
3. TC03: Belanja End-to-End sampai Checkout Berhasil (standard_user) -> PASS
4. TC04: Deteksi Bug Kecepatan Loading Lambat > 3 detik (performance_glitch_user) -> FAIL (BUG!)
5. TC05: Deteksi Bug Filter Harga Low-to-High Rusak (problem_user) -> FAIL (BUG!)
6. TC06: Deteksi Bug Kotak Last Name Tidak Bisa Diketik saat Checkout (problem_user) -> FAIL (BUG!)
"""

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


@pytest.fixture
def browser():
    """Membuka Chrome secara Full Screen (Mode Incognito agar popup Save Password Chrome tidak menutupi tombol Keranjang!)."""
    opsi = Options()
    opsi.add_argument("--start-maximized")
    opsi.add_argument("--incognito")  # Mematikan popup peringatan 'Change your password' dari Chrome!
    opsi.add_argument("--disable-notifications")
    opsi.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def login(driver, username: str, password: str = "secret_sauce"):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


# ==============================================================================
# PENGUJIAN 1: Akun Terkunci (locked_out_user) -> Harus Muncul Pesan Error
# ==============================================================================
def test_01_login_locked_out_user_harus_ditolak(browser):
    login(browser, "locked_out_user")
    time.sleep(1.5)
    pesan_error = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Sorry, this user has been locked out" in pesan_error


# ==============================================================================
# PENGUJIAN 2: Belanja Normal dari Awal sampai Checkout Selesai (standard_user)
# ==============================================================================
def test_02_checkout_end_to_end_standard_user_berhasil(browser):
    login(browser, "standard_user")
    time.sleep(1)

    # Klik Add to Cart pada Backpack, lalu buka Keranjang
    tombol_add = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    browser.execute_script("arguments[0].click();", tombol_add)

    tombol_keranjang = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    browser.execute_script("arguments[0].click();", tombol_keranjang)
    time.sleep(1)

    # Klik Checkout & isi data pembeli
    tombol_checkout = browser.find_element(By.ID, "checkout")
    browser.execute_script("arguments[0].click();", tombol_checkout)
    browser.find_element(By.ID, "first-name").send_keys("Alif")
    browser.find_element(By.ID, "last-name").send_keys("Nugraha")
    browser.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(1)

    browser.find_element(By.ID, "continue").click()
    browser.find_element(By.ID, "finish").click()
    time.sleep(1.5)

    # Pastikan muncul pesan Thank you for your order!
    judul_sukses = browser.find_element(By.CLASS_NAME, "complete-header").text
    assert judul_sukses == "Thank you for your order!"


# ==============================================================================
# PENGUJIAN 3: Cek Kecepatan Login (Menangkap BUG performance_glitch_user)
# ==============================================================================
def test_03_cek_kecepatan_login_performance_glitch_user(browser):
    waktu_mulai = time.time()
    login(browser, "performance_glitch_user")
    durasi_detik = time.time() - waktu_mulai

    # Standar SLA perusahaan: Login wajib selesai di bawah 3.0 detik!
    assert durasi_detik < 3.0, (
        f"[BUG PERFORMANCE TERDETEKSI!] Login terlalu lambat: {durasi_detik:.2f} detik (Batas maksimal: 3.0 detik)"
    )


# ==============================================================================
# PENGUJIAN 4: Cek Filter Harga Termurah (Menangkap BUG Sorting di problem_user)
# ==============================================================================
def test_04_cek_filter_harga_termurah_problem_user(browser):
    login(browser, "problem_user")
    time.sleep(1)

    # Pilih filter 'Price (low to high)'
    dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value("lohi")
    time.sleep(1.5)

    # Ambil daftar semua harga barang yang tampil di layar
    elemen_harga = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    daftar_harga = [float(el.text.replace("$", "")) for el in elemen_harga]

    # Pastikan harga sudah berurutan dari paling murah ($7.99) ke paling mahal ($49.99)
    assert daftar_harga == sorted(daftar_harga), (
        f"[BUG SORTING TERDETEKSI!] Filter Harga (Low to High) gagal mengurutkan barang! "
        f"Urutan di layar: {daftar_harga}"
    )


# ==============================================================================
# PENGUJIAN 5: Cek Form Checkout Last Name (Menangkap BUG Blocker di problem_user)
# ==============================================================================
def test_05_cek_form_checkout_lastname_problem_user(browser):
    login(browser, "problem_user")
    tombol_add = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    browser.execute_script("arguments[0].click();", tombol_add)
    tombol_keranjang = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    browser.execute_script("arguments[0].click();", tombol_keranjang)
    tombol_checkout = browser.find_element(By.ID, "checkout")
    browser.execute_script("arguments[0].click();", tombol_checkout)
    time.sleep(1)

    # Ketik First Name: Alif, lalu Last Name: Nugraha
    browser.find_element(By.ID, "first-name").send_keys("Alif")
    browser.find_element(By.ID, "last-name").send_keys("Nugraha")
    time.sleep(1.5)

    isi_last_name = browser.find_element(By.ID, "last-name").get_attribute("value")
    assert isi_last_name == "Nugraha", (
        f"[BUG CRITICAL CHECKOUT TERDETEKSI!] Kolom Last Name gagal diisi! "
        f"Expected: 'Nugraha', Actual: '{isi_last_name}'"
    )


# ==============================================================================
# PENGUJIAN 6 (SCRUM-10): Cek Tombol Remove di Katalog Produk (problem_user)
# ==============================================================================
def test_06_cek_tombol_remove_macet_problem_user(browser):
    login(browser, "problem_user")
    time.sleep(1)

    # 1. Klik Add to Cart pada Backpack (angka keranjang jadi 1)
    tombol_add = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    browser.execute_script("arguments[0].click();", tombol_add)
    time.sleep(1)

    # 2. Coba klik tombol Remove untuk membatalkan barang
    tombol_remove = browser.find_element(By.ID, "remove-sauce-labs-backpack")
    browser.execute_script("arguments[0].click();", tombol_remove)
    time.sleep(1.5)

    # 3. Cek apakah tombol Remove masih nyangkut (tidak kembali jadi Add to Cart)
    masih_ada_remove = len(browser.find_elements(By.ID, "remove-sauce-labs-backpack")) > 0
    assert not masih_ada_remove, (
        "[BUG SCRUM-10 TERDETEKSI!] Tombol Remove sudah diklik tetapi barang gagal dihapus dari keranjang!"
    )


# ==============================================================================
# PENGUJIAN 7 (SCRUM-12): Cek Tombol Finish Saat Bayar Akhir (error_user)
# ==============================================================================
def test_07_cek_tombol_finish_macet_error_user(browser):
    login(browser, "error_user")
    tombol_add = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    browser.execute_script("arguments[0].click();", tombol_add)
    tombol_keranjang = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    browser.execute_script("arguments[0].click();", tombol_keranjang)
    tombol_checkout = browser.find_element(By.ID, "checkout")
    browser.execute_script("arguments[0].click();", tombol_checkout)

    browser.find_element(By.ID, "first-name").send_keys("Alif")
    browser.find_element(By.ID, "postal-code").send_keys("12345")
    browser.find_element(By.ID, "continue").click()
    time.sleep(1)

    # Klik tombol Finish di halaman Checkout Overview
    tombol_finish = browser.find_element(By.ID, "finish")
    browser.execute_script("arguments[0].click();", tombol_finish)
    time.sleep(1.5)

    # Harusnya pindah ke /checkout-complete.html, tapi di error_user malah nyangkut!
    assert "checkout-complete.html" in browser.current_url, (
        f"[BUG SCRUM-12 TERDETEKSI!] Tombol Finish mati total! URL masih nyangkut di: {browser.current_url}"
    )


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])

