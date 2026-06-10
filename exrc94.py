"""
sistema de notas completo
turma = {}
Tarefa:

Use while para cadastrar alunos com nome e lista de 3 notas
Para cada aluno calcule a média e guarde tudo no dicionário
No final exiba todos os alunos com suas notas e média
Mostre quem foi aprovado (média ≥ 7) e quem foi reprovado

Exemplo de saída:
=== Resultados ===
Ana -> notas: [8.0, 7.5, 9.0] | média: 8.17 | APROVADO
Bruno -> notas: [5.0, 6.0, 4.5] | média: 5.17 | REPROVADO
Dica: cada aluno vai ter como valor um dicionário com "notas" e "media". 
"""

from sys import exit
from time import sleep as sl

turma = {}

while True:

    nome = str(input('Nome do aluno: <')).strip()

    if nome == 'fim':
        print('encerrando...')
        sl(0.75)
        exit()

    nota1 = float(input(f'Digite a 1º nota de {nome}: '))
    nota2 = float(input(f'Digite a 2º nota de {nome}: '))
    nota3 = float(input(f'Digite a 3º nota de {nome}: '))

    turma[nome] = {"notas": [nota1, nota2, nota3]}
    
    for n, nota in turma.items():
        soma =  sum(nota["notas"])
        media = soma / len(nota["notas"])

        if media >= 7:
            status = 'APROVADO'
        else:
            status = 'REPROVADO'
    
        print(f'{n} -> notas: {nota["notas"]} | media: {media:.2f} | {status} ')