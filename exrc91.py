"""
Agora complica um pouco. Você vai trabalhar com um dicionário dentro de outro dicionário — chamamos isso de dicionário aninhado.
pythonfuncionarios = {
    "Ana":    {"cargo": "dev", "salario": 8000},
    "Bruno":  {"cargo": "design", "salario": 5500},
    "Carla":  {"cargo": "dev", "salario": 9200},
    "Diego":  {"cargo": "rh", "salario": 4800},
    "Elena":  {"cargo": "dev", "salario": 7600},
}
Tarefa:

Usando for, calcule e imprima a média salarial de todos os funcionários
Imprima apenas os devs com salário acima da média
Imprima o nome do funcionário com o maior salário de toda a empresa
"""



funcionarios = {
    "Ana":    {"cargo": "dev", "salario": 8000},
    "Bruno":  {"cargo": "design", "salario": 5500},
    "Carla":  {"cargo": "dev", "salario": 9200},
    "Diego":  {"cargo": "rh", "salario": 4800},
    "Elena":  {"cargo": "dev", "salario": 7600},
}

soma = 0
maior = max(funcionarios, key=lambda chave: funcionarios[chave]["salario"])


for n, d in funcionarios.items():
    print(f'{n}: {d["salario"]}')
    soma += d["salario"]

    
media = soma / len(funcionarios)
print(f'A media de todos os salarios são: {media}')

for n, d in funcionarios.items():
    if d["salario"] > media    :
        print(f'O ou A {n}, tem um salario acima da media de {media} com R${d["salario"]}')


print(f'{maior} tem o maior salario da empresa {funcionarios[maior]["salario"]}')
    