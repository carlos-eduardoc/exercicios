"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""

palavras = 'banana', 'leao', 'pirulito', 'limao', 'morango', 'chiclete', 'abacate', 'flor'


for p in palavras:
    vogais = ''
    for l in p:
      
      if l in ['a', 'e', 'i', 'o', 'u']:
        vogais += l

    print(f'Palavra: {p} | Vogais: {', '.join(vogais)}')
