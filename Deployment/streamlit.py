import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Fungsi untuk memuat model CNN
def load_model():
    model = tf.keras.models.load_model('Deployment/model_ulos.h5')
    return model

# Fungsi untuk melakukan prediksi pada gambar
def predict_image(model, image):
    image = image.resize((150, 150))  # Sesuaikan ukuran input dengan model
    image_array = np.array(image) / 255.0  # Normalisasi
    image_array = np.expand_dims(image_array, axis=0)  # Tambahkan batch dimension

    prediction = model.predict(image_array)
    return prediction

# Fungsi untuk validasi apakah gambar termasuk dataset
def is_valid_image(prediction, threshold=0.6):
    return np.max(prediction) > threshold

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

page = st.sidebar.radio("Pilih Fitur", ["Klasifikasi Gambar", "Panduan Pengguna"])

if page == "Klasifikasi Gambar":
    st.markdown(
        """
        **Tentang Aplikasi:**
        Aplikasi ini menggunakan model **Convolutional Neural Network (CNN)** untuk mengklasifikasikan jenis kain **Ulos** berdasarkan gambar yang diunggah pengguna.
        """
    )

    gu_image = st.file_uploader("Upload an image of Ulos", type=["jpg", "jpeg", "png"])

    if gu_image is not None:
        image = Image.open(gu_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        st.write("Processing image...")
        try:
            model = load_model()
            prediction = predict_image(model, image)

            class_names = ['Pinuncaan', 'Ragi Hidup', 'Ragi Hotang', 'Sadum', 'Sibolang', 'Tumtuman']
            
            if len(prediction[0]) == len(class_names):
                if is_valid_image(prediction):
                    predicted_class = class_names[np.argmax(prediction)]
                    confidence = np.max(prediction) * 100

                    st.write(f"**Predicted Class:** {predicted_class}")
                    st.write(f"**Confidence:** {confidence:.2f}%")
                    plot_confidence(prediction, class_names)
                else:
                    st.warning("Gambar tidak dikenali sebagai bagian dari dataset. Harap unggah gambar yang sesuai dengan dataset ulos.")
            else:
                st.error("Model output dimensions do not match the number of class names. Please check the model and class labels.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

elif page == "Panduan Pengguna":
    st.header("Panduan Pengguna")
    st.markdown(
        """ 
        ### Cara Menggunakan Aplikasi
        1. **Unggah Gambar:** Klik tombol "Browse Files" untuk mengunggah gambar ulos dalam format JPG, JPEG, atau PNG.<br>
        2. **Validasi Gambar:** Pastikan gambar yang diunggah memiliki kualitas baik dan menampilkan kain ulos dengan jelas.<br>
        3. **Hasil Prediksi:** Tunggu beberapa saat untuk melihat hasil klasifikasi dan tingkat kepercayaan model.<br>
        4. **Informasi Tambahan:** Bacalah deskripsi singkat tentang jenis ulos yang terdeteksi untuk memperkaya pengetahuan.
        """,
        unsafe_allow_html=True
    )

st.write("\n\n")
st.write("Developed by Kelompok 3 - Data Mining")
