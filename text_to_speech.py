from gtts import gTTS


def generar_audio(texto):
    tts = gTTS(text=texto, lang='es')
    tts.save("respuesta.mp3")
