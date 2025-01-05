"""
Formatação básica de strings
s : string
d : int
f : float
.<número de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> : Esquerda
< : Direita
^ : centro
Sinal : + ou -
Ex.: 0>-100,.1f
Conversion flags: -!r !s !a
"""
variavel = "abc"
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{variavel: <10}')
print(f'{2000.00:+10,.1f}')
print(f'{1500:08x}')
print(f'{variavel!r}')
