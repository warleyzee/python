#valor a ser fatiado
string = '012345678901234567890123456789012345678901234567890123456789'
# variavel para fatiar a string
n = 10
#fatiando a string com os 10 digitos
lista = [string[i:i+n] for i in range(0, len(string), n)]
#join, juntando a lista com o ponto '.'
retorno = '.'.join(lista)
print()
print(lista)
print()
print(retorno)
print()