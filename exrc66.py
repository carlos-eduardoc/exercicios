"""
O mesmo sistema de login, mas agora com limite de tentativas (igual a qualquer app de banco).
Sua missão: Escreva um programa que:

Permite no máximo 3 tentativas de senha
Se acertar antes disso, imprime "Acesso liberado!" e para
Se errar as 3, imprime "Conta bloqueada." e para
A cada tentativa errada, mostra quantas tentativas restam

Dica: você vai precisar de um contador de tentativas. Pensa em como a con
dição do while vai precisar verificar duas coisas ao mesmo tempo — a senha e o número de tentativas.
"""
from time import sleep as sl
senha_correta = 'python123'

tentativas = 0

while tentativas < 3:

    senha_user = str(input('Digite a sua senha: '))
    tentativas += 1

    if senha_user != senha_correta:
        print('Senha Incorreta')


    else:
      print('Acesso LIberado')
      break

if tentativas == 3 and senha_user != senha_correta:
  for n in range(3):
    print(f'...{n + 1}...')
    sl(1.0)
  print('Sua conta foi bloqueada')

