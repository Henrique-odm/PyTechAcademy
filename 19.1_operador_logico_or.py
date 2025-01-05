#Avaliação de circuito
#print(True or False)
#print( False or False or "abc") # o sistema sempre irá procurar a resposta verdadeira "abc"
#print( False or False or "abc" or True) # uma vez que o "abc" é verdadeiro, ele não executa o último verdadeiro (True)

#Avaliação de circuito
senha = input("senha: ") or 'sem senha'
print(senha)