<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="90" alt="Python logo"/>

# 🐍 Exercícios Python — Mundo 2 e Mundo 3

### Prática de lógica, estruturas de dados e funções com base no *Curso em Vídeo* (Gustavo Guanabara)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Exercícios](https://img.shields.io/badge/Exerc%C3%ADcios-70%2B-informational?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-MIT-green?style=for-the-badge)

</div>

---

## 📖 Sobre este repositório

Este repositório reúne os exercícios que venho resolvendo nos **Mundo 2** e **Mundo 3** do curso de Python do *Curso em Vídeo*. Cada arquivo `exrcXX.py` corresponde a um desafio numerado proposto no curso — o número no nome do arquivo é o número do exercício, não a ordem em que aparecem aqui.

O objetivo não é só "fazer o exercício rodar", e sim treinar os pilares que sustentam qualquer programa em Python:

- **Condições** (`if` / `elif` / `else`) para tomar decisões,
- **Funções** para organizar e reutilizar lógica,
- **Estruturas de dados** (listas, tuplas e dicionários) para guardar e manipular informação,
- **Tratamento de erros** para deixar o programa mais robusto,
- **Modularização** para dividir um problema grande em partes menores.

Abaixo eu explico cada um desses pontos com trechos de código reais tirados do próprio repositório.

---

## 🧩 Estruturas condicionais e laços de repetição

A base do Mundo 2: usar `if`/`elif`/`else` combinados com `for`/`while` para controlar o fluxo do programa. Exemplo do `exrc60.py`, que soma apenas os números pares digitados pelo usuário:

```python
n = int(input('Quantos numeros: '))
soma_par = 0

for i in range(n):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma_par += num

print(f'A soma dos numeros pares é de {soma_par}')
```

Aqui o `for` controla **quantas vezes** o programa repete a leitura, e o `if` dentro do laço decide **o que fazer** com cada valor lido. Esse padrão (repetir + decidir) aparece na maioria dos exercícios do Mundo 2.

---

## 🗂️ Estruturas de dados (listas, tuplas e dicionários)

No Mundo 3 o foco passa a ser guardar e organizar dados de forma mais elaborada do que uma única variável.

**Listas** — manipulação direta com métodos prontos (`exrc80.py`):

```python
nums = [5, 2, 8, 1, 9, 3]
nums.remove(8)
nums.sort()
print(nums)  # [1, 2, 3, 5, 9]
```

**Dicionários aninhados** — usados quando cada registro precisa de vários campos, como em um sistema de notas (`exrc94.py`):

```python
turma = {}
turma[nome] = {"notas": [nota1, nota2, nota3]}

for n, nota in turma.items():
    media = sum(nota["notas"]) / len(nota["notas"])
    status = 'APROVADO' if media >= 7 else 'REPROVADO'
    print(f'{n} -> notas: {nota["notas"]} | media: {media:.2f} | {status}')
```

O dicionário funciona aqui como um "mini banco de dados" em memória: a chave é o nome do aluno, e o valor é outro dicionário com as notas dele.

---

## 🔧 Funções

Funções aparecem para evitar repetição de código e para dar nome a uma operação específica. Exemplo clássico do `exrc111.py`, o cálculo de fatorial:

```python
def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

num = int(input('Digite um numero: '))
fat = fatorial(num)
print(f'O fatorial do numero {num} é {fat}')
```

Outro exemplo mais avançado é o uso de **argumentos variáveis** (`*args`) e **valor padrão de parâmetro**, no `exrc109.py`:

```python
def notas(*notas, situacao='nao tem'):
    tamanho = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / tamanho
    return {
        "quantidade de notas": tamanho,
        "maior nota": maior,
        "menor nota": menor,
        "media da turma": media,
        "situacao": situacao
    }
```

Com `*notas`, a função aceita **qualquer quantidade** de notas na chamada, e `situacao='nao tem'` garante que o parâmetro seja opcional.

---

## 🧱 Modularização

Modularizar é dividir um problema grande em várias funções pequenas, cada uma com uma responsabilidade única — e depois combiná-las. O `exrc99.py` (uma calculadora de gastos mensais) é o exemplo mais claro disso no repositório:

```python
def adicionar_gastos(produtos, nome, valor):
    produtos.append({"nome": nome, "valor": valor})
    return produtos

def total_gasto(produtos):
    return sum(item["valor"] for item in produtos)

def gasto_maior(produtos):
    maior = max(produtos, key=lambda item: item["valor"])
    return maior["valor"], maior["nome"]

def relatorio(produtos):
    total = total_gasto(produtos)
    maior_gasto = gasto_maior(produtos)
    print(f'=== Relatório ===\nTotal: R${total:.2f}\nMaior gasto: {maior_gasto}')
```

Nenhuma função sozinha resolve o problema todo. `relatorio()` só funciona porque **chama** `total_gasto()` e `gasto_maior()` — esse encadeamento é a essência da modularização.

---

## 🛡️ Tratamento de erros

Um programa robusto não pode quebrar quando o usuário digita algo inesperado (uma letra no lugar de um número, uma divisão por zero, etc.). Esse cuidado é trabalhado nos exercícios finais do Mundo 3 usando `try`/`except`, seguindo o padrão abaixo:

```python
while True:
    try:
        valor = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Erro: digite apenas números inteiros.')
        continue
    else:
        print(f'Você digitou {valor} com sucesso!')
        break
```

A ideia central: `try` executa o código que **pode falhar**, `except` captura o erro específico (aqui, `ValueError`, disparado quando o `input` não é um número) e `else` roda somente se **não** houve erro. Isso evita que o programa feche abruptamente por um erro de digitação do usuário.

---

## ▶️ Como executar

Pré-requisito: **Python 3** instalado ([python.org](https://www.python.org/downloads/)).

```bash
# 1. Clone o repositório
git clone https://github.com/carlos-eduardoc/exercicios.git
cd exercicios

# 2. Rode o exercício que quiser
python exrc99.py
```

Cada arquivo é independente — não é necessário rodar em nenhuma ordem específica.

---

## 📁 Estrutura do repositório

```
exercicios/
├── exrc36.py   ... exrc66.py    → Mundo 2: condicionais, laços, validação de entrada
├── exrc67.py   ... exrc111.py   → Mundo 3: listas, tuplas, dicionários, funções, tratamento de erros
└── __init__.py
```

> A numeração dos arquivos segue a numeração oficial dos exercícios do curso — por isso não é sequencial de 1 em 1 dentro deste repositório.

---

## 👨‍💻 Autor

**Carlos Eduardo**
Estudando Python com foco em segurança ofensiva (OffSec).

[![GitHub](https://img.shields.io/badge/GitHub-carlos--eduardoc-181717?style=for-the-badge&logo=github)](https://github.com/carlos-eduardoc)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Carlos%20Eduardo-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carloseduardo-dev/)
