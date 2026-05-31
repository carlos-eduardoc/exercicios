"""
Um caixa eletrônico libera saques enquanto o saldo for maior que zero.
Sua missão: Escreva um while que:

Começa com saldo = 200
A cada volta do loop, subtrai 50 do saldo
Imprime o saldo atual a cada saque
Quando o saldo chegar a 0, imprime "Saldo esgotado."



"""

saldo = 200

while saldo > 0:
    print(f'Seu saldo atual: {saldo}')
    saldo -= 50

print(f'Saldo esgotado')