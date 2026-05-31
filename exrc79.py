"""
lista= []

lista.append(x)       # adiciona x no final
lista.insert(i, x)    # adiciona x na posição i
lista.extend([x, y])  # junta outra lista no final
lista.remove(x)  # remove a primeira ocorrência de x (erro se não existir)
lista.pop()      # remove e retorna o último item
lista.pop(i)     # remove e retorna o item da posição i
lista.clear()    # apaga tudo
lista.index(x)   # retorna o índice de x (erro se não existir)
lista.count(x)   # quantas vezes x aparece na lista
lista.sort()         # ordena em ordem crescente (modifica a lista)
lista.reverse()      # inverte a ordem (modifica a lista)
sorted(lista)        # retorna uma nova lista ordenada (não modifica)
lista.copy()   # retorna uma cópia independente da lista
"""
frutas = ['maça', 'abacate', 'banana']

frutas.append('melao')
frutas.insert(2, 'uva')
frutas.remove('maça')
frutas.pop()
frutas.pop(2)
# frutas.clear()

frutas.index('uva')
frutas.count('uva')
frutas.reverse()

frutas.sort()
print(frutas)

print(frutas.index('uva'))
print(frutas.count('abacate'))
print(frutas)

