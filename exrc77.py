"""
times = [
    ('Flamengo', 78),
    ('Palmeiras', 72),
    ('Gremio', 60),
    ('Corinthians', 55),
    ('Santos', 48)
]
Com while, percorra a lista e imprima só os times com mais de 60 pontos, assim:
Flamengo: 78 pts
Palmeiras: 72 pts
"""

times = [
    ('Flamengo', 78),
    ('Palmeiras', 72),
    ('Gremio', 60),
    ('Corinthians', 55),
    ('Santos', 48)
]

i = 0

while i < len(times):

    time, pontos = times[i]

    if pontos > 60:
        print(f'{time}: {pontos} pontos')

    i += 1