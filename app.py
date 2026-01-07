import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ SmartText Assistant")
st.write("Aplicación web para mejorar y reescribir textos en español de forma clara y profesional.")

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="mrm8488/t5-small-spanish-summarization"
    )

generator = load_model()

st.markdown("### ✍️ Ingresá un texto base")
texto = st.text_area(
    "Texto:",
    height=120,
    placeholder="hola buenas nesecito una carta para quejarme de algo"
)

if st.button("Generar texto"):
    if not texto.strip():
        st.warning("Por favor ingresá un texto.")
    else:
        prompt = (
            "Reescribí el siguiente texto en español formal, claro y profesional. "
            "Escribí únicamente el texto final:\n\n"
            f"{texto}"
        )

        with st.spinner("Generando texto..."):
            result = generator(
                prompt,
                max_length=200,
                do_sample=False
            )

        st.markdown("### ✅ Texto generado")
        st.write(result[0]["generated_text"])

st.markdown("---")
st.caption("Proyecto académico – SmartText Assistant")
