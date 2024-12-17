import numpy as np
import streamlit as st
import cohere as cohere
from dotenv import load_dotenv
import os

# Configuración inicial
load_dotenv()
co = cohere.Client(os.environ['COHERE_API_KEY'])

# Configuración de la página
st.set_page_config(
    page_title="Hazle preguntas a Cohere!",
    page_icon=":rocket:",
    layout="wide",
)
# Encabezados 
st.markdown("<h1 style='text-align: center;'>🤖 Hazle preguntas a Cohere</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Sube un archivo de texto, escribe una pregunta y obtén respuestas inteligentes.</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col2:
    st.image("data.jpg", width=600)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<ol>
    <li>Sube tu archivo de texto (.txt)</li>
    <li>Escribe tu pregunta en el campo de texto</li>
    <li>Haz clic en 'Analizar' para obtener una respuesta</li>
</ol>
""", unsafe_allow_html=True)

# Cargar texto desde archivo subido
texto_subido = st.file_uploader("Sube aquí tu archivo .txt", type="txt", help="Asegúrate de subir un archivo de texto sin formato (.txt).")

if texto_subido is not None:
    texto = texto_subido.getvalue().decode("utf-8")
    st.success("Archivo cargado exitosamente. ¡Puedes hacer tu pregunta ahora!")

    # Función para dividir el texto en chunks
    def dividir_texto(texto, tamaño):
        return [texto[i:i+tamaño] for i in range(0, len(texto), tamaño)]

    chunks = dividir_texto(texto, 500)
    
    # Función para calcular similitud
    def calculate_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    # Input del usuario
    user_input = st.text_input("Ingresa tu pregunta aquí:")
    if st.button("Analizar"):
        if user_input:
            # Procesar embeddings
            model = "embed-spanish-v3.0"
            input_type = "search_query"

    # Embeddings de los chunks
    res = co.embed(texts=chunks, model=model, input_type=input_type, embedding_types=['float'])
    cosas = res.embeddings.float


    # Input del usuario
    user_input = st.text_input("Cuál es tu pregunta:")

    if st.button("Analizar"):
        if user_input:
            # Embedding de la pregunta del usuario
            impus = co.embed(texts=[user_input], model=model, input_type=input_type, embedding_types=['float'])
            pregunta = impus.embeddings.float[0]

            # Calcular similitudes
            parecidos = [calculate_similarity(pregunta, cosa) for cosa in cosas]
            mas_parecido = max(parecidos)
            index_mas_parecido = np.argmax(parecidos)

            # Generar respuesta usando Cohere
            response = co.generate(
                model="command-r-plus",
                prompt=f"Basado en el siguiente texto: '{chunks[index_mas_parecido]}', responde a la pregunta: {user_input}",
                max_tokens=150,
                temperature=0.7,
            )
            generated_text = response.generations[0].text.strip()

            st.write("**Respuesta del Asistente:**")
            st.write(generated_text)

            st.subheader("Respuesta del Asistente:")
            st.markdown(f"<div style='padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;'>{generated_text}</div>", unsafe_allow_html=True)
        else:
            st.warning("Por favor, ingresa una pregunta válida.")
else:
    st.warning("Sube tu texto y haz preguntas!")


# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Aplicación desarrollada con ❤️ usando Streamlit y Cohere API.</p>", unsafe_allow_html=True)