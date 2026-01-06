import streamlit as st
import google.generativeai as genai

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
    placeholder="Ej: Quiero enviar un mail para solicitar información..."
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

if st.button("🚀 Generar texto con IA"):
    if user_text.strip() == "":
        st.warning("Por favor ingresá un texto base.")
    else:
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel("gemini-1.0-pro")

            prompt = f"""
            Actúa como un asistente experto en redacción profesional.
            A partir del siguiente texto base, genera un {text_type}
            claro, coherente y bien estructurado.

            Texto base:
            {user_text}
            """

            response = model.generate_content(prompt)

            st.subheader("✅ Texto generado")
            st.write(response.text)

        except Exception as e:
            st.error(f"❌ Error real: {e}")

st.markdown("---")
st.subheader("ℹ️ ¿Cómo funciona?")

st.markdown("""
1. Ingresás una idea o texto base.  
2. Seleccionás el tipo de texto.  
3. Presionás el botón de generación.  
4. La IA genera un texto optimizado listo para usar.
""")
