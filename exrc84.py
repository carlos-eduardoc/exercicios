"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
 de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo 
 por extenso.
"""

contagem = [
    ('zero', 0),
    ('um', 1),
    ('dois', 2),
    ('tres', 3),
    ('quatro', 4),
    ('cinco', 5),
    ('seis', 6),
    ('sete', 7),
    ('oito', 8),
    ('nove', 9),
    ('dez', 10),
    ('onze', 11),
    ('doze', 12),
    ('treze', 13),
    ('quatorze', 14),
    ('quinze', 15),
    ('dezesseis', 16),
    ('dezessete', 17),
    ('dezoito', 18),
    ('dezenove', 19),
    ('vinte', 20)
]

i = 0

print('-=' * 5 + 'digite um numero de 0 até 20, e veja ele por extenso!')
num = int(input('Digite um numero de 0 até 20!'))

while i < len(contagem):
  extenso, numero = contagem[i]

  if num == numero:
     print(f'Seu numero escolhido foi {num}, e por extenso {extenso}')
  i += 1

  