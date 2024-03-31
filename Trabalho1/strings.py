
#TRATAMENTO DE STRINGS EM PYTHON

palavra = "universo"

print(palavra[1]) #retorna a letra 'n' de UNIVERSO

print(palavra[3:6]) #retorna do caracter acima do 3 ao 6

print(palavra[::-1]) #inverte a palavra

print(palavra*3) #repete a string 3x

texto = "marcia"
for c in texto:
    print(c) #itera cada caracter de marcia
    
for j in range(0, len(texto), 1):
    print(texto[j]) #j percorre cada índice de texto (0 até len(texto) de um em um)
    
#METODOS STRING

tex = "SARa"
print(tex.lower()) # retorna uma cópia da string com os caracteres alfabéticos em minúsculos

print(tex.upper()) # retorna uma cópia da string com os caracteres alfabéticos em maiúsculos

print(tex.islower()) # retorna True se todos os caracteres alfabéticos são minúsculos

print(tex.isupper()) # retorna True se todos os caracteres alfabéticos são maiusculos

print(tex.isalpha()) # retorna True se todos os caracteres da string são dígitos alfabeticos

print(tex.isdigit()) # retorna True se todos os caracteres da string são dígitos númericos

    