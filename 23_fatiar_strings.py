"""
Fatiamento de strings
 012345678
 olá mundo
-987654321
Fatiamento [i:f:p] [::] #i: inicio / #f: fim / #p: pular letras

obs: A fubnção len retorna a quantidade de carateres da str
"""

variavel = "Olá mundo"
print(variavel[0:]) #[-9:] ele exibirá tudo

variavel = "Olá mundo"
print(len(variavel)) #contagem de caracteres

variavel = "Olá mundo"
print(variavel[0:9:2]) #contagem ao contrário