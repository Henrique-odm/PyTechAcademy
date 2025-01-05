#or (ou)
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("senha: ")

#Variável
senha_permitida = "Henrique1106#"

#if e and - sempre será: True (verdadeiro)
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")