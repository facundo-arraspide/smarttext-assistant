import streamlit as st

st.set_page_config(
    page_title="SmartText Assistant",
    page_icon="✉️",
    layout="centered"
)

st.title("✉️ SmartText Assistant")
st.write(
    "Aplicación web que genera textos formales y profesionales "
    "a partir de una idea base."
)

st.markdown("### ✍️ Ingresá un texto base")
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

def generar_texto(texto, tipo):
    if tipo == "Email formal":
        return f"""Estimado/a:

Me dirijo a usted con el fin de comunicarme formalmente respecto al siguiente asunto.

{texto.capitalize()}.

Quedo a disposición por cualquier información adicional que considere necesaria.

Atentamente,
"""

    if tipo == "Carta de reclamo":
        return f"""Por medio de la presente, me dirijo a usted para expresar un reclamo formal.

{texto.capitalize()}.

Espero una pronta respuesta y una solución a la situación planteada.

Sin otro particular, saludo atentamente.
"""

    if tipo == "Solicitud de información":
        return f"""Por medio de la presente, me comunico con usted para solicitar información relacionada con el siguiente tema:

{texto.capitalize()}.

Agradezco desde ya su atención y quedo a la espera de su respuesta.

Atentamente,
"""

if st.button("🚀 Generar texto"):
    if not user_text.strip():
        st.warning("Por favor ingresá un texto.")
    else:
        resultado = generar_texto(user_text, text_type)

        st.markdown("### ✅ Texto generado")
        st.text(resultado)

st.markdown("---")
st.caption("Proyecto académico – SmartText Assistant")
