# 🏛️ Prediksi CPNS Kemenkeu - Panduan Instalasi dan Penggunaan

Aplikasi prediksi kelulusan CPNS Kementerian Keuangan menggunakan 5 model Machine Learning dengan akurasi hingga 87.76%.

---

## 🤖 Apa itu Aplikasi Ini?

Aplikasi **Prediksi CPNS Kemenkeu** adalah sistem cerdas yang dapat memprediksi kemungkinan kelulusan peserta CPNS Kementerian Keuangan berdasarkan:
- Umur peserta
- Nilai IPK
- Nilai SKD (Seleksi Kompetensi Dasar)
- Nilai SKB (Seleksi Kompetensi Bidang)

Aplikasi menggunakan 5 model AI berbeda untuk memberikan prediksi yang akurat:
- **SVM** (Support Vector Machine)
- **Decision Tree** (Pohon Keputusan)
- **Random Forest** (Hutan Acak)
- **K-NN** (K-Nearest Neighbors)
- **Naïve Bayes**

---

## 🎮 Cara Menjalankan Aplikasi

### Untuk Windows:
1. **Buka Command Prompt** (tekan Windows + R, ketik `cmd`, tekan Enter)
2. **Navigasi ke folder aplikasi**:
   ```bash
   cd Desktop\Fastwork
   ```
3. **Jalankan aplikasi**:
   ```bash
   streamlit run cpns_streamlit_app.py
   ```

### Untuk Mac:
1. **Buka Terminal**
2. **Navigasi ke folder aplikasi**:
   ```bash
   cd Desktop/Fastwork
   ```
3. **Jalankan aplikasi**:
   ```bash
   streamlit run cpns_streamlit_app.py
   ```

### ✅ Tanda Aplikasi Berhasil Jalan:

Setelah menjalankan perintah di atas, Anda akan melihat pesan seperti ini:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

**Browser akan otomatis terbuka** dan menampilkan aplikasi. Jika tidak terbuka otomatis:
1. **Buka browser**
2. **Ketik** `http://localhost:8501` di address bar
3. **Tekan Enter**

---

## 📱 Cara Menggunakan Aplikasi

### 1. Isi Data Peserta:
- **Nama Lengkap**: Masukkan nama lengkap peserta
- **Umur**: Masukkan umur
- **Nilai IPK**: Masukkan IPK
- **Nilai SKD**: Masukkan nilai SKD
- **Nilai SKB**: Masukkan nilai SKB

### 2. Klik Tombol "🔮 Prediksi"

### 3. Baca Hasil Prediksi:
Aplikasi akan menampilkan:
- **Data peserta** yang sudah diinput
- **Prediksi dari 5 model** dengan tingkat akurasi masing-masing
- **Hasil prediksi** berupa:
  - **P/L**
  - **TL**
  - **TH**
  - **TMS-1**

---

## 🔧 Mengatasi Masalah

### Problem 1: "Python tidak dikenali" atau "'python' is not recognized"
**Solusi:**
- Python belum terinstall dengan benar
- Ulangi instalasi Python dan pastikan centang "Add Python to PATH"
- Restart komputer setelah instalasi

### Problem 2: "pip tidak dikenali" atau "'pip' is not recognized"
**Solusi Windows:**
- Gunakan `python -m pip install -r requirements.txt` sebagai gantinya

**Solusi Mac:**
- Gunakan `pip3` instead of `pip`

### Problem 3: Error saat install requirements
**Solusi:**
- Pastikan koneksi internet stabil
- Coba jalankan lagi perintah instalasi
- Jika masih error, install satu per satu:
  ```bash
  pip install streamlit
  pip install pandas
  pip install numpy
  pip install scikit-learn
  pip install plotly
  pip install joblib
  pip install openpyxl
  pip install imblearn
  ```

### Problem 4: Browser tidak terbuka otomatis
**Solusi:**
- Buka browser manual
- Ketik `http://localhost:8501` di address bar
- Pastikan tidak ada aplikasi lain yang menggunakan port 8501

### Problem 5: Aplikasi lambat atau not responding
**Solusi:**
- Pastikan komputer memiliki RAM minimal 4GB
- Tutup aplikasi lain yang tidak perlu
- Restart aplikasi dengan tekan Ctrl+C di terminal, lalu jalankan ulang

### Problem 6: Model tidak ditemukan
**Solusi:**
- Pastikan folder `models` ada di dalam folder aplikasi
- Pastikan semua file `.joblib` ada di dalam folder `models`
- Jangan pindahkan atau hapus file apapun dari folder aplikasi

---

## 📝 Catatan Penting

- ⚠️ **Jangan hapus atau pindahkan** file apapun dari folder aplikasi
- 💡 **Aplikasi perlu koneksi internet** hanya saat instalasi pertama
- 🔄 **Untuk menghentikan aplikasi**: Tekan `Ctrl+C` di terminal/command prompt
- 📱 **Aplikasi bisa diakses dari komputer lain** di jaringan yang sama menggunakan Network URL

---

**© 2024 Prediksi CPNS Kemenkeu - Machine Learning Application** 