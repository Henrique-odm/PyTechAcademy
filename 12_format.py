a = "Henrique"
b = "Andrade"
c = 1.1
formato = "a={nome1} b={nome2} c={nome3:.2f}".format(nome1=a, nome2=b,nome3=c) 

print(formato)

#argumentos dentro de format
#"a={} b={} c={:.2f}" «-strings
#c={:.2f} duas casas decimais
#nome1= «-parâmetros