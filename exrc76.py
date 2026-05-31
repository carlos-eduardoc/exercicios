"""
estoque = [
    ('arroz', 50),
    ('feijao', 0),
    ('macarrao', 12),
    ('azeite', 0),
    ('sal', 30)
]
Com for, percorra o estoque e imprima só os produtos com quantidade zero, assim:
feijao — SEM ESTOQUE
azeite — SEM ESTOQUE
"""

estoque = [
    ('arroz', 50),
    ('feijao', 0),
    ('macarrao', 12),
    ('azeite', 0),
    ('sal', 30)
]

for p, e in estoque:

    if e == 0:
        print(f'{p} -- SEM ESTOQUE')