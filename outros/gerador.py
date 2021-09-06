import sys
import time

def gera():
    for n in range(10):
        #função yield vai imprimindo os valores um de cada vez sem esperar todos de uma vez.
        yield n
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)


#diferença de tamanho em memoria de lista (l1) para gerador(l2)

l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))
print('DIFERENÇA DE TAMANHO ENTRE LISTA E GERADOR')
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))