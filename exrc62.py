"""
Leia N números e exiba a soma dos positivos e a soma dos negativos separadamente. 
Se não houver nenhum positivo ou nenhum negativo, avise o usuário.
"""
n = int(input('Quantos numeros: '))

soma_p = 0
soma_n = 0
pos = 0
neg = 0

for i in range(n):
    num = int(input('Digite um numero: '))
    
    if num > 0:
        soma_p += num
        pos += 1

    elif num < 0:
        soma_n += num
        neg += 1

if pos == 0 and neg == 0:
    print('Digite numeros positivos e negativos')

else:
   print('-' * 25)
   print(f'A soma entre os positivos é {soma_p}')
   print(f'A soma entre os negativos é {soma_n}')
   print('-' * 25)
