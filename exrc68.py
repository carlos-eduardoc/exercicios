"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""

sexo = input('Digite seu sexo (M ou F): ').strip().upper()

while sexo not in 'MmFf':
    sexo = input('Opção invalida, Digite novamente entre M e F: ').strip()

print(f'Seu sexo é {sexo}')