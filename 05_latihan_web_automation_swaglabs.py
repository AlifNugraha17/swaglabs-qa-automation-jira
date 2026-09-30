"""
MODUL 5: Web Automation Testing di Swag Labs (saucedemo.com) dengan Python + Selenium + Pytest
----------------------------------------------------------------------------------------------
Script ini mengotomatiskan pengujian tiket Jira SCRUM-5 yang baru saja Anda buat:
"[Product Catalog] All product thumbnails incorrectly display a placeholder dog image for problem_user"

Apa yang dilakukan Robot Python ini?
1. Membuka browser Google Chrome secara otomatis (Headless/Background).
2. Menguji akun `standard_user` -> Memastikan TIDAK ada gambar anjing (sl-404).
3. Menguji akun `problem_user`  -> Membuktikan bahwa Python otomatis mendeteksi BUG gambar anjing (SCRUM-5)!
"""

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    """Menyiapkan browser Chrome otomatis yang MUNCUL DI LAYAR Anda."""
    opsi = Options()
    # Membuka Chrome secara Full Screen (Maximized) agar langsung terlihat di depan layar
    opsi.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=opsi)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def login_dan_ambil_gambar_pertama(driver, username: str, password: str) -> str:
    """Fungsi bantuan untuk Login ke Swag Labs dan mengambil URL gambar produk pertama."""
    driver.get("https://www.saucedemo.com/")
    time.sleep(1.5)  # Jeda agar Anda bisa melihat halaman depan terbuka

    # 1. Ketik Username & Password, lalu klik Login secara otomatis
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(1.5)  # Jeda setelah mengetik username
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1.5)  # Jeda setelah mengetik password
    driver.find_element(By.ID, "login-button").click()

    time.sleep(4)  # Jeda 4 detik di halaman katalog produk agar Anda bisa melihat gambar tas / anjingnya!

    # 2. Ambil link gambar (src) pada produk pertama (Sauce Labs Backpack)
    elemen_gambar = driver.find_element(By.CSS_SELECTOR, "img.inventory_item_img")
    return elemen_gambar.get_attribute("src")


def test_SCRUM5_retest_standard_user_gambar_harus_benar(browser):
    """
    [QA Retest - PASSED]
    Verifikasi bahwa pada akun `standard_user`, foto produk BUKAN gambar anjing (sl-404).
    """
    url_gambar = login_dan_ambil_gambar_pertama(browser, "standard_user", "secret_sauce")
    print(f"\n[INFO] URL Gambar pada standard_user: {url_gambar}")

    # Pastikan nama file gambar mengandung 'sauce-backpack' dan BUKAN 'sl-404' (gambar anjing)
    assert "sl-404" not in url_gambar, f"Masih muncul gambar anjing: {url_gambar}"
    assert "sauce-backpack" in url_gambar


def test_SCRUM5_deteksi_bug_gambar_anjing_pada_problem_user(browser):
    """
    [Simulasi Penemuan Bug SCRUM-5 oleh Robot Python]
    Saat login dengan `problem_user`, test ini akan otomatis GAGAL (FAILED)
    dan melaporkan bahwa gambar yang muncul adalah gambar anjing (sl-404)!
    """
    url_gambar = login_dan_ambil_gambar_pertama(browser, "problem_user", "secret_sauce")
    print(f"\n[INFO] URL Gambar pada problem_user: {url_gambar}")

    # Kita uji: Harusnya gambar produk BUKAN gambar anjing (sl-404)
    assert "sl-404" not in url_gambar, (
        f"[BUG SCRUM-5 TERDETEKSI OTOMATIS OLEH PYTHON!] "
        f"Expected: foto backpack, Actual: muncul foto anjing ({url_gambar})"
    )


if __name__ == "__main__":
    # Memungkinkan Anda langsung klik tombol Play (Run Python File ▶️) di pojok kanan atas Antigravity IDE!
    pytest.main(["-v", "-s", __file__])

