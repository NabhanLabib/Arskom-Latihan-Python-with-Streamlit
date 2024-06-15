import streamlit as st

def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

st.markdown(":blue-background[Nama : Nabhan Labib]")
st.markdown(":blue-background[Kelas : TI.23.C.7]")
st.markdown(":blue-background[NIM : 312310783]")
st.title('Kalkulator BMI')
st.write("Hitung Indeks Massa Tubuh (BMI) Anda")

#Input berat badan dalam kilogram
berat = st.number_input('Masukkan berat badan anda (kg)', value=0.0)
#Input tinggi badan dalam meter
tinggi = st.number_input('Masukkan tinggi badan anda (m)', value=0.0)
if berat > 0 and tinggi > 0:
    #Hitung BMI
    bmi = hitung_bmi(berat, tinggi)
    #Tampilkan hasil
    st.write(f'BMI Anda adalah {bmi:.2f}')
    #Interpretasi hasil BMI
    if bmi < 18.5 :
        st.write("Anda kekurangan berat badan.")
    elif 18.5 <= bmi < 24.9:
        st.write("Berat badan Anda normal.")
    elif 25 <= bmi < 29.9:
        st.write("Anda kelebihan berat badan.")
    else:
        st.write("Anda mengalami obesitas.")
else:
    st.write("Silahkan masukkan berat dan tinggi badan yang valid.")
