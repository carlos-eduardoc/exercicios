"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o 
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

"""

print("-" * 10)



print('Escolha sua opcão: 1- para binario, 2- para octal e 3- para hexadecimal e tambem digite seu numero')
escolha = int(input('Escolha uma opção: '))
numero = int(input('Digite seu numero inteiro para conversao: '))

if escolha in [1, 2, 3]:
  if escolha == 1:
     conversao_bin = bin(numero)
     print(f'Seu numero {numero}, convertido para binario é {conversao_bin}')


  elif escolha == 2:
     conversao_oct = oct(numero)
     print(f'Seu numero {numero}, convertido para octal é {conversao_oct}')

  elif escolha == 3:
     conversao_hex = hex(numero)
     print(f'Seu numero {numero}, convertido para hexadecimal é {conversao_hex}')

else:
     print('Opção invalida!')

print("-" * 10)
