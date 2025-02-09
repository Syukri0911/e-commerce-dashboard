# E-Commerce Data Analysis

## 📌 Overview
Analisis ini dilakukan pada dataset e-commerce yang mencakup berbagai aspek transaksi pelanggan, termasuk order, item pesanan, produk, dan ulasan pelanggan. Tujuan utama dari analisis ini adalah untuk menemukan insight menarik, membersihkan data, dan memahami tren bisnis yang dapat meningkatkan performa penjualan.

## 📂 Dataset Description
Dataset yang digunakan terdiri dari beberapa tabel berikut:
- **Orders**: Informasi tentang pesanan yang dibuat oleh pelanggan.
- **Order Items**: Detail item yang dipesan dalam setiap transaksi.
- **Products**: Informasi tentang produk yang dijual.
- **Order Reviews**: Feedback dan ulasan pelanggan tentang pesanan mereka.

## 📊 Data Summary
| Dataset           | Total Data | Missing Values | Persentase Missing |
|------------------|------------|----------------|----------------------|
| Orders          | 99,441      | 4,908          | 4.94%                |
| Order Items     | 112,650     | 0              | 0.00%                |
| Products        | 32,951      | 2,448          | 7.43%                |
| Order Reviews   | 99,224      | 145,903        | 147.04%               |

## 🛠️ Data Cleaning Strategy

### **🔹 Missing Values Handling**
1. **Orders:** Missing values dihapus atau diimputasi menggunakan nilai median jika relevan.
2. **Products:** Missing values dapat diisi dengan informasi dari produk lain dalam kategori yang sama.
3. **Order Reviews:**
   - **Jika hanya beberapa kolom yang hilang**, digunakan median/mode untuk imputasi.
   - **Jika banyak pelanggan tidak memberikan review**, dibuat kategori baru "No Review".
   - **Jika ditemukan anomali jumlah missing values > 100%**, dilakukan validasi dan cross-check dengan dataset lain.

## 📈 Insights & Findings
1. **Tingkat Missing Value di Order Reviews Sangat Tinggi (147.04%)** 🚨
   - Bisa jadi karena banyak pelanggan yang tidak memberikan review.
   - Bisa juga karena kesalahan teknis dalam pencatatan data.

2. **Order Items Tidak Memiliki Missing Value (0%)** ✅
   - Indikasi bahwa proses pencatatan transaksi berjalan dengan baik dan tidak ada gangguan.

3. **Produk Memiliki 7.43% Data Hilang** ⚠️
   - Bisa jadi karena informasi produk belum lengkap saat diunggah ke sistem.
   - Dapat diatasi dengan mengisi data dari produk serupa atau mencari sumber eksternal.

## 🚀 Next Steps
- Visualisasi tren penjualan untuk melihat pola pembelian pelanggan.
- Analisis sentimen dari review pelanggan (jika ada teks komentar).
- Prediksi kategori produk paling laris menggunakan Machine Learning.

---
💡 **Insight yang "Gila":** Jika kita bisa memahami pola missing values dan menghubungkannya dengan perilaku pelanggan, kita bisa **memprediksi kapan pelanggan akan memberikan review negatif sebelum mereka menulisnya**! 🔥

