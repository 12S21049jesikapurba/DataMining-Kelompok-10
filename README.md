# Case 4: 
# DiTenun - Ulos Image Classification 
Classification for the smallest motif images of ulos will be conducted using CNN (Convolutional Neural Networks) algorithms.
Klasifikasi untu gambar motif ulos dengan menggunakan algoritma CNN (Convolutional Neural Networks).

🚀 How to explore the DiTenun-Ulos classification? [Click here](). 

<div align="center">
  <img src="Picture/DiTenun.png" alt="DiTenun Logo" width="800"/>
</div>

## CNN Algorithm
A convolutional neural network is a feed-forward neural network that analyzes visual images by processing data in a grid-like pattern. It’s also known as ConvNet. A convolutional neural network detects and classifies objects in an image.

<div align="center">
 <img src="Picture/CNN overview.png" height="400" width="800"/>
</div>

For more explanation, [click here!](https://insightsimaging.springeropen.com/articles/10.1007/s13244-018-0639-9). 

## Dataset
Ulos Motif Dataset can be accessed <a
    href="Dataset"> <button>here</button></a>.

## 📑 Business Understanding
**DiTenun - Ulos Image Classification**

`Objektif Project `
Ulos adalah kain tradisional suku Batak yang memiliki berbagai motif sesuai dengan makna budayanya. Motif yang beragam dengan variasi dan pola yang rumit sering kali menyebabkan penggolongan ulos yang cukup rumit. Tugas analitik utama adalah klasifikasi motif ulos. Dengan menggunakan algoritma Convolutional Neural Network (CNN), proyek ini bertujuan untuk memprediksi kelas atau kategori ulos berdasarkan gambar motifnya. Dataset gambar ulos berasal dari organisasi DiTenun yang bekerja sama dengan IT Del, yang mengharapkan sistem klasifikasi ini dapat membantu proses identifikasi, pelabelan, dan dokumentasi motif ulos secara otomatis dan efisien.

`Tujuan Project`
Tujuan dari proyek ini adalah mengembangkan algoritma CNN untuk melakukan klasifikasi terhadap motif ulos berdasarkan jenis motifnya. Target utamanya adalah mencapai akurasi ≥90% pada data uji. Model akan dilatih secara terpisah untuk 2 dataset: gambar hitam putih (black) dan gambar berwarna (color), agar setiap model dapat berfokus pada karakteristik data masing-masing.

`Struktur Data`
Dataset terdiri dari gambar ulos dengan label motif tertentu, baik dalam versi hitam putih (black) maupun berwarna (color). Label motif (kelas) pada dataset adalah kategori yang merepresentasikan jenis motif ulos yang akan dikenali.
Setiap gambar memiliki informasi berikut:
- Dimensi gambar (width, height).
- Saluran warna (RGB untuk color dan grayscale untuk black).
- Nama kelas (label) yang mewakili jenis motif ulos, misalnya ulos_ragi, ulos_sadum, dll.

Struktur dataset yang disiapkan adalah dataset untuk motif ulos versi hitam putih dan berwarna (disajikan secara terpisah). Nantinya, setiap data ini akan dibagi lagi untuk pemisahan data training dan data testing. 

Setiap kelas motif  ulos pada dataset memiliki jumlah data sebanyak 64 gambar untuk memastikan model CNN dapat digunakan dengan baik. Jika jumlah data per kelas masih kurang, maka augmentasi data akan dilakukan. 

Sumber dataset disediakan oleh organisasi DiTenun dan dapat diakses <a
    href="Dataset"> <button>disini</button></a>.

`Rencana Pelaksanaan Proyek `
Ruang lingkup (Berdasarkan Work Breakdown Structure) dari proyek ini adalah sebagai berikut:
* Persiapan
  - Pemilihan kasus, yaitu identifikasi masalah klasifikasi motif ulos.
  - Penentuan Algoritma, yaitu memilih algoritma CNN sebagai metode untuk klasifikasi gambar.
    
* Pelaksanaan
  - Business Understanding, yaitu mementukan objektif proyek, tujuan proyek, dan rencana proyek.
  - Data Understanding, yaitu mengumpulkan data, menelaah data, dan memvalidasi data.
  - Data Preparation, yaitu memilah , membersikan, mengkonstruksi, menentukan label, dan mengintegrasikan data.
  - Modeling, yaitu membangun skenario pengujian, dan membangun model.
  - Model Evaluation, yaitu mengevaluasi hasil pemodelan, dan melakukan review proses pemodelan.
  - Deployment, yaitu melakukan deployment model dan membuat laporan akhir proyek.

Timeline yang dibutuhkan untuk melakukan proyek ini adalah sekitar 5 minggu untuk proses pengumpulan dan pelabelan data sampai dengan implementasi (deployment)

## Data Understanding

## Modeling


## Evaluation


## Deployment

### Timeline
See the timeline <a
    href="https://docs.google.com/spreadsheets/d/1VXhPiIWqko85sHdpUdVkVoxPtRhJi3Kr-K-TBdkKMRg/edit?usp=sharing">
    <button>here</button></a>!<br />

<br />

#### 🧞‍♂ Data Mining - Kelompok 10

- 12S21047 | Elshaday Simamora
- 12S21048 | Nessy Pangaribuan
- 12S21049 | Jesika Purba

