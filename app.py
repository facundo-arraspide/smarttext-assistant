import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 SmartText Assistant")
st.write(
    "SmartText Assistant es una aplicación web con Inteligencia Artificial "
    "que genera textos claros y profesionales a partir de una idea base."
)

st.subheader("✍️ Ingresá tu idea o borrador")

user_text = st.text_area(
    "Texto base:",
    height=150,
    placeholder="Ej: Necesito enviar un mail para solicitar información..."
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

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

generator = load_model()

if st.button("🚀 Generar texto con IA"):
    if user_text.strip() == "":
        st.warning("Por favor ingresá un texto base.")
    else:
        # PROMPT CORREGIDO (CLAVE)
        prompt = f"""
Redactá el siguiente texto en español.

Tipo de texto: {text_type}

Texto:
{user_text}

Texto final:
"""

        result = generator(
            prompt,
            max_length=250,
            do_sample=True,
            temperature=0.7
        )

        st.subheader("✅ Texto generado")
        st.write(result[0]["generated_text"])

st.markdown("---")
st.subheader("ℹ️ ¿Cómo funciona?")

st.markdown("""
1. In
