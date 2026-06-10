"""
Crie uma função chamada media_turma que:

Usa um for com range() pra pedir as notas de 5 alunos via input()
Calcula a média das notas
Retorna "Turma aprovada" se a média for maior ou igual a 6, ou "Turma reprovada" se for menor
Printa o resultado
"""

def media_turma():
    
    notas = []
    for n in range(1, 6):
        nota = float(input('Digite uma nota: '))
        notas.append(nota)

    media = sum(notas) / len(notas)
    if media >= 6:
        return f'Turma aprovada, com a media {media:.2f}'
    else:
        return f'Turma reprovada, com a media {media:.2f}'
    
resultado = media_turma()
print(resultado)