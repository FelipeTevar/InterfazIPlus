import streamlit as st  # Importa la biblioteca Streamlit para crear interfaces web interactivas

# Título principal de la aplicación
st.title("Pantalla Inicial")

# Botones para navegar a otras pantallas
if st.button("Ir a Albarán"):
    st.session_state.pantalla = "albaran"  # Guarda en la sesión que se ha seleccionado la pantalla de Albarán
if st.button("Ir a Factura"):
    st.session_state.pantalla = "factura"  # Guarda en la sesión que se ha seleccionado la pantalla de Factura

# Si el usuario ha seleccionado la pantalla de Albarán
if st.session_state.get("pantalla") == "albaran":
    st.title("Pantalla Albarán")  # Título de la pantalla

    st.text("Instrucción:")  # Texto de instrucción
    archivo = st.file_uploader("Adjuntar Archivo")  # Componente para subir archivos
    if archivo:
        st.success("Archivo adjuntado correctamente.")  # Mensaje de éxito si se sube un archivo

    st.text("Datos/Info de los Adjuntos:")  # Texto informativo
    st.text_area("Información adicional")  # Área de texto para escribir información

# Si el usuario ha seleccionado la pantalla de Factura
if st.session_state.get("pantalla") == "factura":
    st.title("Pantalla Factura")  # Título de la pantalla

    st.text("Contenido:")  # Texto de contenido
    st.text("Info datos documentos")  # Información adicional

    # Pregunta al usuario si quiere modificar una línea de pedido
    st.write("¿Quiere modificar línea de pedido?")
    col1, col2 = st.columns(2)  # Divide la pantalla en dos columnas
    with col1:
        if st.button("Sí"):
            st.info("Modificando línea de pedido...")  # Mensaje si elige "Sí"
    with col2:
        if st.button("No"):
            st.warning("No se modificará la línea.")  # Mensaje si elige "No"

