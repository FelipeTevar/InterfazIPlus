import streamlit as st

st.title("Pantalla Inicial")

# Botones para navegar
if st.button("Ir a Albarán"):
    st.session_state.pantalla = "albaran"
if st.button("Ir a Factura"):
    st.session_state.pantalla = "factura"



if st.session_state.get("pantalla") == "albaran":
    st.title("Pantalla Albarán")

    st.text("Instrucción:")
    archivo = st.file_uploader("Adjuntar Archivo")
    if archivo:
        st.success("Archivo adjuntado correctamente.")

    st.text("Datos/Info de los Adjuntos:")
    st.text_area("Información adicional")



if st.session_state.get("pantalla") == "factura":
    st.title("Pantalla Factura")

    st.text("Contenido:")
    st.text("Info datos documentos")

    st.write("¿Quiere modificar línea de pedido?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sí"):
            st.info("Modificando línea de pedido...")
    with col2:
        if st.button("No"):
            st.warning("No se modificará la línea.")

