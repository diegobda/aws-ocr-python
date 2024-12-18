import pytesseract
from PIL import Image
from pathlib import Path

def detect_text_with_tesseract():
    # Caminho do arquivo de imagem (pode ser PNG, JPEG, etc.)
    file_path = Path(__file__).parent / "images" / "lista de materia.png"

    try:
        # Abrir a imagem
        img = Image.open(file_path)

        # Usar Tesseract para fazer OCR na imagem
        text = pytesseract.image_to_string(img)

        # Exibir o texto detectado
        print("Texto detectado:")
        print(text)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    detect_text_with_tesseract()
