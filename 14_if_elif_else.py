# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == "entrar": #se o usuário digitar entrar
    print("Você entrou no sistema")#digitar tecla TAB para dar espaço e não dar erro no sistema
elif entrada == "sair": #se o usúario digitar sair
    print("Você saiu do sistema")#TAB
else:
    print("Você não digitou nem entrar e nem sair.")

#if - pode ser usado sozinho
#elif e else não pode estar sem o if
#else sempre vem por último       