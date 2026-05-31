"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER


"""
from datetime import datetime
ano_nascimento = int(input('Em que ano voce nasceu: '))

if ano_nascimento:
   ano_atual = datetime.now().year
   idade = ano_atual - ano_nascimento

   if idade <= 9:
       print('Sua categoria na natação é MIRIM')
   elif idade <= 14:
       print('Sua categoria na natação é INFANTIL')
   elif idade <= 19:
       print('Sua categoria na natação é JUNIOR')
   elif idade <= 25:
       print('Sua categoria na natação é SENIOR')
   elif idade > 25:
       print('Sua categoria na natação é MASTER')

else:
    print('Digite o ano de nascimento')