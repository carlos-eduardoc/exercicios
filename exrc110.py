"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer
Quando o usuário digitar Faça um mini-sistema que utilize o Interactive Help do Python.
 O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
 Importante: use cores.
a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""

from sys import exit as ex 
from colorama import init, Fore, Back, Style
from time import sleep as sl

init()

def mensagem(msg, cor=Fore.MAGENTA):
    print(cor, '~' * len(msg))
    print(f' {msg}', cor)
    print(cor, '~' * len(msg))


def mostrarHelp(comando):
    """
    param n -> jfj
    """

    
    if comando == 'help':
        mensagem('ENTRANDO NO MODO DE HELPY')
        sl(0.45)
        help()

        mensagem('SAINDO DO PROGRAMA...')
        sl(0.45)
        mensagem('VOCE SAIU DO PROGRAMA! VOLTE SEMPRE')
        ex()
    

    elif comando == 'FIM'.lower():
        mensagem('SAINDO DO PROGRAMA...')
        sl(0.45)
        mensagem('VOCE SAIU DO PROGRAMA! VOLTE SEMPRE')
        ex()

    return comando

mostrarHelp(comando = input('Digite entre FIM ou help: ').lower().strip())
