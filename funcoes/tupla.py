#Declaração de Tuplas, lembrando que tuplas nao podem ser editadas a menos que virem listas
t1 = (1,2,3, 'warley', 'souza', 3.4, 'henrique')
t2 = 1,2,3, 'warley', 'souza', 3.4, 'henrique'
t3 = 1,
# print(type(t1))
# print(type(t2))
# print(type(t3))

#transformando a tupla em lista para edita-la
t1 = list(t1)

#editando a lista
t1[3] = 'warley henrique de souza'

#Comando pop para apagar um item da lista, passando o argumento 
t1.pop(4)
t1.pop(5)

print(t1)