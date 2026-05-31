"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

"""
valores = (int(input('Digite um valor: ')),
         int(input('Digite um outro valor: ')),
         int(input('Digite um outro valor: ')),
         int(input('Digite um outro valor:  ')))


print('-=' * 10)

print('Os valores digitados foram: ')
for valor in valores:
   print(valor, end=' ')


print(f'\nO numero 9 apareceu {valores.count(9)}')
if 3 in valores:
    print(f'O numero 3 aparece pela primeira vez na posição {valores.index(3) + 1} ')
 
for p in valores:
  if p % 2 == 0: 
    print(f'Os numeros pares foram: {p}')
    

print('-=' * 10)