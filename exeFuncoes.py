#1 faça uma função que retorno uma saudação e um nome
def saudacao(msg, nome):
    return f'{msg} {nome}, seja vem vindo'

saudacao = saudacao("Ola", "Warley")

print(saudacao)

#2 faca uma função que receba 3 numero e some eles
def somar(n1, n2, n3):
    return n1 +n2+n3

soma = somar(4,5,8)
print (soma)

#3 faça uma função que receba um numero e uma porcentagem, depois some a porcentagem ao numero 
def porcento(n1, porc):
    return n1 + (n1 * porc/100)

calc = porcento(100,50)
print(calc)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def divisao(n1):
    if(n1 % 3 == 0 and n1 % 5 == 0):
        return 'Fizz Buzz'
    elif(n1 % 5 == 0):
        return 'Buzz'
    elif (n1 % 3 == 0):
        return 'Fizz '
    else:
        pass

    return n1

dividir = divisao(11)
print (dividir)

#5 Faça uma função  que recebe  uma função2  como paramentro e retorno o valor da  função2 executada.
def func ():
    n1 = 1
    n2 = 2
    return n1, n2

def func2 (funcao):
    return funcao()
    

var = func2(func)
print (var)

#6 Faça uma função  que recebe  uma função2  como paramentro e retorno o valor da  função2 executada. 
# Faça a função1 executar duas  funçoes  que receba um numero diferente como argumento 

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def diga_oi(oi):
    return f'{oi}'

def diga_ola(ola):
    return f'{ola}'

diga = mestre(diga_oi,'warley')
diga2 = mestre(diga_ola,'Henrique')
print (diga)
print (diga2)
