import spacy
from collections import defaultdict
import sys

if len(sys.argv) != 2:
    sys.exit(1)

nlp = spacy.load('pt_core_news_lg')

def criarIndice(listaArquivos):
    stopwords = {' ', '.', '...', ',', '!', '?', '\n'}
    
    indiceInvertido = defaultdict(lambda: defaultdict(lambda: {'frequencia': 0}))
    for numeroArquivo, arquivo in enumerate(listaArquivos):
        with open(arquivo, 'r') as arquivoAberto:
            texto = arquivoAberto.read()
            doc = nlp(texto.lower()) 
            
            for token in doc:
                tokenTexto = token.text.strip()
                if tokenTexto and not token.is_stop and not token.is_punct and tokenTexto not in stopwords:
                    indiceInvertido[token.lemma_][numeroArquivo]['frequencia'] += 1

    return indiceInvertido 

caminhoListaDoc = sys.argv[1]
with open(caminhoListaDoc, 'r') as arquivoAberto:
    listaArquivos = [linha.strip() for linha in arquivoAberto]

indice = criarIndice(listaArquivos)

with open("indice.txt", "w") as arquivo:
    for termo, documentos in sorted(indice.items()):
        freqPorDocumento = ", ".join([f'{numeroDocumento+1}, {dados["frequencia"]}' for numeroDocumento, dados in documentos.items()])
        print(f'{termo}: {freqPorDocumento}')
        arquivoEscrita = f'{termo}:  {freqPorDocumento}'
        arquivo.write(arquivoEscrita + '\n')
