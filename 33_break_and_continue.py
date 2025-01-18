contador = 0

while contador <= 20:
    contador += 1 # controlador do seu while
   
    if contador == 6: #bloco para pular o número que deseja
        print("Não vou mostrar o 6.")
        continue

    if contador >= 10 and contador <= 18: #bloco de código onde você gostaria que o programa parasse de executar
        print("Não vou mostrar o", contador)
        continue

    print(contador)

    if contador == 20:
        break #função de parar

print("Acabou")

# caso o programa entre no loop (execute o KeyboardInterrupt Ctrl+C no terminal)