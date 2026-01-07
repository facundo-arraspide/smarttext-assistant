import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="🤖"
)

st.title("🤖 SmartText Assistant")
st.write(
    "Aplicación web con Inteligencia Artificial que mejora textos "
    "y los convierte en versiones más claras y profesionales."
)

st.subheader("✍️ Ingresá un texto base")

user_text = st.text_area(
    "Texto:",
    height=150,
    placeholder="Ej: hola buenas necesito una carta para quejarme de algo"
)

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

model = load_model()

if st.button("🚀 Mejorar texto"):
    if user_text.strip() == "":
        st.warning("Por favor ingresá un texto.")
    else:
        prompt = f"""
Rewrite the following text in Spanish using a formal, clear and professional tone.

Text:
{user_text}

Improved version:
"""

        result = model(
            prompt,
            max_length=200,
            do_sample=False
        )

        st.subheader("✅ Texto generado")
        st.write(result[0]["generated_text"])

st.markdown("---")
st.subheader("ℹ️ ¿Cómo funciona?")
st.markdown(
    "1. Ingresás un texto base.\n"
    "2. Presionás el botón de mejora.\n"
    "3. La IA devuelve una versión más profesional del texto."
)
