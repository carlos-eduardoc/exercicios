"""
Escreva um programa para aprovar o empréstimo 
bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""


valor_casa = float(input('Valor dessa casa: '))
salario = float(input('Qual seu salario: '))
qntd_anos = int(input('Em quantos anos você vai pagar: '))

if valor_casa / (qntd_anos * 12) > (salario / 100 * 30):
    print('Seu emprestimo foi negado! por ultrapassar 30% do seu salario')
else:
    print('Seu emprestimo foi aprovado!')