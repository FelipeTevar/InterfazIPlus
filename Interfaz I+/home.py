import streamlit as st

st.title("Pantalla Inicial")

if st.button("Ir a Albarán"):
    st.switch_page("pages/Albaran.py")

if st.button("Ir a Factura"):
    st.switch_page("pages/Factura.py")

