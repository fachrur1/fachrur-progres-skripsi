import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi halaman Streamlit agar memenuhi layar (wide)
st.set_page_config(
    page_title="Dashboard Skripsi Kulon Progo",
    page_icon="🎓",
    layout="wide"
)

# 2. Menyembunyikan elemen bawaan Streamlit (header/footer/menu) agar terlihat seperti web asli
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding: 0rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Membaca dan merender file HTML
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
    
    # Menampilkan HTML di dalam iframe Streamlit
    # Height diatur cukup tinggi agar menampung seluruh konten dan scrollbar berfungsi
    components.html(html_data, height=1800, scrolling=True)
except FileNotFoundError:
    st.error("File index.html tidak ditemukan. Pastikan file tersebut berada di folder yang sama dengan app.py.")
