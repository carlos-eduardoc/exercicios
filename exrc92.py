"""
Construindo um dicionário com while
Você vai criar um sistema de cadastro simples. O programa pergunta o nome e a nota de um aluno, e vai guardando num dicionário.
Para quando o usuário digitar "fim".
Exemplo de uso:
Nome do aluno (ou 'fim' para encerrar): Ana
Nota da Ana: 8.5
Nome do aluno (ou 'fim' para encerrar): Bruno
Nota do Bruno: 6.0
Nome do aluno (ou 'fim' para encerrar): fim

Alunos cadastrados:
Ana -> 8.5
Bruno -> 6.0
Dica: começa pensando em como criar um dicionário vazio antes do while
"""

from time import sleep as sl
from sys import exit

alunos = {}

while True:
    aluno = str(input('Nome do Aluno (ou fim para encerrar o programa): ')).strip()
    
    if aluno.lower() == "fim":

        print('Finalizando o programa...')
        sl(0.55)
        exit()
    
    nota = float(input(f'Nota de {aluno}: '))
    alunos[aluno] = nota
    
    print('Alunos cadastrados: ')
    for aluno, nota in alunos.items():
       print(f'Nome: {aluno} -> {nota}')


    
