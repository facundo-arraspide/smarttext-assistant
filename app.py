import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="✍️",
    layout="centered"
)

st.title("SmartText Assistant")
st.write("Mejorá y reescribí textos en español de forma clara y profesional.")

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="mrm8488/mbart-large-finetuned-opus-es-en"
    )

generator = load_model()

st.markdown("### ✍️ Ingresá un texto base")
texto = st.text_area(
    "Texto:",
    placeholder="hola buenas nesecito una carta para quejarme de algo",
    height=120
)

if st.button("Generar texto"):
    if not texto.strip():
        st.warning("Ingresá un texto.")
    else:
        prompt = f"Reescribí el siguiente texto en español formal y profesional:\n{texto}"

        with st.spinner("Generando texto..."):
            result = generator(
                prompt,
                max_length=300,
                do_sample=False
            )

        st.markdown("### ✅ Texto generado")
        st.write(result[0]["generated_text"])

st.markdown("---")
st.caption("Proyecto académico – SmartText Assistant")
