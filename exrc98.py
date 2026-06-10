"""
Crie uma função chamada analisar_notas que:

Recebe uma lista de notas como parâmetro (não usa input)
Usa for pra percorrer a lista
Retorna um dicionário com:

"maior" → a maior nota
"menor" → a menor nota
"media" → a média das notas


Chama a função com a lista [7.5, 4.0, 9.2, 6.8, 3.5, 8.1] e printa o resultado



def analisar_notas(notas):

    media = sum(notas) / len(notas)
    return {"maior":  max(notas), "menor": min(notas), "media": media}
    
lista_notas = analisar_notas([7.5, 4.0, 9.2, 6.8, 3.5, 8.1])
print(lista_notas)
"""

def analisar_notas(notas):
   
   soma = 0
   maior = notas[0]
   menor = notas[0]


   for n in notas:
      soma += n

      
      if n > maior:
         maior = n
      if n < menor:
         menor = n
   media = soma / len(notas)
   return {"maior":  maior, "menor": menor, "media": media}
    
    
lista_notas = analisar_notas([7.5, 4.0, 9.2, 6.8, 3.5, 8.1])
print(lista_notas)
        