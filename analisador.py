import os
import string
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize


# Baixar recurso punkt se necessário
nltk.download('punkt')

# Pastas
INPUT_FOLDER = "textos"
OUTPUT_FOLDER = "resultados"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def limpar_texto(texto):
    """Remove pontuação e deixa tudo minúsculo"""
    texto = texto.lower()
    return texto.translate(str.maketrans('', '', string.punctuation))


def analisar_texto(caminho_arquivo):
    """Conta frequência de palavras em um arquivo de texto"""
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    texto_limpo = limpar_texto(texto)
    palavras = word_tokenize(texto_limpo)
    frequencias = Counter(palavras)
    return frequencias


def salvar_resultado(frequencias, nome_arquivo):
    """Salva o resultado da análise"""
    caminho_saida = os.path.join(OUTPUT_FOLDER, f"frequencias_{nome_arquivo}")
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        for palavra, contagem in frequencias.most_common():
            f.write(f"{palavra}: {contagem}\n")
        print(f"Resultado salvo em {caminho_saida}")


def main():
    for arquivo in os.listdir(INPUT_FOLDER):
        if arquivo.endswith(".txt"):
            caminho = os.path.join(INPUT_FOLDER, arquivo)
            frequencias = analisar_texto(caminho)
            salvar_resultado(frequencias, arquivo)


if __name__ == "__main__":
    main()
