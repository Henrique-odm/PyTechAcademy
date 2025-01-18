"""whuile/else"""

string = "valor qualquer"

i = 0 #(i) índice
while i < len(string):
    letra = string[i]

    #break (o break snedo executado dentro do while, nada será executado após, como exemplo o else!)
    print(letra)
    i += 1
else:
    print("O else foi executado.")
print("fora do while") #break em while, somenet essa linha será executada!