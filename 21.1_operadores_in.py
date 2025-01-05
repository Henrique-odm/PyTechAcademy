nome = input ("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:# se encontrar está em nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')#se não encontar não está em nome