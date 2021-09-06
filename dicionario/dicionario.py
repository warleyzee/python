#Criação de um dicionário

cadastro = {
    'Colaborador1' : {
        'Nome':'Warley',
        'sobrenome':'Souza',
        'idade':29,
        'cidade':'Brasilia',
        'tamanho':1.81,
        'casado':'Não'
    },
    'colaborador2' : {
        'Nome':'Warley',
        'sobrenome':'Souza',
        'idade':29,
        'cidade':'Brasilia',
        'tamanho':1.81,
        'casado':'Não'
    }
    
}
for cadastro_k, valor_v in cadastro.items():
    print(f'Exibindo {cadastro_k}')
    for item_k, item_v in valor_v.items():
        print(f'\t{item_k} = {item_v}')