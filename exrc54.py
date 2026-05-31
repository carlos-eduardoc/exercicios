"""
Leia N e exiba a contagem de N até 0.

"""
import time
contagem = 10

for n in range(contagem, -1, -1):
    contagem -= n
    print(n)
    time.sleep(1)