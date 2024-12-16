# Case 4: 
# DiTenun - Ulos _Image Classification_ 
Klasifikasi untuk gambar motif ulos dengan menggunakan algoritma CNN (Convolutional Neural Networks).

<div align="center">
  <img src="Picture/DiTenun.png" alt="DiTenun Logo" width="800"/>
</div>

## 📑 _Business Understanding_
**DiTenun - Ulos _Image Classification_**

`Based on Data `<br>
Ulos adalah kain tradisional suku Batak yang memiliki berbagai motif sesuai dengan makna budayanya. Motif yang beragam dengan variasi dan pola yang rumit sering kali menyebabkan penggolongan ulos yang cukup rumit. Tugas analitik utama adalah klasifikasi motif ulos. Dengan menggunakan algoritma Convolutional Neural Network (CNN), proyek ini bertujuan untuk memprediksi kelas atau kategori ulos berdasarkan gambar motifnya. 

Data yang diperlukan adalah gambar ulos yang memiliki deskripsi tentang jenis ulosnya (misalnya: Ulos Ragidup, Ulos Sibolang, Ulos Sadum, dan lain-lain). Dataset dapat diakses dari [Kaggle](https://www.kaggle.com/datasets/fthnaja/kain-ulos). Dataset berisi 1.231 gambar motif ulos dengan 6 label yang menunjukkan jenis motif ulos (Pinuncaan, Ragi Hidup, Ragi Hotang, Sadum, Sibolang, Tumtuman). Dataset ini merupakan dataset _via public data_. Data sudah dibagi untuk _train_ dan _test data_.  

`Rencana Pelaksanaan Proyek ` <br>
Ruang lingkup (Berdasarkan Work Breakdown Structure) dari proyek ini adalah sebagai berikut:
* Persiapan
  - Pemilihan kasus, yaitu identifikasi masalah klasifikasi motif ulos.
  - Penentuan Algoritma, yaitu memilih algoritma CNN sebagai metode untuk klasifikasi gambar.
    
* Pelaksanaan
  - _Business Understanding_, yaitu mementukan objektif proyek, tujuan proyek, dan rencana proyek.
  - _Data Understanding_, yaitu mengumpulkan data, menelaah data, dan memvalidasi data.
  - _Data Preparation_, yaitu memilah , membersikan, mengkonstruksi, menentukan label, dan mengintegrasikan data.
  - _Modeling_, yaitu membangun skenario pengujian, dan membangun model.
  - _Model Evaluation_, yaitu mengevaluasi hasil pemodelan, dan melakukan review proses pemodelan.
  - _Deployment_, yaitu melakukan deployment model dan membuat laporan akhir proyek.

_Timeline_ yang dibutuhkan untuk melakukan proyek ini adalah sekitar 5 minggu untuk proses pengumpulan dan pelabelan data sampai dengan implementasi (_deployment_).

## _Data Understanding_
- Mengumpulkan data<br>
  Data dikumpulkan dari [Kaggle](https://www.kaggle.com/datasets/fthnaja/kain-ulos) yang berisi berbagai motif ulos.<br>
  Struktur dari dataset disajikan 2 per kelas motif ulos, dan dapat dilihat pada gambar dibawah ini. 
  <p align="center">
  <img src="Picture/Data Understanding/Deskripsi Data.png" alt="dataset description" width="200">
</p>
  <br>
  Jumlah gambar yang terdapat pada dataset adalah 1.231 gambar dan jumlah untuk masing-masing kelas dapat dilihat pada gambar dibawah ini.
<p align="center">
  <img src="Picture/Data Understanding/Mengumpulkan Data.png" alt="dataset description" width="200"><br>
  <br>
  
- Menelaah Data
  Proses analisis data dilakukan secara eksploratif (_Exploratory Data Analysis_).<br>
  Karakteristik atribut yang diperoleh adalah sebagai berikut:
<p align="center">
  <img src="Picture/Data Understanding/Karakteristik Atribut.png" alt="dataset description" width="200">
   <br>
 
  Keterkaitan antar data dianalisisi dengan menggunakan metode Anova, Kendall's Tau Test, dan Chi-Square Test. 
  Berikut adalah hasilnya:
  ```
  ANOVA Test Results:
  F-statistic: 173.15445738956262, p-value: 1.9097527024196994e-139
  Ada perbedaan signifikan dalam ukuran file antar kategori.
  
  Kendall's Tau Test Results:
  Tau: -0.04412125023041999, p-value: 0.031794602025439316
  Ada asosiasi signifikan antara ukuran file dan kategori.
  
  Chi-Squared Test Results:
  Chi-Squared: 1575.0099207161215, p-value: 0.0
  Ada asosiasi signifikan antara kategori dan format file.
  
  Mutual Information between 'Category' and 'File Size (bytes)': 2.8846400016536338
  ```
<br>
<div align="center">
  <img src="https://github.com/12S21049jesikapurba/DataMining-Kelompok10_Case4/blob/d5f0018e7b80689a529d1ca84f91a4beeff6e20f/Picture/Data%20Understanding/Keterkaitan%20Antar%20Data%20%5B1%5D.png" alt="dataset description" width="300">
</div>
<div align="center">
  <img src="https://github.com/12S21049jesikapurba/DataMining-Kelompok10_Case4/blob/f3e49b6509cadf19ff3a9903163538cf7e46d38f/Picture/Data%20Understanding/Keterkaitan%20Antar%20Data%20%5B2%5D.png" alt="dataset description" width="300">
</div>
<br>
- Memvalidasi Data
  Validasi data dilakukan untuk menilai kesesuaian kualitas data. Berikut hasil validasi data yang didapatkan.

  ```
  Untuk ukuran data dari 1.231 gambar motif ulos,  1.044 valid dan 187 invalid karena ukuran terlalu besar (>5 MB).
  File invalid perlu dikompresi untuk memenuhi batas ukuran yang diizinkan.
  ```
  ```
  Statistik data menunjukkan bahwa dataset memiliki distribusi kategori yang seimbang, didominasi dengan format jpg.
  Ukuran file bervariasi antara 8 KB hingga 7,25 MB. Beberapa file besar perlu diproses ulang untuk konsistensi.
  ```
   <br>
   
  Relasi antar atribut menunjukkan Cross-Tabulation antara kategori dan format file sebagai berikut:
  ```
  Cross-Tabulation antara Kategori dan Format File:
  File Format  JPG  PNG  jpeg  jpg
  Category                        
  Pinuncaan     10  129     0   62
  Ragi Hidup     0  177     0   28
  Ragi Hotang    0    0     0  209
  Sadum          0    0     0  204
  Sibolang       0    0    50  156
  Tumtuman       0    0   162   44
  ```
<br>
<div align="center">
  <img src="https://github.com/12S21049jesikapurba/DataMining-Kelompok10_Case4/blob/f3e49b6509cadf19ff3a9903163538cf7e46d38f/Picture/Data%20Understanding/Relasi%20Antar%20Atribut%20%26%20Label%20%5B1%5D.png" alt="dataset description" width="150">
</div>
<div align="center">
  <img src="https://github.com/12S21049jesikapurba/DataMining-Kelompok10_Case4/blob/f3e49b6509cadf19ff3a9903163538cf7e46d38f/Picture/Data%20Understanding/Relasi%20Antar%20Atribut%20%5B2%5D.png" alt="dataset description" width="150">
</div>
<br>

## _Data Preparation_
- Memilih dan Memilah Data<br>
```
Pada langkah ini, data yang tersedia dipilih dan dipilah berdasarkan kategori atau label yang akan digunakan.
Proses ini akan memproses rekord data dan atribut data yang terpakai.
Dataset yang digunakan pada proses ini sudah terdiri dari folder ”Train” dan ”Test yang berisi gambar sudah dikelompokkan kedalam kategori-kategori ulos tertentu.
```
<br>

- Membersihkan Data <br>
```
Pada tahap ini, dilakukan pembersihan terhadap data gambar.
Proses ini dilakukan untuk meminimalkan noise (tidak lengkap atau salah) pada data.
Hasil akhirnya adalah data gambar yang telah terorganisasi, ternormalisasi, dan siap digunakan untuk melatih model.
```
<br>

- Mengkonstruksi Data<br>
```
Setelah data dibersihkan, dilakukan konstruksi dataset yaitu menambahkan feature engineering dan melakukan transformasi
terhadap data (standardisasi dan normalisasi). Dataset yang sudah dikonstruksi kemudian akan digunakan untuk dibagi
menjadi menjadi set pelatihan dan pengujian. Hasilnya adalah generator data training dan validasi yang siap digunakan untuk melatih model. 
```

- Integrasi Data<br>
```
Pada tahap ini, akan dilakukan penggabungan terhadap data pelatihan dan pengujian yang telah dipisahkan sebelumnya.
Terdapat proses pemanfaatan augmentasi data untuk menambah variasi dalam dataset pelatihan, yang dapat membantu model untuk generalisasi lebih baik.
Teknik augmentasi yang umum digunakan adalah rotasi, pemotongan, dan flipping gambar secara acak. 
```

## _Modeling_
- Membangun Model CNN<br>
```
Pembangunan model CNN dilakukan dengan pemrosesan data latih menggunakan ImageDataGenerator dengan augmentasi seperti rotasi, pergeseran, zoom,
dan flipping untuk meningkatkan variasi data. Algoritma CNN terdiri dari empat lapisan konvolusi dengan kernel 3x3, masing-masing diikuti oleh
pooling layer untuk mengurangi dimensi data. Setelah itu, data diratakan menggunakan lapisan Flatten dan diteruskan ke Fully Connected layer dengan 512 unit dan aktivasi ReLU. Dropout dengan rasio 0.5 ditambahkan untuk mengurangi risiko overfitting. Output layer menggunakan aktivasi softmax untuk menangani
klasifikasi multi-kelas sesuai jumlah kategori dalam data. Hasil akhirnya adalah arsitektur model siap digunakan.
```
<br>

- Melatih Model CNN<br>
```
Kompilasi model dilakukan menggunakan optimizer Adam, fungsi loss categorical_crossentropy untuk menangani klasifikasi multi-kelas, dan metrik evaluasi accuracy.
Model kemudian dilatih selama 30 epoch menggunakan data augmentasi yang dihasilkan oleh train_generator, dengan jumlah langkah per epoch ditentukan oleh jumlah sampel dibagi ukuran batch.
Setelah pelatihan selesai, model disimpan dalam file model_ulos.h5, memungkinkan pengguna untuk memuat dan menggunakan model di kemudian hari tanpa perlu melatih ulang. Hasil akhirnya adalah model terlatih yang dapat mengklasifikasikan gambar kain Ulos ke dalam kategori yang sesuai berdasarkan pola visual.
```
<br>

- Menguji Model CNN<br>
```
Tahap terakhir dari modeling adalah menguji model untuk mengukur performansi dari model yang digunakan.
```
```
Proses pemuatan data uji diatas dilakukan dengan menggunakan ImageDataGenerator untuk preprocessing data uji. Selanjutnya, digunakan test_generator untuk memuat gambar dari direktori data uji, dan mengubah ukuran gambar. Terakhir, dilakukan pengecekan urutan data dengan menggunakan shuffle=false.
```
```
Proses prediksi pada data uji diatas dilakukan untuk menghasilkan probabilitas untuk setiap kelas. Kelas akan didapatkan dengan probabilitas tertinggi sebagai prediksi, dan kemudian dilakukan penyimpanan label sebenarnya dari data uji untuk nantinya digunakan sebagai pembanding hasil prediksi.
```
```
Kode diatas menghasilkan matrix yang menunjukkan perbandingan antara hasil prediksi model dengan label sebenarnya, yang nantinya akan digunakan untuk membantu mengevaluasi kinerja model. Visualisasi ditampilkan dengan menggunakan seaborn.heatmap untuk melihat distribusi prediksi di tiap kelas. 
```
<br>
Berikut visualisasi Confusion Matrix dan Grafik Heatmap yang disajikan.
<br>
<div align="center">
  <img src="https://github.com/12S21049jesikapurba/DataMining-Kelompok10_Case4/blob/e43609b4893d36d47be0c23263da88f50d86e965/Picture/Modeling/Conf%20Matrix.png" alt="dataset description" width="150">
</div>
<div align="center">
  <img src="https://github.com/12S21049jesikapurba/DataMining-Kelompok10_Case4/blob/e43609b4893d36d47be0c23263da88f50d86e965/Picture/Modeling/TP%2C%20TN%2C%20FP%2C%20FN.png" alt="dataset description" width="150">
</div>
<br>


## _Evaluation_


## _Deployment_

### _Timeline_
_See the timeline_ <a
    href="https://docs.google.com/spreadsheets/d/1VXhPiIWqko85sHdpUdVkVoxPtRhJi3Kr-K-TBdkKMRg/edit?usp=sharing">
    <button>_here_</button></a>!<br />

<br />

#### 🧞‍♂ Data Mining - Kelompok 10

- 12S21047 | Elshaday Simamora
- 12S21048 | Nessy Pangaribuan
- 12S21049 | Jesika Purba

