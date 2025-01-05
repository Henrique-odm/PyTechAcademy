# operadores lógicos
# and (e) / todas as condições precisam ser verdadeiras
# or (ou)
# not (não)
# 0 0 0 false
# "" false
# None (um não valor)

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("senha: ")

#Variável
senha_permitida = "Henrique1106#"

#if e and - sempre será: True (verdadeiro)
if entrada == "E"and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")