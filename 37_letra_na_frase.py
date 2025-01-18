"""
Qual a letra que mais apareceu nessa frase?

.lower() para letras minúsculas
.upper() para letras minúsculas
.frase() para identificar a frase
.count() para contagem de letras
"""

frase = "o Python é uma linguagem de programação " \
    "multiparadigma. "\
    "Python foi criado por Guido van Rossum. "

#print(frase.count("o"))#quantas vezes "LETRAS OU PALAVRAS" apareceu nessa frase?

#i = 0
#while i < len(frase):
#    letra_atual = frase [i]
#    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    
    
#    print(letra_atual, quantas_vezes_letra_apareceu)
#    i += 1

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ""

while i < len(frase):
    letra_atual = frase [i]

    if letra_atual == " ":
        i += 1 # para o sistem não entrar em um loop!
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_mais_vezes <= qtd_atual:
        qtd_mais_vezes = qtd_atual
        letra_mais_vezes = letra_atual

    i += 1
print(
    "A letra que apareceu mais vezes foi "
    f'"{letra_mais_vezes}" que apareceu '
    f'{qtd_mais_vezes} x'
   
 ) #se as letras empatarem, o sistema irá considerar semrpe a última letra que apareceu mais vezes!
    
   