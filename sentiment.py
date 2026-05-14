def analizar_sentimiento(texto):
    analisis = TextBlob(texto)

    polaridad = analisis.sentiment.polarity

    if polaridad > 0:
        return "positivo"
    elif polaridad < 0:
        return "negativo"
    else:
        return "neutral"
