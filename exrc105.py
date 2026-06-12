"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

"""    

from datetime import datetime as dt
    
def voto(ano_nascimento):

    idade = dt.now().year - ano_nascimento

    if idade < 16:
        return 'VOTO NEGADO'
    elif idade <= 16 or idade == 17:
        return 'Voto OPCIONAL'
    else:
        return 'VOTO OBRIGATORIO'



voto(ano_nascimento = int(input('Digite seu ano de nascimento: ')))
    
