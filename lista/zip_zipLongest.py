"""
ZIP         - Unindo Interáveis
ZIP_LONGEST - Itertools
"""
from itertools import zip_longest, count

#Criar um indice automatico 
indice = count()
"""
Código
"""
cidade = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']

"""
Mais Código
"""

estado = ['SP', 'MG', 'BA']

"""
Mais Código
"""

siglas = ['SP', 'BH', 'SV', 'MB', 'Ot']

#Zip reuni todas as lista contando a menor lista, neste caso a lista de estados
cidade_estado = zip(indice, cidade, siglas, estado)

for indice, cidade, siglas, estado in cidade_estado:
    print(indice, cidade, siglas, estado)

print("IMPRIMIR LISTA COMPLETA")

#zip_longuest imprime toda as listas, onde estiver vazio fica com o valor NONE a menos que user fillvalue, 
cidade_estado_siglas = zip_longest(cidade, siglas, estado, fillvalue='Estados')
print(list(cidade_estado_siglas))