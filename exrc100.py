"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
 (largura e comprimento) e mostre a área do terreno.


"""

def area(largura, comprimento):
    
    area_terreno = largura / comprimento
    print(f'Largura: {largura} | Comprimento: {comprimento} | Area: {area_terreno:.3f}')


area(largura = float(input('Passe a largura do terreno: ')), comprimento = float(input('Passe o comprimento do terreno: ')))