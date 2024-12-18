📝 OCR Tesseract & AWS 🚀

Este repositório contém três scripts para extração de texto de arquivos de imagens e PDFs usando OCR (Reconhecimento Óptico de Caracteres). Utilizando duas abordagens distintas: Tesseract OCR (código aberto) e AWS Textract (solução em nuvem da Amazon).
📂 Arquivos

    ocr_Tesseract.py: Extrai texto de imagens utilizando o Tesseract OCR. 🖼️
    ocr_Tesseract2.py: Converte PDFs em imagens e aplica OCR para extrair texto. 📄➡️🖼️
    ocr_AWS.py: Exemplo de uso do AWS Textract para extração de texto de imagens ou PDFs diretamente na nuvem. ☁️

🚀 Funcionalidades

    📸 Imagens: Extração de texto de imagens no formato PNG, JPG, JPEG e outros.
    📄 PDFs: Converte PDFs para imagens e faz OCR nessas imagens.
    🤖 Tesseract OCR: Solução local de código aberto, ideal para quem não quer utilizar serviços em nuvem.
    ☁️ AWS Textract: Solução escalável e poderosa para OCR com a infraestrutura da AWS, ideal para grandes volumes de documentos.

🔧 Como usar
1️⃣ Tesseract OCR

    Instale o Tesseract:
        Linux: sudo apt install tesseract-ocr
        Mac: brew install tesseract
        Windows: Baixe e instale o Tesseract.

    Instale as dependências do Python:

pip install pytesseract pillow pdf2image

Execute o script para ler imagens (ocr_Tesseract.py):

    python ocr_Tesseract.py

2️⃣ Tesseract OCR para PDFs

    Instale as dependências do Python (mesmo para o ocr_Tesseract2.py):

pip install pytesseract pillow pdf2image

Execute o script para ler PDFs (ocr_Tesseract2.py):

    python ocr_Tesseract2.py

3️⃣ AWS Textract

    Configure sua conta AWS:
        Crie um usuário IAM com permissões para o AWS Textract.
        Configure as credenciais em ~/.aws/credentials (para Linux/Mac) ou no AWS CLI.

    Instale o pacote boto3:

pip install boto3

Execute o script de exemplo para AWS (ocr_AWS.py):

    python ocr_AWS.py

⚙️ Como funciona

    Tesseract: Usamos o Tesseract OCR para extrair texto de imagens ou PDFs convertidos para imagens. Ele pode ser configurado localmente e é ideal para projetos menores ou para quem não quer usar a nuvem.

    AWS Textract: Ao usar o AWS Textract, a extração de texto é feita diretamente na nuvem. Esse serviço é ótimo para documentos mais complexos e é altamente escalável. A única exigência é uma conta da AWS.

💻 Requisitos
Para Tesseract:

    Tesseract: Certifique-se de que o Tesseract esteja instalado corretamente no seu sistema.
    Python 3: O código foi testado com Python 3.6+.
    Dependências Python: pytesseract, pillow, pdf2image.

Para AWS Textract:

    Conta AWS: É necessário uma conta ativa na AWS com permissões para usar o AWS Textract.
    Credenciais AWS: Configure suas credenciais da AWS corretamente.

🛠️ Dependências

    pytesseract: Interface Python para o Tesseract OCR.
    pillow: Biblioteca de processamento de imagens.
    pdf2image: Converte PDFs em imagens para poder aplicar o OCR.
    boto3: Biblioteca da AWS para interagir com o Textract.

🚨 Atenção

    AWS Textract: É necessário configurar a conta da AWS corretamente e ter as permissões devidas para utilizar o Textract.
    Limitações do Tesseract: O Tesseract é eficaz, mas pode não ser tão preciso quanto o AWS Textract em documentos muito complexos.

    Develloper = DIEGO DOS SANTOS GONÇALVES - GOIÂNIA / GOIAS / BRASIL