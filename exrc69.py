"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
 palpites foram necessários para vencer.


"""
from random import randint as rndt

maquina = rndt(1, 11)
palpite_jog = int(input('Adivinhe o numero de 1 a 10: '))
palpites = 0

while palpite_jog != maquina:
    palpite_jog = int(input('Adivinhe o numero de 1 a 10: '))
    palpites += 1

print(f'Voce acertou  o numero era {maquina}, voce acertou em {palpites + 1} palpites!')