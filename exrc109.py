"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:

– Quantidade de notas             – A maior nota                 – A menor nota   – A média da turma      – A situação (opcional)


"""

def notas(* notas, situacao='nao tem'):
    tamanho = len(notas)
    maior = notas[0]
    menor = notas[0]
    soma = 0

    for nota in notas:

        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        soma += nota

        media = soma / tamanho

        estatisca = {"quantidade de notas": tamanho,
                  "maior nota": maior,
                  "menor nota": menor,
                  "media da turma": media,
                  "situacao": situacao
                }

    
    return estatisca
    
r1 = notas(8.0, 9.0, 7.0, 2.0, 10.0, 10.0, 10.0, 21.0, 1.0, situacao = str(input('Digite a situação: ')))

print('Estatisca:')
for chave, valor in r1.items():
    print(f'{chave}: {valor} ')
