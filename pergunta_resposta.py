print()
print('Texto explicativo:')

pergunta = {
    'Pergunta 1':{
        'pergunta': 'quanto é 2+2?',
        'respostas':{
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 2':{
        'pergunta': 'quanto é 1+1?',
        'respostas':{
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 3':{
        'pergunta': 'quanto é 1+2?',
        'respostas':{
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 4':{
        'pergunta': 'quanto é 10-6?',
        'respostas':{
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'd',
    },
}

soma_resposta = 0
soma_erro = 0

for chave_p, chave_r in pergunta.items():
    print(f'{chave_p} {chave_r["pergunta"]}')
    print('RESPOSTAS')
    for pergunta_p, resposta_r in chave_r['respostas'].items():
        print(f'[{pergunta_p}]: {resposta_r}')

    resposta_user = input('Sua resposta: ')
    if resposta_user == chave_r['resposta_certa']: 
        print('YEAHH, Nice Jobe')
        soma_resposta +=1
    else:
        print('NEXXXXXT')
        soma_erro +=1        
    print()

print(f'Voce acertou {soma_resposta}, e errou {soma_erro}')
    