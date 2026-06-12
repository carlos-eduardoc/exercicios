"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def line():
    print('-' * 15)

def ficha(nome='<jogador desconhecidos>', gols=0):

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    line()
    
    return f'Ficha de dados: \nNome do jogador: {nome} \nGol(s): {gols}'


dados = ficha(nome=input('Seu nome: ').strip(), gols=str(input('Quantos gols marcados: ')).strip())
print(dados)