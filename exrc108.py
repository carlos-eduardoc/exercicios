"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""

from time import sleep as sl


def leiaInt(msg):
    msg = input(msg)

    while not msg.isnumeric():
        print('Validando resposta...')
        sl(0.35)
        print('\033[31mERRO! Digite um inteiro!\033[0m')
        

        msg = input('Digite novamente: ')

    msg = int(msg)

    return msg    

n = leiaInt('Digite um algo: ')
print(f'Voce acabou de digitar o numero {n}')
