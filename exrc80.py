"""
Você tem essa lista:
pythonnumeros = [5, 2, 8, 1, 9, 3]
Remova o número 8, ordene a lista e imprima o resultado.
Resultado esperado:
[1, 2, 3, 5, 9]
"""

nums = [5, 2, 8, 1, 9, 3]

nums.remove(8)
nums.sort()
print(nums)