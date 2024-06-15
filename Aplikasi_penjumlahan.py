import streamlit as st

st.title("Aplikasi Penjumlahan")

angka1 = st.number_input("Masukkan angka pertama")
angka2 = st.number_input("Masukkan angka kedua")

if st.button("Jumlahkan"):
    hasil = angka1 + angka2
    st.write("Hasil penjumlahan:", hasil)