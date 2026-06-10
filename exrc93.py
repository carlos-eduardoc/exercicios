"""
Inverter um dicionário
Você tem este dicionário:
pythonplacas = {
    "ABC-1234": "Carlos",
    "DEF-5678": "Ana",
    "GHI-9012": "Bruno",
}
Tarefa: Crie um novo dicionário invertido onde as chaves viram valores e os valores viram chaves:
python# resultado esperado
{
    "Carlos": "ABC-1234",
    "Ana": "DEF-5678",
    "Bruno": "GHI-9012",
}
Dica: você vai precisar de um dicionário vazio e um for. 
"""

placas = {
    "ABC-1234": "Carlos",
    "DEF-5678": "Ana",
    "GHI-9012": "Bruno",
}

placas_inv = {

}

for c, v in placas.items():
   placas_inv[v] = c

   print(f'{v} -> {c}')