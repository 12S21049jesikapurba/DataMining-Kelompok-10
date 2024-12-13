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
- Mengumpulkan data:
  Data dikumpulkan dari [Kaggle](https://www.kaggle.com/datasets/fthnaja/kain-ulos) yang berisi berbagai motif ulos.
  Struktur datasetnya adalah sebagari berikut:
  ## Ragi Hidup
+------------+--------------+-------------+
|  Category  |  File Name   | File Format |
+------------+--------------+-------------+
| Ragi Hidup | IMG_5125.PNG |     PNG     |
| Ragi Hidup | IMG_5158.PNG |     PNG     |
+------------+--------------+-------------+

## Sadum
+----------+----------------------------+-------------+
| Category |         File Name          | File Format |
+----------+----------------------------+-------------+
|  Sadum   | IMG_20240705_231559_5.jpg  |     jpg     |
|  Sadum   | IMG_20240705_231559_36.jpg |     jpg     |
+----------+----------------------------+-------------+

## Sibolang
+----------+--------------------------------------------------------+-------------+
| Category |                       File Name                        | File Format |
+----------+--------------------------------------------------------+-------------+
| Sibolang | WhatsApp Image 2024-07-05 at 23.49.23 (15) - Copy.jpeg |    jpeg     |
| Sibolang |                     1000104052.jpg                     |     jpg     |
+----------+--------------------------------------------------------+-------------+

## Ragi Hotang
+-------------+---------------------------+-------------+
|  Category   |         File Name         | File Format |
+-------------+---------------------------+-------------+
| Ragi Hotang |  IMG_20240705_231428.jpg  |     jpg     |
| Ragi Hotang | IMG_20240611_211520_1.jpg |     jpg     |
+-------------+---------------------------+-------------+

## Pinuncaan
+-----------+--------------------------+-------------+
| Category  |        File Name         | File Format |
+-----------+--------------------------+-------------+
| Pinuncaan | IMG_20240611_2011255.jpg |     jpg     |
| Pinuncaan |       IMG_5327.PNG       |     PNG     |
+-----------+--------------------------+-------------+

## Tumtuman
+----------+-------------------------------------------------+-------------+
| Category |                    File Name                    | File Format |
+----------+-------------------------------------------------+-------------+
| Tumtuman | WhatsApp Image 2024-07-06 at 00.02.57 (18).jpeg |    jpeg     |
| Tumtuman |              ulos (16) - Copy.jpeg              |    jpeg     |
+----------+-------------------------------------------------+-------------+
 
  Jumlah data yang terdapat pada dataset adalah:
  +-------------+-------------+
|  Category   | Image Count |
+-------------+-------------+
| Ragi Hidup  |     205     |
|    Sadum    |     204     |
|  Sibolang   |     206     |
| Ragi Hotang |     209     |
|  Pinuncaan  |     201     |
|  Tumtuman   |     206     |
+-------------+-------------+

Jumlah total gambar dalam dataset: 1231

  ```
  
  ```

- Menelaah Data


- Memvalidasi Data

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

