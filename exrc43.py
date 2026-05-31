"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""
print('-' * 5 + 'CALCULADORA DE IMC' + '-' * 5)

peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em M: '))
imc = peso / (altura ** 2)


if imc < 18.5:
       print(f'Seu imc é {imc:.2f} e o reultado é de ABAIXO DO PESO')
elif imc < 25:
       print(f'Seu imc é {imc:.2f} e o resultado é de PESO IDEAL')
elif imc < 30:
       print(f'Seu imc é {imc:.2f} e o é de SOBREPESO')
elif imc < 40:
       print(f'Seu imc é {imc:.2f} e o resultado é de OBESIDADE')
else:
       print(f'Seu imc é {imc:.2f} e o resultado é de OBESIDADE MORBIDA')

print('-' * 18)
