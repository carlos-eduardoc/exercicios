"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro chamado show,
 que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

"""
def line():
   print('-' * 13)

def factorial(num, show=False):
    """
    -> Calcular o fatorial de um numero: 
    :param num -> Ele é responsavel por receber o numero base para o calculo.
    :param show -> Ele é responsavel por mostrar ou nao o calculo
    :return -> Retorna o resultado
    """

    resultado = 1
    
    print('Processo: ')
    line()

    for n in range(num, 0, -1):
        atual = resultado

        resultado *= n

        if show:
          print(f'{atual} x {n} = {resultado}')
    line()


    return resultado



factorial(5, True)
