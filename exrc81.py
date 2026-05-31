"""
Você tem essa lista:
pythonnomes = ["Carlos", "Ana", "Bruno", "Diana"]
Adicione "Eduardo" no final, adicione "Alice" na posição 0, e imprima a lista em ordem inversa.
Resultado esperado:
["Eduardo", "Diana", "Carlos", "Bruno", "Ana", "Alice"]
"""

nomes = ['Carlos', 'Ana', 'Bruno', 'Diana']

nomes.append('Eduardo')
nomes.insert(0, 'Alice')
nomes.reverse()
print(nomes)