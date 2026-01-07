import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="🤖"
)

st.title("🤖 SmartText Assistant")
st.write(
    "Esta aplicación usa Inteligencia Artificial para mejorar y reescribir "
    "textos en español de forma clara y profesional."
)

st.subheader("✍️ Ingresá un texto base")

user_text = st.text_area(
    "Texto:",
    height=150,
    placeholder="Ej: hola, quiero pedir información sobre un producto"
)

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

model = load_model()

if st.button("🚀 Mejorar texto con IA"):
    if user_text.strip() == "":
        st.warning("Por favor ingresá un texto.")
    else:
        prompt = f"""
Reescribí el siguiente texto en español usando un tono formal, claro y profesional:

Texto:
{user_text}

Texto mejorado:
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
    "3. La IA reescribe el texto de forma más profesional."
)
