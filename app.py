import streamlit as st
from transformers import pipeline

# Configuración de la página
st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="🤖",
    layout="centered"
)

# Título y descripción
st.title("🤖 SmartText Assistant")
st.write(
    "SmartText Assistant es una aplicación web con Inteligencia Artificial "
    "que genera textos claros y profesionales a partir de una idea base."
)

st.subheader("✍️ Ingresá tu idea o borrador")

# Entrada del usuario
user_text = st.text_area(
    "Texto base:",
    height=150,
    placeholder="Ej: crear una carta para pedir información"
)

text_type = st.selectbox(
    "Tipo de texto:",
    [
        "Email formal",
        "Texto académico corto",
        "Descripción de producto",
        "Publicación profesional"
    ]
)

# Cargar el modelo (sin API)
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

generator = load_model()

# Botón de generación
if st.button("🚀 Generar texto con IA"):
    if user_text.strip() == "":
        st.warning("Por favor ingresá un texto base.")
    else:
        prompt = f"""
{text_type} en español.

Texto base:
{user_text}

Texto final:
"""

        result = generator(
            prompt,
            max_length=250,
            do_sample=False
        )

        st.subheader("✅ Texto generado")
        st.write(result[0]["generated_text"])

# Sección Cómo funciona
st.markdown("---")
st.subheader("ℹ️ ¿Cómo funciona?")

st.markdown(
    "1. Ingresás una idea o texto base.\n"
    "2. Seleccionás el tipo de texto.\n"
    "3. Presionás el botón de generación.\n"
    "4. La IA genera un texto listo para usar."
)
