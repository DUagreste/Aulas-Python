"""Listas: coleção ordenada, mutável e que permite duplicar
Tuplas: coleção ordenada, imutável e que permite duplicar
Dicionários: coleção desordenada, mutável e que não permite duplicar
"""

# não tem index
# chave:valor
dicio = {"nome": "Vitor", "idade": "24", "cidade": "Mossoró"}

print(dicio)

dicionario = {
    "time": "Spurs",
    "nacional": "Brasil",
    "teste": True
}
print(dicionario['time'])
print(dicionario.get("teste"))
print(dicionario.keys())
print(len(dicionario))
print(dicionario.values())

if "teste" in dicionario:
    print("Essa chave existe!")
else:
    print("Nunca nem vi!")

print(dicionario.items())
