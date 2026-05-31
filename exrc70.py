"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))

print('MENU: \n [1] somar \n [2] multiplicar \n [3] maior \n [4] novos numeros \n [5] sair do programa')

while True:
 opcao = int(input('Digite uma das opções: '))


 if opcao == 1:
    soma = n1 + n2 
    print(f'O resultado na sua soma é {soma}')

 elif opcao == 2:
    mult = n1 * n2
    print(f'O resultado da multiplicação é {mult}')

 elif opcao == 3:
   if n1 > n2:
     print(f'O numero {n1} é o maior!')
   else:
     print(f'O numero {n2} é o maior!')

 elif opcao == 4:
   n1 = int(input('Digite um novo numero: '))
   n2 = int(input('Digite um novo numero: '))

 elif opcao == 5:
   print('Programa finalizado...')
   break
 
 else:
   print('Opção invalida..')