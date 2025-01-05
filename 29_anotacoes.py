""""
try:
    Código que pode gerar uma exceção
except:
    Código para tratar de exceção
else:
    Código que será executado se não houiver exceção
finaly:
    Código que será executado sempre, com ou semm exceção
"""

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Não possível dividir por zero.")
else:
    print(f'Resultado: {resultado:.2F}')
finally:
    print("Finalizando o programa")