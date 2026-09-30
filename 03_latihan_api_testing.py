"""
MODUL 3: Latihan API Testing dengan Python (requests + pytest)
--------------------------------------------------------------
QA Engineer sering menguji server/backend secara langsung melalui API
menggunakan library `requests` di Python.

Pada latihan ini, kita menguji publik API gratis (JSONPlaceholder)
untuk memverifikasi:
1. Apakah server merespons dengan status 200 OK?
2. Apakah waktu respons server cepat (< 2 detik)?
3. Apakah isi data JSON sesuai harapan?
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_api_ambil_profil_user():
    """Menguji endpoint GET /users/1"""
    response = requests.get(f"{BASE_URL}/users/1", timeout=5)

    # 1. Cek Status Code harus 200 (OK / Berhasil)
    assert response.status_code == 200

    # 2. Cek Kecepatan Server (Response Time harus di bawah 2 detik)
    waktu_respons_detik = response.elapsed.total_seconds()
    assert waktu_respons_detik < 2.0, f"Server terlalu lambat: {waktu_respons_detik} detik"

    # 3. Cek Isi Data JSON (Dictionary di Python)
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "Bret"
    assert "@" in data["email"]  # Pastikan format email mengandung karakter '@'


def test_api_user_tidak_ditemukan_negative_test():
    """Negative Test: Menguji bagaimana respons server jika kita meminta ID user yang tidak ada (99999)"""
    response = requests.get(f"{BASE_URL}/users/99999", timeout=5)

    # Server yang baik harus mengembalikan status 404 (Not Found), bukan 500 (Server Crash)
    assert response.status_code == 404
