# 📊 Modul 4: Pengenalan Grafana & Performance Testing untuk QA

Setelah Anda menguasai **Jira** (untuk laporan bug) dan **Python Pytest** (untuk menguji kebenaran fitur), pertanyaan berikutnya adalah:
> *"Fitur Login sudah benar. Tapi bagaimana jika ada **10.000 orang** yang Login secara bersamaan saat Flash Sale jam 12.00? Apakah server akan kuat atau tumbang?"*

Di sinilah seorang QA menggunakan **Load Testing Tool (Python Locust / Grafana k6)** yang dipadukan dengan **Grafana Dashboard**.

---

## 1. Alur Kerja Python / k6 $\rightarrow$ Database $\rightarrow$ Grafana

```
[Script Load Test (Python Locust / Grafana k6)]
       │
       ├──► Menembak 1.000 request/detik ke Server Aplikasi
       │
       └──► Mengirim data hasil tes ke Database Metrik (Prometheus / InfluxDB)
                   │
                   ▼
         [ GRAFANA DASHBOARD ]
         Menampilkan grafik warna-warni secara Real-Time!
```

---

## 2. Empat Grafik Utama yang Wajib Dibaca QA di Grafana

Saat Anda membuka dashboard **Grafana** ketika pengujian berlangsung, ada 4 angka/grafik yang wajib Anda perhatikan dan laporkan ke tim:

1. **Virtual Users (VUs)**:
   - Jumlah robot/pengguna simulasi yang sedang mengakses aplikasi pada detik tersebut (misal: naik bertahap dari 10 $\rightarrow$ 500 $\rightarrow$ 1.000 user).
2. **Throughput / RPS (*Requests Per Second*)**:
   - Berapa banyak transaksi per detik yang sanggup dilayani server.
3. **Response Time / Latency (`p95` dan `p99`)**:
   - Di Grafana, QA jarang melihat nilai rata-rata (*Average*) karena bisa menipu.
   - QA melihat **`p95` (Percentile 95)**: Artinya *95% pengguna merasakan waktu loading di bawah angka tersebut*.
   - **Standar bagus**: `p95 < 500 ms` (0.5 detik). Jika di grafik Grafana `p95` tembus `5.000 ms` (5 detik), berarti server mulai kewalahan!
4. **Error Rate (`%`)**:
   - Persentase request yang gagal (HTTP `500`, `502 Bad Gateway`, `504 Gateway Timeout`).
   - **Standar bagus**: Error rate harus **`0%`** (atau `< 0.1%`). Jika grafik Error Rate di Grafana naik menjadi merah saat user mencapai 800 orang, maka batas kekuatan server Anda adalah 800 user!

---

## 3. Contoh Script Load Testing dengan Python (`Locust`)
Karena Anda sudah bisa Python, Anda bisa membuat simulasi ribuan user hanya dengan beberapa baris kode Python menggunakan library `locust`:

```python
from locust import HttpUser, task, between

class SimulasiUserToko(HttpUser):
    # Jeda waktu antar klik layaknya manusia asli (1 sampai 3 detik)
    wait_time = between(1, 3)

    @task(3)
    def buka_halaman_produk(self):
        self.client.get("/posts")

    @task(1)
    def lihat_detail_produk(self):
        self.client.get("/posts/1")
```
Hasil pengujian di atas nantinya dihubungkan ke **Grafana** agar manajer dan tim developer bisa melihat grafiknya secara langsung.
