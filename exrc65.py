"""
Agora vamos adicionar entrada do usuário dentro do while isso é onde o while brilha de verdade.
Contexto: Um sistema de login simples.
Sua missão: Escreva um programa que:

Define senha_correta = "python123"
Fica pedindo a senha com input() enquanto a senha digitada estiver errada
A cada tentativa errada, imprime "Senha incorreta, tente novamente."
Quando acertar, imprime "Acesso liberado!" e para
"""

senha_correta = 'python123'
senha_dig = None

while senha_dig != senha_correta:
    senha_user = str(input('Digite a sua senha: '))
    senha_dig = senha_user

    if senha_dig != senha_correta:
        print('Senha Incorreta')

print('Acesso Liberado!')