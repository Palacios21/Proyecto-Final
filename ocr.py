import pytesseract
import cv2
import numpy as np


def extraer_texto(imagen):
    imagen_np = np.array(imagen)

    gray = cv2.cvtColor(imagen_np, cv2.COLOR_BGR2GRAY)

    texto = pytesseract.image_to_string(gray, lang='eng')

    return texto
