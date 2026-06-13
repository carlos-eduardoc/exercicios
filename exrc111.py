# Guanabara pediu para escrever esse code:

def fatorial(n):

    f = 1
    for c in range(n, 0, -1): # pode ser tambem (1, n+1)
        f *= c

    return f


num = int(input('Digite um numero: '))
fat = fatorial(num)
print(f'O fatorial do numero {num} é {fat}')