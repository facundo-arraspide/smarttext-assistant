import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 SmartText Assistant")
st.write(
    "Aplicación web que utiliza un modelo de lenguaje (LLM) "
    "para generar textos formales y profesionales."
)

st.markdown("### ✍️ Ingresá tu texto base")

user_text = st.text_area(
    "Texto:",
    height=120,
    placeholder="hola buenas necesito una carta para quejarme de algo"
)

text_type = st.selectbox(
    "Tipo de texto:",
    [
        "Email formal",
        "Carta de reclamo",
        "Solicitud de información"
    ]
)

if st.button("🚀 Generar texto con IA"):
    if not user_text.strip():
        st.warning("Por favor ingresá un texto.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            prompt = f"""
Redactá un {text_type} en español.
Usá un tono formal, claro y profesional.
NO expliques lo que vas a hacer.
NO repitas la consigna.
Escribí únicamente el texto final.

Texto base:
{user_text}
"""

            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )

            st.markdown("### ✅ Texto generado")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error al generar el texto: {e}")

st.markdown("---")
st.subheader("ℹ️ ¿Cómo funciona?")
st.markdown("""
1. El usuario ingresa un texto base.  
2. La aplicación envía la solicitud a un **modelo de lenguaje (LLM)**.  
3. El modelo procesa el texto y genera una respuesta formal.  
4. El resultado se muestra en pantalla.
""")
