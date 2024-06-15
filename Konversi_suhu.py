import streamlit as st

st.title("Konversi Suhu dari Celsius ke Fahrenheit")

suhu_celsius = st.number_input("Masukkan suhu dalam Celsius")

suhu_fahrenheit = (suhu_celsius *9/5) + 32

st.write("Suhu dalam fahrenheit:", suhu_fahrenheit, "°F")