import streamlit as st

st.title("Aplikasi Kelulusan")
nilai = st.number_input("Masukkan nilai:")
kehadiran = st.number_input("Masukkan persentase kehadiran:")

def cek_kelulusan(nilai, kehadiran):
    if nilai >= 70 and kehadiran >=75:
        return "LULUS"
    else:
        return "TIDAK LULUS"
    
if st.button("Cek kelulusan"):
    hasil = cek_kelulusan(nilai, kehadiran)
    st.write("Hasil: {}".format(hasil))