# OCR com Tesseract

Este projeto usa o **Tesseract OCR**, uma ferramenta de código aberto para reconhecimento óptico de caracteres (OCR). O Tesseract pode extrair texto de imagens, como arquivos de imagem PNG, JPEG, entre outros. A principal vantagem é que você **não precisa de uma conta em nuvem** para utilizar a ferramenta, tornando-a ideal para ser executada localmente.

## Requisitos

Antes de executar o código, é necessário instalar o Tesseract OCR na sua máquina e configurar o ambiente Python.

### 1. Instalar o Tesseract

#### Windows
- Baixe e instale o Tesseract a partir deste [link](https://github.com/UB-Mannheim/tesseract/wiki).
- Durante a instalação, certifique-se de adicionar o caminho do Tesseract ao `PATH` do sistema.

#### Linux
- No Linux, você pode instalar o Tesseract usando o seguinte comando:

  ```bash
  sudo apt install tesseract-ocr
