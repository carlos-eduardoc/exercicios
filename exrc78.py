"""
um degrau acima
vendas = [
    ('Ana', 3200),
    ('Bruno', 1800),
    ('Carla', 4100),
    ('Diego', 2950),
    ('Eva', 5300)
]
Com for, percorra e imprima todos, mas com uma etiqueta diferente dependendo da venda:

Abaixo de 2000 → ABAIXO DA META
Entre 2000 e 3999 → NA META
4000 ou mais → SUPEROU

Assim:
Ana: R$3200 — NA META
Bruno: R$1800 — ABAIXO DA META
Carla: R$4100 — SUPEROU
Diego: R$2950 — NA META
Eva: R$5300 — SUPEROUvendas = [
    ('Ana', 3200),
    ('Bruno', 1800),
    ('Carla', 4100),
    ('Diego', 2950),
    ('Eva', 5300)
]

for n, v in vendas:

    if v < 2000:
        print(f'{n}: R${v} - ABAIXO DA MEDIA')
    elif v > 2000 and v < 3999:
        print(f'{n}: R${v} - NA META ')
    else:
        print(f'{n}: R${v} - SUPEROU ')

"""

vendas = [
    ('Ana', 3200),
    ('Bruno', 1800),
    ('Carla', 4100),
    ('Diego', 2950),
    ('Eva', 5300)
]

for n, v in vendas:

    if v < 2000:
        print(f'{n}: R${v} - ABAIXO DA MEDIA')
    elif v >= 2000 and v <= 3999:
        print(f'{n}: R${v} - NA META ')
    else:
        print(f'{n}: R${v} - SUPEROU ')
