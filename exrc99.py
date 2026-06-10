"""
Crie um programa com funções separadas que funcione como uma calculadora de gastos mensais:

adicionar_gasto(lista, nome, valor) — adiciona um dicionário {"nome": nome, "valor": valor} na lista
total_gastos(lista) — percorre a lista com for e retorna a soma de todos os valores
gasto_maior(lista) — retorna o nome do gasto com maior valor
relatorio(lista) — chama as duas funções anteriores e printa um relatório assim:

=== RELATÓRIO DE GASTOS ===
Aluguel: R$ 1200.00
Internet: R$ 120.00
Mercado: R$ 800.00
--------------------------
Total: R$ 2120.00
Maior gasto: Aluguel
Chama adicionar_gasto pelo menos 3 vezes, depois chama relatorio.
"""
produtos = []

def adicionar_gastos(produtos, nome, valor):
    produtos.append({"nome": nome, "valor": valor})

    return produtos

def total_gasto(produtos):
    soma = 0

    for n in produtos:
        soma += n["valor"]
    return soma

def gasto_maior(produtos):
    maior = produtos[0]["valor"]
    maior_nome = produtos[0]["nome"]

    for n in produtos:
        if n["valor"] > maior:
            maior = n["valor"]
            maior_nome = n["nome"]
        
    return maior, maior_nome

def relatorio(produtos):
    total = total_gasto(produtos)
    maior_gasto = gasto_maior(produtos)

    print(f'====Relatorio=== \n {produtos} \n O total gasto foi: {total:.2f} \n O maior gasto foi: R${maior_gasto}')
    
adicionar_gastos(produtos, nome = input('Nome do que foi gasto: '), valor = float(input('Valor do mesmo: ')))
adicionar_gastos(produtos, nome = input('Nome do que foi gasto: '), valor = float(input('Valor do mesmo: ')))
adicionar_gastos(produtos, nome = input('Nome do que foi gasto: '), valor = float(input('Valor do mesmo: ')))

relatorio(produtos)

