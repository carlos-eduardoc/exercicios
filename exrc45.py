"""
Crie um programa que faça o computador jogar Jokenpô com você
"""

import random
from time import sleep

opcoes = {1:'pedra', 
          2:'papel',
          3:'tesoura'
          }

print('-----JOGO DE JOKENPO-----')


print('Digite umas das seguintes opções: 1-Pedra, 2- Papel, 3- Tesoura')
escolha = int(input('Digite umas das opcões: '))
jogada = opcoes[escolha]
maquina = random.choice(list(opcoes.values()))

print('Estamos capturando a escolha da maquina...')
sleep(0.75)


 
if escolha in opcoes:
   print(f'Sua escolha: {jogada} | Escolha da maquina: {maquina}')

   if jogada == 'pedra' and maquina == 'papel':
      print('Eu ganhei! papel ganha da pedra')
   elif jogada == 'papel' and maquina == 'pedra':
      print('Voce ganhou de mim! papel ganha da pedra')
   elif jogada == 'tesoura' and maquina == 'papel':
      print('Voce ganhou de mim! tesoura corta papel')
   elif jogada == 'papel' and maquina == 'tesoura':
      print('Eu ganhei! tesoura corta papel')
   elif jogada == 'tesoura' and maquina == 'pedra':
      print('Eu ganhei! pedra quebra tesoura')
   elif jogada == 'pedra' and maquina == 'tesoura':
      print('Voce ganhou de mim! pedra quebra tesoura')
   else:
      print('Empatamos nesse round! escolhemos as mesma coisas')
else:
   print('Digite uma opção VALIDA')  
 

# Passo a passo
"""
Primeiro apresentar a calculador, apresentar as opçoes, declarar lista e variaveis usar o random.choice, depois usar as condicionais
para expor os resultados
"""