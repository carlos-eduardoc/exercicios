estoque = {
    "arroz": 50,
    "feijão": 30,
    "macarrão": 20,
    "azeite": 5,
    "sal": 100
}

soma = sum(estoque.values())
for produto, quantidade in estoque.items():

    if quantidade < 25:
        print(f'{produto} esta faltando estoque, tendo {quantidade} unidades')
print(f'O total de produtos em estoque -> {soma}')