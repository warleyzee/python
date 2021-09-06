lista = [
    ('key', 'value'),
    ('key2', 'value2'),
    ('key3', 'value3')
]

#refazendo a lista
d1 = {x: y for x,y in lista}
#multiplicando o value por 2
d2 = {x: y*2 for x,y in lista}
#colocando em caixa alta a chave e valor
d3 = {x.upper(): y.upper() for x,y in lista}

print(d1)
print(d2)
print(d3)