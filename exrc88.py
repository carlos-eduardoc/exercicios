"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ('lapis', 6.50,
            'caderno', 20.55,
            'borracha', 3.50,
            'apagador', 10.00,
            'apontador', 5.50)


print(f"{'Produtos':<12}  | {'Preço':>5}")
print('-' * 20)

for i in range(0, len(listagem), 2):
    print('-' * 20)
    print(f' { listagem[i]:<12} | {listagem[i+1]:>6.2f}') 