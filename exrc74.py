"""
uma lista de produtos onde cada produto é uma tupla (nome, preço):
python produtos = [
    ('arroz', 6.50),
    ('feijão', 8.90),
    ('macarrão', 4.30)
]

Seu desafio: percorra essa lista com for e imprima assim:
Produto: arroz | Preço: R$ 6.5
Produto: feijão | Preço: R$ 8.9
Produto: macarrão | Preço: R$ 4.3
Dica: cada elemento do for vai ser uma tupla — você pode desempaco
tá-la direto no for. 
"""
produtos = [
    ('arroz', 6.50),
    ('feijao', 8.90),
    ('macarrao', 4.30)
]


for p, n in produtos:
    print(f'Produto: {p} | Preço: {n}')

