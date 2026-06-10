"""
functions

Crie uma função chamada calcular_imc que:

Recebe dois parâmetros: peso (em kg) e altura (em metros)
Calcula o IMC com a fórmula: imc = peso / (altura ** 2)
Retorna uma string com a classificação:

IMC < 18.5 → "Abaixo do peso"
18.5 ≤ IMC < 25 → "Peso normal"
25 ≤ IMC < 30 → "Sobrepeso"
IMC ≥ 30 → "Obesidade"



Depois chame a função com pelo menos 3 valores diferentes e imprima o resultado de cada um.

"""


def calcular_imc(peso, altura):
   
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return "abaixo do peso"
    elif 18.5 <= imc < 25:
        return "peso normal"
    elif 25 <= imc < 30:
        return "sobre peso"
    else:
        return "obesidade"
    




resultado = calcular_imc(peso = float(input('Digite seu peso em kg: ')), altura = float(input('Digite a altura em metros(1.60): ')))
print(resultado)