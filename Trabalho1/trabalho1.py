import spacy
from collections import defaultdict
import sys
from pathlib import Path

# Verificar se um caminho de arquivo foi fornecido como argumento
if len(sys.argv) != 2:
    print("Uso: python gerador_indice.py caminho_do_arquivo_com_lista_de_documentos")
    sys.exit(1)

# Carregar o modelo de língua portuguesa do SpaCy
nlp = spacy.load('pt_core_news_lg')

# Função para processar os documentos e criar o índice invertido
def criar_indice_invertido(lista_arquivos):
    stopwords_adicionais = {' ', '.', '...', ',', '!', '?', '\n'}
    
    indice_invertido = defaultdict(lambda: defaultdict(lambda: {'frequencia': 0}))
    for num_arquivo, arquivo in enumerate(lista_arquivos):
        with open(arquivo, 'r', encoding='utf-8') as f:
            texto = f.read()
            # Processar o texto com o modelo do SpaCy
            doc = nlp(texto.lower())
            # Iterar sobre os tokens do documento
            for pos, token in enumerate(doc):
                # Verificar se o token é relevante (não é stopword, não é pontuação e não está vazio)
                token_text = token.text.strip()
                if token_text and not token.is_stop and not token.is_punct and token_text not in stopwords_adicionais:
                    # Incrementar a contagem do termo no documento e adicionar a posição
                    indice_invertido[token.lemma_][num_arquivo]['frequencia'] += 1

    return indice_invertido



# Ler o arquivo com a lista de documentos
caminho_lista_documentos = sys.argv[1]
with open(caminho_lista_documentos, 'r') as f:
    lista_arquivos = [linha.strip() for linha in f]

# Criar o índice invertido
indice = criar_indice_invertido(lista_arquivos)



with open("indice.txt", "w") as arquivo:
    for termo, documentos in sorted(indice.items()):
        freqs_por_documento = ",".join([f'{num_doc+1},{dados["frequencia"]}' for num_doc, dados in documentos.items()])
        print(f'{termo}:  {freqs_por_documento}')
        arquivoEscrita = f'{termo}:  {freqs_por_documento}'
        arquivo.write(arquivoEscrita + '\n') 
