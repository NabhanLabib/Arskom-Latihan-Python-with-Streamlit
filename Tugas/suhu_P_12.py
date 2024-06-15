import streamlit as st
st.markdown(":blue-background[Nama : Nabhan Labib]")
st.markdown(":blue-background[Kelas : TI.23.C.7]")
st.markdown(":blue-background[NIM : 312310783]")

def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32
st.title('Temperatur Converter')
st.write("Convert temperature from Celsius to Fahrenheit")

#Input temperature in Celsius
celsius = st.number_input('Enter temperature in Celsius', value=0.0)
#Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)
#Display the result
st.write(f'{celsius}°C = {fahrenheit:.2f}°F')