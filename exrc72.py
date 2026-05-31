# tuplas

"""
Crie uma tupla chamada cores com 3 cores que você gostar. Depois, 
use um for para imprimir cada cor com a mensagem "Cor: X" — onde X é a cor da vez.
"""

#cores = 'preto', 'branco', 'verde'

#for cor in cores:
  #  print(f'Cor: {cor}')

cores = 'preto', 'branco', 'verde'
i = 0

while i < len(cores):
    print(f'Cor: {cores[i]}')
    i += 1