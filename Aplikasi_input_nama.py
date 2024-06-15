import streamlit as st
st.title("Aplikasi Input Nama")
st.subheader("Masukkan Nama Anda")

nama= st.text_input("Nama:")

if nama:
    st.write("Halo,", nama, "!")