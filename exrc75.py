"""
Você vai juntar tudo que aprendeu: tupla, lista, for, while e desempacotamento.
pythonalunos = [
    ('Carlos', 7.5),
    ('Ana', 9.2),
    ('Bruno', 5.8),
    ('Lea', 8.1)
]
Com while, percorra a lista e imprima só os alunos com nota maior ou igual a 7, assim:
Carlos — Aprovado (7.5)
Ana — Aprovado (9.2)
Lea — Aprovado (8.1)
"""

alunos = [
    ('Carlos', 7.5),
    ('Ana', 9.2),
    ('Bruno', 5.8),
    ('Lea', 8.1)
]

i = 0
while i < len(alunos):
   nome, nota = alunos[i]

   if nota >= 7:
      print(f'Nome: {nome} | Aprovado no Nota: {nota} ')

   i += 1

