import os
import pytesseract
from PIL import Image

# Ruta al ejecutable de Tesseract en Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta a la carpeta tessdata
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

def extraer_texto_de_imagen(imagen_path, lang='spa'):
    """
    Extrae texto de una imagen usando Tesseract OCR.
    lang puede ser 'eng' para inglés o 'spa' para español (si tienes el traineddata).
    """
    try:
        imagen = Image.open(imagen_path)
        texto = pytesseract.image_to_string(imagen, lang=lang)
        return texto
    except Exception as e:
        return f"[ERROR] {imagen_path}: {e}"

def main():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    archivos = [f"Diapositiva{i}.png" for i in range(1, 54)]
    salida_md = os.path.join(carpeta, "presentacion_libranza.md")

    with open(salida_md, "w", encoding="utf-8") as f:
        for archivo in archivos:
            ruta = os.path.join(carpeta, archivo)
            if os.path.exists(ruta):
                f.write(f"# {archivo}\n\n")
                texto = extraer_texto_de_imagen(ruta, lang='spa')  # Cambia a 'eng' si el texto está en inglés
                f.write(texto.strip() + "\n\n")
            else:
                f.write(f"# {archivo}\n[Imagen no encontrada]\n\n")

    print(f"Archivo Markdown generado: {salida_md}")

if __name__ == "__main__":
    main()
