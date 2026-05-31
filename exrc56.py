n = int(input('Quantos numeros: '))

maior = None
menor = None

for i in range(n):
    num = int(input('Digite um numero: '))

    if maior is None or maior < num:
        maior = num
    if menor is None or menor > num:
        menor = num

print(f'O maior numero é {maior} e menor é {menor}')
