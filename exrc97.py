"""
Crie uma função chamada validar_senha que:

Pede uma senha via input()
Usa while pra continuar pedindo enquanto a senha não tiver pelo menos 8 caracteres
Quando a senha for válida, retorna "Senha aceita"
Printa o resultado
"""

def validar_senha():
    senha = input('Digite uma senha de letras: ')
    
    while len(senha) < 8:
        print('8 CARACTERES')
        senha = input('Digite uma senha de letras de 8 caracteres: ')
    return 'Senha aceita'
    
resultado = validar_senha()
print(resultado)
