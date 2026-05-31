"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo 
de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

comp_a = float(input('Digite o comprimento A: '))
comp_b = float(input('Digite o comprimento B: '))
comp_c = float(input('Digite o comprimento C: '))

if comp_a + comp_b > comp_c and comp_a + comp_c > comp_b and comp_b + comp_c > comp_a:
    equi = comp_a == comp_b and comp_a == comp_c
    isoc = comp_a == comp_b and comp_a != comp_c
    escl = comp_a != comp_b and comp_a != comp_c

    if equi:
      print('Seus comprimentos formam um triângulo e EQUILATERO')
    elif isoc:
       print('Seus comprimentos formam um triângulo e ISOCELES')
    elif escl:
       print('Seus comprimentos formam um triângulo e ESCALENO')
else:
    print('Seus comprimentos nao formam um triângulo')