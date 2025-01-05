"""
flag (bandeira) - marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True
passou_no_if = None #um não valor

if condicao:
    passou_no_if = True #flag (variável dentro das condições)
    print("Faça algo")
else:
    print("Não faça algo")

if passou_no_if is None: #é um não valor
    print("Não passou no if")
if passou_no_if is not None: #não é um valor
    print("Passou no if")