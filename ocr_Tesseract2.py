import pytesseract
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path

def detect_text_with_tesseract():
    # Caminho do arquivo (pode ser PDF ou imagem)
    file_path = Path(__file__).parent / "images" / "lista de materia.pdf"  # Modifique para o seu arquivo

    try:
        # Verifica se o arquivo é um PDF ou imagem
        if file_path.suffix.lower() == ".pdf":
            # Converte o PDF em imagens
            images = convert_from_path(file_path)
            for i, image in enumerate(images):
                # Usando o Tesseract para OCR em cada página do PDF convertida para imagem
                print(f"Texto detectado na página {i+1}:")
                text = pytesseract.image_to_string(image)
                print(text)
        else:
            # Se for uma imagem, aplica o OCR diretamente
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img)
            print("Texto detectado na imagem:")
            print(text)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    detect_text_with_tesseract()
