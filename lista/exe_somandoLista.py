lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]

somando_lista = []

#Modulo convencional de somar as duas listas
for l1, l2 in zip(lista1, lista2):
    somando_lista.append(l1+l2)

print(list(somando_lista))

#Utilizando list compreshion
lista_soma = [x + y for x, y in zip(lista1, lista2)]
print('Somando os valores da List Compreshion:')
print(lista_soma)
print()

