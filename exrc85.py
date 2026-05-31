"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro 
de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""

times = ('palmeiras', 'flamengo', 'fluminense', 'atletico-pr', 
         'bragantino', 'coritiba', 'sao paulo', 'bahia', 'cruzeiro', 
         'botafogo', 'vitoria', 'aletico-mg', 'internacional', 'gremio',
         'corinthians', 'vasco da gama', 'santos', 'mirassol', 'remo', 'chapecoense')

for t in times[:5]:
    print(f'OS 5 PRIMEIROS COLOCADOS SÃO: {t}')

for t in times[16:]:
    print(f'NOSSOS LATERNAS SAO: {t}')


ordenada = tuple(sorted(times))
print(f"A classificação em ordem alfabetica é {', '.join(ordenada)}")

print(f"O chapecoense está em {times.index('chapecoense') + 1}")