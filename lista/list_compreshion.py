#lista comum
l1 = [1,2,3,4,5,6,7,8,9]

#criando uma nova lista a partir de uma existente
ex1 = [variavel for variavel in l1]

#multiplicando os valores de uma lista ja criada
ex2 = [v*2 for v in ex1]

#criando um tupla 
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

#criando uma lista de string
l2 = ['Warley', 'Henrique', 'Souza']

#subistituindo os a por @
ex4 = [v.replace('a', '@') for v in l2]

print(f'lista Comum:   {ex1}')
print(f'lista Mult 2:  {ex2}')
print(f'lista Tupla:   {ex3}')
print(f'lista Strings: {ex4}')