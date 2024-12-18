import json
from pathlib import Path
import boto3
from botocore.exceptions import ClientError

def detect_file_text():
    # Inicializar cliente do AWS Textract
    client = boto3.client("textract")

    # Caminho do arquivo
    file_path = Path(__file__).parent / "images" / "lista de materia.png"

    try:
        # Abrir o arquivo em modo binário
        with open(file_path, "rb") as f:
            file_bytes = f.read()

        # Chamar a API DetectDocumentText
        response = client.detect_document_text(Document={"Bytes": file_bytes})

        # Processar e exibir os resultados
        print("Texto detectado:")
        for block in response.get("Blocks", []):
            if block["BlockType"] == "LINE":
                print(block["Text"])

        # Salvar resultado em um arquivo JSON (opcional)
        output_path = Path(__file__).parent / "output.json"
        with open(output_path, "w", encoding="utf-8") as outfile:
            json.dump(response, outfile, indent=4, ensure_ascii=False)
        print(f"Resultado salvo em: {output_path}")

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
    except ClientError as e:
        print(f"Erro ao chamar o AWS Textract: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    detect_file_text()
