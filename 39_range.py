"""
for + range
range -> range(start, stop, step)
"""
# numeros = range(10) #range(10) significa que eu queros numeros de 1 a 10
# numeros = range(5, 10) #numeros de 5 a 10
# numeros = range(5, 10, 2) #pula os numeros de 2 em 2 (star 5, stop 10, step 2)
# print(numeros)

numeros = range(0, 11, 2) #start, stop, step

#variável (numero), variável criada permitida através do for!
for numero in numeros:
    print(numero)
