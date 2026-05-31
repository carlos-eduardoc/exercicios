"""
Faça um programa que leia N números digitados pelo usuário (ele define quantos)
 e ao final mostre qual foi o maior e qual foi o menor número digitado.
Quantos números? 5 Digite: 8 → Digite: 3 → Digite: 15 → Digite: 1 → 
Digite: 9 Maior: 15 | Menor: 1
"""
maior = None
menor = None


qntd_num = int(input('Quantos numeros vao ser digitados: '))

for n in range(qntd_num):
   digi = int(input('Digite: '))
   
   if maior is None or digi > maior:
      maior = digi
    
   elif menor is None or digi < menor:
      menor = digi

print(f'O numero {maior} é o maior')
print(f'O numero {menor} é o menor')
      
