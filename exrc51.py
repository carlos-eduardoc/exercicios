""""
Faça um programa que leia uma frase digitada pelo usuário e conte quantas vogais ela possui.
 Deve funcionar com letras maiúsculas e minúsculas.
Digite uma frase: Python é incrível Vogais encontradas: 6
"""

frase = str(input('Digite uma frase: ')).lower().strip()
vogal = 0

for letra in frase:
    
    if letra in ['a', 'e', 'i', 'o', 'u']:
        vogal += 1
    
print(f'A frase: {frase} tem {vogal} vogais')