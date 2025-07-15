import streamlit as st

st.title("Pantalla Inicial")

# Botones para navegar
if st.button("Ir a Albarán"):
    st.session_state.pantalla = "albaran"
if st.button("Ir a Factura"):
    st.session_state.pantalla = "factura"
