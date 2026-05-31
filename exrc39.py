"""
Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import datetime


anos = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - anos

if idade > 18:
    passou = idade - 18
    print(f'Sua idade é {idade}, voce ja passou da idade para alistamento a exatos {passou} anos ')
elif idade < 18:    
    falta = 18 - idade
    print(f'Sua idade é {idade}, e voce nao precisa se alistar falta exatos {falta} anos')
else:
    print('Voce deve se alistar pois tem 18 anos')
