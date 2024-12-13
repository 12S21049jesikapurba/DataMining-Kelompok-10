import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Fungsi untuk memuat model CNN
def load_model():
    model = tf.keras.models.load_model('model_ulos.h5')
    return model

# Fungsi untuk melakukan prediksi pada gambar
def predict_image(model, image):
    # Preprocessing gambar agar sesuai dengan input model
    image = image.resize((150, 150))  # Sesuaikan ukuran input dengan model
    image_array = np.array(image) / 255.0  # Normalisasi
    image_array = np.expand_dims(image_array, axis=0)  # Tambahkan batch dimension

    # Prediksi
    prediction = model.predict(image_array)
    return prediction

# Fungsi untuk menampilkan visualisasi confidence level
def plot_confidence(prediction, class_names):
    fig, ax = plt.subplots()
    ax.barh(class_names, prediction[0], color='skyblue')
    ax.set_xlabel('Confidence')
    ax.set_title('Prediction Confidence Level')
    st.pyplot(fig)

# Streamlit App
st.set_page_config(layout="wide")
st.title("Ulos Image Classification")

# Sidebar untuk navigasi
page = st.sidebar.radio("Pilih Fitur", ["Klasifikasi Gambar", "Panduan Pengguna"])

if page == "Klasifikasi Gambar":
    st.markdown(
        """**Tentang Aplikasi:**
        Aplikasi ini menggunakan model Convolutional Neural Network (CNN) untuk mengklasifikasikan jenis kain ulos berdasarkan gambar yang diunggah pengguna. Model ini bertujuan untuk mendukung pelestarian budaya dan meningkatkan pemahaman tentang kain tradisional ulos.
        """
    )

    # Upload file gambar
    gu_image = st.file_uploader("Upload an image of Ulos", type=["jpg", "jpeg", "png"])

    if gu_image is not None:
        # Tampilkan gambar yang diunggah
        image = Image.open(gu_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Muat model dan lakukan prediksi
        st.write("Processing image...")
        try:
            model = load_model()
            prediction = predict_image(model, image)

            # Validasi hasil prediksi
            class_names = ['Pinuncaan', 'Ragi Hidup', 'Ragi Hotang', 'Sadum', 'Sibolang', 'Tumtuman']  # Label kelas
            if len(prediction[0]) == len(class_names):
                predicted_class = class_names[np.argmax(prediction)]
                confidence = np.max(prediction) * 100

                st.write(f"Predicted Class: **{predicted_class}**")
                st.write(f"Confidence: **{confidence:.2f}%**")

                # Tampilkan visualisasi confidence level
                plot_confidence(prediction, class_names)

                # Deskripsi tambahan tentang ulos yang diprediksi
                ulos_descriptions = {
                    "Pinuncaan": """
                    **Desain:** Ulos ini memiliki struktur yang terdiri dari lima bagian yang ditenun secara terpisah dan kemudian disatukan. Motifnya biasanya menggunakan warna-warna cerah dengan pola geometris yang khas.
                    **Kegunaan:**
                    - Acara Resmi: Sering digunakan dalam upacara adat dan acara resmi oleh pemimpin atau raja.
                    - Pernikahan: Dipakai oleh pengantin dan keluarga dalam perayaan pernikahan.
                    - Marpaniaran: Dililitkan sebagai kain oleh keluarga tuan rumah pada waktu pesta besar dalam acara marpaniaran.
                    - Simbol Kehormatan: Melambangkan status dan kehormatan bagi pemakainya dalam konteks sosial.
                    """,
                    "Ragi Hidup": """
                    **Desain:** Ulos Ragi Hidup umumnya berbentuk panjang dan lebar, dengan pola yang sederhana namun elegan. Motifnya sering kali mencerminkan kehidupan sehari-hari masyarakat Batak.
                    **Kegunaan:**
                    - Pakaian Sehari-hari: Digunakan sebagai baju atau sarung, memberikan kenyamanan bagi pemakainya.
                    - Simbol Kehidupan: Melambangkan kehidupan dan keberlangsungan, sering dipakai dalam acara-acara penting.
                    """,
                    "Ragi Hotang": """
                    **Desain:** Ulos Ragi Hotang Memiliki pola yang lebih rumit dan berwarna gelap, sering kali dihiasi dengan motif tradisional Batak.
                    **Kegunaan:**
                    - Selimut: Digunakan sebagai selimut untuk memberikan kehangatan, terutama pada malam hari atau saat cuaca dingin.
                    - Simbol Status: Memiliki nilai simbolis, sering kali digunakan oleh keluarga kaya dalam acara tertentu.
                    """,
                    "Sadum": """
                    **Desain:** Ulos Sadum memiliki bingkai bergaris gelap di kedua sisinya, dengan warna-warna ceria di tengahnya. Pola yang digunakan biasanya cukup beragam, mencerminkan suasana bahagia.
                    **Kegunaan:**
                    - Acara Bahagia: Dipakai dalam acara-acara sukacita seperti pesta, ulang tahun, atau perayaan lainnya.
                    - Kenang-Kenangan: Sering dijadikan sebagai hadiah atau kenang-kenangan untuk orang terkasih.
                    """,
                    "Sibolang": """
                    **Desain:** Ulos Sibolang memiliki warna dominan hitam dan putih dengan pola bergaris sederhana, sering dipakai pada acara penghormatan.
                    **Kegunaan:**
                    - Acara Duka Cita: Dipakai oleh keluarga yang berduka dalam upacara pemakaman, melambangkan kedekatan dan penghormatan kepada yang telah meninggal.
                    - Simbol Kesedihan: Menjadi tanda kesedihan dan dukacita bagi keluarga yang ditinggalkan.
                    """,
                    "Tumtuman": """
                    **Desain:** Ulos Tumtuman memiliki pola geometris unik, melambangkan harapan untuk masa depan yang cerah. Ulos ini memiliki motif tali-tali yang khas, memberikan kesan kuat dan terikat.
                    **Kegunaan:**
                    - Digunakan pada acara yang melibatkan harapan akan masa depan yang sukses dan bahagia.
                    - Ikatan Keluarga: Dipakai oleh anak pertama dalam keluarga, simbol dari status dan tanggung jawab.
                    - Acara Tradisional: Digunakan dalam berbagai upacara adat untuk menunjukkan posisi dalam struktur keluarga.
                    """
                }
                
                st.markdown(f"""**Tentang {predicted_class}:**\n{ulos_descriptions.get(predicted_class, 'Deskripsi untuk jenis ulos ini belum tersedia.')}""")
            else:
                st.error("Model output dimensions do not match the number of class names. Please check the model and class labels.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif page == "Panduan Pengguna":
    st.header("Panduan Pengguna")
    st.markdown(
        """ 
        1. **Unggah Gambar:** Klik tombol "Browse Files" untuk mengunggah gambar ulos dalam format JPG, JPEG, atau PNG.<br>
        2. **Validasi Gambar:** Pastikan gambar yang diunggah memiliki kualitas baik dan menampilkan kain ulos dengan jelas.<br>
        3. **Hasil Prediksi:** Tunggu beberapa saat untuk melihat hasil klasifikasi dan tingkat kepercayaan model.<br>
        4. **Informasi Tambahan:** Bacalah deskripsi singkat tentang jenis ulos yang terdeteksi untuk memperkaya pengetahuan.
        """,
        unsafe_allow_html=True
    )
    
    st.header("Informasi Tambahan tentang Kain Ulos")
    st.markdown(
        """
        - **Makna Simbolis:** Kain ulos bukan hanya sekadar kain, tetapi juga memiliki nilai filosofis yang mendalam. Setiap jenis ulos memiliki makna yang melambangkan status sosial, hubungan keluarga, atau doa untuk kebahagiaan.
        - **Proses Pembuatan:** Kain ulos dibuat menggunakan alat tenun tradisional dengan teknik yang diwariskan secara turun-temurun. Proses ini mencerminkan ketekunan dan keahlian tinggi dari para pengrajin.
        - **Penggunaan Modern:** Saat ini, ulos tidak hanya digunakan dalam upacara adat tetapi juga sebagai inspirasi dalam desain busana modern, seperti pakaian, tas, dan aksesori.
        - **Pelestarian Budaya:** Penggunaan ulos dalam kehidupan sehari-hari dan pengenalan kepada generasi muda menjadi bagian penting dari upaya melestarikan warisan budaya Batak.
        """,
        unsafe_allow_html=True
    )

st.write("\n\n")
st.write("Developed by Kelompok 3 - Data Mining")
