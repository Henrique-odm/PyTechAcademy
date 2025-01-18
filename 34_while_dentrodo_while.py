qtd_linhas = 3
qtd_colunas = 1

linha = 1 #contador
while linha <= qtd_linhas:#enquanto linha for menor ou igual a quantidade de linhas:
     coluna = 1 #coluna começa do 1
     
     while coluna <= qtd_colunas: #enquanto coluna for menor ou igual a quantidade de colunas           
        print(f"{linha=} {coluna=}")   #{linha=} {coluna=} o sinal de igual (=) exibir o nome da variável   
        coluna += 1 #controle do while interno
     linha += 1 #controle do while interno

print("acabou")

#EXECUTAR O DEBUG PARA INTENDER A INTERPRETAÇ]AO DO PROGRAMA!