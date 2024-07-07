# Visualisasi Data Timbulan Sampah di Indonesia

Proyek ini menggunakan Flask untuk membuat visualisasi data timbulan sampah di Indonesia berdasarkan provinsi dan kategori. Data yang digunakan diambil dari [Sistem Informasi Pengelolaan Sampah Nasional (SIPS) Kementerian Lingkungan Hidup dan Kehutanan](https://sipsn.menlhk.go.id/sipsn/public/data/timbulan) yang disimpan dalam waste_data.xlsx.

## Deskripsi Proyek

Proyek ini memanfaatkan Flask sebagai framework web untuk menyajikan visualisasi data dalam bentuk grafik menggunakan Matplotlib dan Seaborn. Terdapat beberapa fitur utama:

- **Visualisasi Berdasarkan Pulau**: Pengguna dapat memilih pulau (Jawa, Sumatra, Kalimantan, Sulawesi, Maluku & Papua, Bali & Nusa Tenggara) untuk melihat grafik jumlah timbulan sampah tahunan dari provinsi-provinsi di pulau tersebut.
- **Grafik Kategori Sampah**: Grafik ini menunjukkan kategori provinsi-provinsi berdasarkan rata-rata timbulan sampah tahunan, diwarnai sesuai dengan kategori (Hijau, Orange, Merah).
- **Jumlah Provinsi per Kategori**: Grafik ini menunjukkan jumlah provinsi yang masuk ke dalam setiap kategori sampah (Hijau, Orange, Merah).

## Setup

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1. **Instalasi Dependencies**:
   Pastikan Anda telah menginstal Python dan pip. Kemudian, instal semua dependencies yang dibutuhkan dengan menjalankan perintah berikut di terminal:

2. **Menjalankan Flask**:
Jalankan aplikasi Flask dengan menjalankan perintah berikut di terminal:

Aplikasi akan berjalan di `http://127.0.0.1:5000/`.

3. **Akses Aplikasi**:
Buka browser dan akses `http://127.0.0.1:5000/` untuk melihat visualisasi data.

## Struktur Proyek

- `app.py`: Berkas utama Flask yang berisi definisi aplikasi dan rute-rute API.
- `data/waste_data.xlsx`: Berkas Excel yang berisi data timbulan sampah per provinsi dan tahun.
- `templates/index.html`: Template HTML untuk tampilan utama aplikasi.
- `static/js/script.js`: Berkas JavaScript untuk meng-handle permintaan dan menampilkan grafik-grafik.

## Google Colab

Anda dapat mengakses notebook Google Colab yang digunakan untuk analisis dan persiapan data awal [di sini](https://colab.research.google.com/drive/1tfkHJZSyuctcJet-qifhphA6F3sZiqw0?usp=sharing).
