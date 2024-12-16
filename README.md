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
  <img src="https://github.com/12S21049jesikapurba/DataMining-Kelompok10_Case4/blob/d5f0018e7b80689a529d1ca84f91a4beeff6e20f/Picture/Data%20Understanding/Keterkaitan%20Antar%20Data%20%5B1%5D.png" alt="dataset description" width="50">
</div>
<div align="center">
  <img src="Picture/Data Understanding/Keterkaitan Antar Data [2].png" alt="dataset description" width="50">
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
<div align="center">
  <img src="Picture/Data Understanding/Relasi_Antar_Atribut_&_Label_[1].png" alt="dataset description" width="100">
</div>
<div align="center">
  <img src="Picture/Data Understanding/Relasi_Antar_Atribut_[2].png" alt="dataset description" width="100">
</div>
<br>

## _Modeling_


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

