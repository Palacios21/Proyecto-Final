import streamlit as st
from PIL import Image
from sentiment import analizar_sentimiento
from ocr import extraer_texto
from mqtt_client import enviar_mqtt
from text_to_speech import generar_audio

st.set_page_config(page_title="Sistema Multimodal", layout="wide")

st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

.main {
    background-color: #0f172a;
}

.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Sistema Inteligente Multimodal")

opcion = st.sidebar.selectbox(
    "Seleccione entrada",
    ["Texto", "Imagen"]
)

if opcion == "Texto":
    texto = st.text_area("Ingrese texto")

    if st.button("Analizar"):
        sentimiento = analizar_sentimiento(texto)

        st.success(f"Sentimiento detectado: {sentimiento}")

        generar_audio(f"El sentimiento detectado es {sentimiento}")

        audio_file = open("respuesta.mp3", "rb")
        st.audio(audio_file.read())

        if sentimiento == "positivo":
            enviar_mqtt("iot/sentimiento", "verde")
        else:
            enviar_mqtt("iot/sentimiento", "rojo")

if opcion == "Imagen":
    imagen = st.file_uploader("Suba una imagen", type=["png", "jpg", "jpeg"])

    if imagen:
        img = Image.open(imagen)

        st.image(img, caption="Imagen subida")

        texto_extraido = extraer_texto(img)

        st.write("Texto detectado:")
        st.code(texto_extraido)

        sentimiento = analizar_sentimiento(texto_extraido)

        st.success(f"Sentimiento detectado: {sentimiento}")

        generar_audio(f"El sentimiento detectado es {sentimiento}")

        audio_file = open("respuesta.mp3", "rb")
        st.audio(audio_file.read())

        if sentimiento == "positivo":
            enviar_mqtt("iot/sentimiento", "verde")
        else:
            enviar_mqtt("iot/sentimiento", "rojo")
