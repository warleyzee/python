#Somar os valores de uma lista usando uma list Comprehension
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 1', 50))
carrinho.append(('Produto 1', 5.90))
carrinho.append(('Produto 1', 50.10))
carrinho.append(('Produto 1', 50))

#pega todos os valores da lista
total_lista = [float(y) for x,y in carrinho]
print(total_lista)

#sum soma o valor da lista
total = sum([float(y) for x,y in carrinho])
print(total)

