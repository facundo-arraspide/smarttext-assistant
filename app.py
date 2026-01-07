import streamlit as st
from transformers import pipeline

# Configuración de la página
st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="✍️",
    layout="centered"
)

st.title("Asistente de SmartText")
st.write(
    "SmartText Assistant es una aplicación web con Inteligencia Artificial "
    "que mejora y reescribe textos en español usando un tono formal, claro y profesional."
)

# Cargar modelo (liviano y gratuito)
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

generator = load_model()

# Entrada del usuario
st.markdown("### ✍️ Ingresá un texto base")
texto_usuario = st.text_area(
    "Texto:",
    placeholder="Ejemplo: hola buenas nesecito una carta para quejarme de algo",
    height=120
)

# Botón
if st.button("Generar texto"):
    if not texto_usuario.strip():
        st.warning("Por favor, ingresá un texto para mejorar.")
    else:
        prompt = f"""
You are a professional writing assistant.

Task:
Rewrite the following text in formal, clear and professional Spanish.
Do not explain anything.
Do not repeat the instructions.
Only return the final rewritten text.

Text:
"{texto_usuario}"
"""

        with st.spinner("Generando texto..."):
            result = generator(
                prompt,
                max_length=250,
                do_sample=False
            )

        texto_generado = result[0]["generated_text"]

        st.markdown("### ✅ Texto generado")
        st.write(texto_generado)

# Footer
st.markdown("---")
st.caption("Proyecto académico – SmartText Assistant")
