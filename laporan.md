# Laporan Eksperimen Klasifikasi Chest X-Ray menggunakan MobileNetV2

Disusun oleh:  
Danendra Henry  
122430130

## Latar Belakang
Eksperimen ini dilakukan untuk meningkatkan performa klasifikasi citra Chest X-Ray dengan mengganti arsitektur model dari ResNet/SimpleCNN ke MobileNetV2. Tujuan utama adalah mencapai akurasi target 88% dengan mengoptimalkan arsitektur yang lebih ringan dan efisien.

## Perubahan Arsitektur Model
Perubahan utama yang dilakukan adalah penggantian arsitektur model dari ResNet/SimpleCNN ke MobileNetV2. MobileNetV2 dipilih karena beberapa keunggulan:

1. Efisiensi Komputasi
   - Arsitektur yang lebih ringan
   - Jumlah parameter yang lebih sedikit
   - Waktu pelatihan yang lebih cepat

2. Performa yang Optimal
   - Desain arsitektur modern
   - Penggunaan inverted residual blocks
   - Depth-wise separable convolutions

3. Kemampuan Transfer Learning
   - Memanfaatkan pre-trained weights
   - Adaptasi yang baik untuk dataset medis
   - Feature extraction yang optimal

## Modifikasi Hyperparameter
Untuk mencapai target akurasi 88%, beberapa penyesuaian hyperparameter dilakukan:

1. Learning Rate
   - Penurunan learning rate dari 0.0003 ke 0.0001
   - Membantu konvergensi yang lebih stabil
   - Mengurangi resiko overfitting

2. Batch Size
   - Peningkatan batch size dari 16 ke 32
   - Meningkatkan stabilitas training
   - Mempersingkat waktu pelatihan

3. Jumlah Epoch
   - Penambahan epoch dari 16 ke 30
   - Memberikan waktu yang cukup untuk konvergensi
   - Memungkinkan pembelajaran fitur yang lebih dalam

## Adaptasi Input dan Output Layer
Beberapa penyesuaian teknis dilakukan untuk mengakomodasi karakteristik dataset:

1. Input Layer
   - Modifikasi untuk menerima gambar grayscale (1 channel)
   - Penyesuaian normalisasi input
   - Optimasi preprocessing

2. Output Layer
   - Konfigurasi untuk klasifikasi biner
   - Penyesuaian fungsi aktivasi
   - Optimasi loss function

## Hasil dan Performa
Perubahan arsitektur dan optimasi yang dilakukan memberikan beberapa dampak:

1. Peningkatan Akurasi
   - Target akurasi 88% dapat dicapai
   - Stabilitas prediksi yang lebih baik
   - Performa yang konsisten pada data validasi

2. Efisiensi Komputasi
   - Waktu training yang lebih singkat
   - Penggunaan memori yang lebih efisien
   - Inference time yang lebih cepat

3. Generalisasi Model
   - Performa yang baik pada data baru
   - Pengurangan overfitting
   - Robustness yang lebih baik

## Kesimpulan
Implementasi MobileNetV2 dengan optimasi parameter yang dilakukan berhasil mencapai target performa yang diinginkan. Model menunjukkan keseimbangan yang baik antara akurasi dan efisiensi komputasi, menjadikannya pilihan yang tepat untuk aplikasi klasifikasi citra medis.

## Rekomendasi
Beberapa saran untuk pengembangan lebih lanjut:

1. Implementasi teknik augmentasi data yang lebih advance
2. Eksplorasi teknik regularisasi tambahan
3. Pengujian pada dataset eksternal untuk validasi lebih lanjut
4. Implementasi mekanisme interpretability untuk analisis prediksi
5. Optimasi lebih lanjut untuk deployment di lingkungan produksi