import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="🤖"
)

st.title("🤖 SmartText Assistant")
st.write("Generador simple de textos con IA a partir de una idea.")

# Entrada del usuario
user_text = st.text_input(
    "Ingresá una idea:",
    placeholder="Ej: crear una carta para pedir información"
)

text_type = st.selectbox(
    "Tipo de texto",
    ["Email formal", "Texto académico", "Descripción de producto"]
)

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

model = load_model()

if st.button("Generar texto"):
    if user_text.strip() == "":
        st.warning("Ingresá una idea primero.")
    else:
        prompt = f"Write a {text_type.lower()} in Spanish about: {user_text}"

        result = model(
            prompt,
            max_length=200
        )

        st.subheader("✅ Texto generado")
        st.write(result[0]["generated_text"])
