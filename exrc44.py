"""
Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros



"""
import time 

print('-' * 5 + 'CAIXA ELETRONICO' + '-' * 5)

valor = float(input('Digite o valor do produto: '))
print('Carregando sistema...')
time.sleep(0.75)

if valor:
    print('Escolha a forma de pagamento entre dinheiro e cartao')
    forma = str(input('Digite a sua forma: ')).strip()

    if forma.lower() == 'cartao':
       deb_or_cre = str(input('Debito ou credito: '))

       if deb_or_cre.lower() == 'debito':
           desc_vista = valor - (valor / 100 * 5)
           print(f'O valor de seu produto é R${valor:.2f} e com desconto aplicado de 5% R${desc_vista:.2f}')

       elif deb_or_cre.lower() == 'credito':
           parcelame = int(input('Escolha em quantas vezes parcelar entre 2 e 3 ou mais: '))
           if parcelame == 2: 
               valor_parc = valor / 2
               print(f'O valor parcelad por 2 é de {valor_parc:.2f}')
           elif parcelame >= 3:
               valor_parc_3 = valor * 1.20
               total = valor_parc_3 / parcelame
            
               print(f'O valor parcelado por {parcelame}, é {total}')
           else:
               print('Digite a quantidade de parcelas')
       else:
           print('Digite entre credito e debito')

    elif forma.lower() == 'dinheiro':
        desc_dinh = valor - (valor / 100 * 10)
        print(f'O valor final do produto em dinheiro é {desc_dinh}')

    else:
        print('Opção invalida')
else:
    print('Digite um valor')