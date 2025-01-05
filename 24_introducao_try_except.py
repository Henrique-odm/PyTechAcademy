"""
introdução ao try/except
try--> tentar executar o código
except--> ocorreu algun erro ao tentar executar
"""
#print(1234)
#print(456)
#int("a") # estourou a excessão: o python vai indentificar um erro

#teste 1
#numero = input("vou dobrar o número que você digitar: ")
#print(f'O dobro de {numero} é {numero * 2}') # ele vai dar erro na multiplicação

#teste 2 com correção
#numero = input("vou dobrar o número que você digitar: ")

#numero_float = float(numero)# correção
#print(f'O dobro de {numero} é {numero_float * 2:.2f}') 

#teste 3
#numero_str = input("vou dobrar o número que você digitar: ")

#print(numero_str.isdigit())#isdigit (checa se o usuário digitou apenas números)ele é um teste boll

#numero_float = float(numero_str)
#print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') 

#teste 4
#numero_str = input("vou dobrar o número que você digitar: ")

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') 
#else:
#    print("Isso não é um número")

#teste 5
numero_str = input("vou dobrar o número que você digitar: ")

try:
    print("STR:", numero_str)
    numero_float = float(numero_str) # se usuário digitar letras, o programa morre aqui
    print("FLOAT", numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') 
except:
    print("Isso não é um número")