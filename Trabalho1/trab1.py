import spacy
from spacy.lang.pt.examples import sentences 

nlp = spacy.load("pt_core_news_sm")
sentence = nlp(u'A rodinha do computador')
for word in sentence:
    print(word.text, word.pos_)

print("Lista de tokens")
tokens = list(sentence)
print(tokens)
    
valor = tokens[2].orth_
print(valor)    
    

print("\n\n\n")    
    
print("Criando as entidades")
for entidade in sentence.ents:
    print(entidade.text + '-' + entidade.label_ + '- ' + str(spacy.explain(entidade.label_))) # listando entidades da sentença
    

print("\n\n\n")
    
print("Encontrando substantivos na frase:")
sentence2 = nlp(u'A rodinha do computador')
for noun in sentence2.noun_chunks:
    print(noun.text)
    
print("\n\n\n")
print ("Lematizacao")
for word in sentence:
    print(word.text + ' ===>', word.lemma_)

print('\n\n\n')
print("Lendo o arquivo a.txt")
with open('base/a.txt', "r") as arquivo:
    conteudo = arquivo.read()
    
    for palavras in conteudo:
        doc = spacy.load("pt_core_news_sm")
        tokentizacao = doc(conteudo)
        
        print(conteudo)