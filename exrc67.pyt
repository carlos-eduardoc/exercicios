"""
Um jogo de adivinhação, clássico de quem tá aprendendo lógica.
Sua missão: Escreva um programa que:

Define um número secreto: numero_secreto = 42
Fica pedindo pro usuário adivinhar com input()
Se o chute for menor que o secreto, imprime "Muito baixo!"
Se for maior, imprime "Muito alto!"
Se acertar, imprime "Acertou!" e para
Converte o input pra inteiro com int()
"""

numero_secreto = 42
chute_dg = None

while chute_dg != numero_secreto:
    chute = int(input('Advinhe o numero: '))
    chute_dg = chute

    if chute_dg < numero_secreto:
      print('Muito baixo')

    elif chute_dg > numero_secreto:
       print('Muito alto')

print(f'Aceeertoo! o numero era {numero_secreto}')