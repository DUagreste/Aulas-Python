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
print(dicionario.keys())  # exibe todas as chaves
print(len(dicionario))  # exibi e o tamanho do dicionário
print(dicionario.values())  # exibe todos os valores

if "teste" in dicionario:
    print("Essa chave existe!")
else:
    print("Nunca nem vi!")

print(dicionario.items())   # exibi os itens do dicionário em tuplas/listas

print(50*"-")

dados = {
    "ano": 1997,
    "carro": "polo",
    "cachorro": "yang"
}
print(dados)

dados.update({"ano": 2022})  # atualiza o valor de uma chave
print(dados)

dados.update({"estado": "RN"})  # caso a chave não exista, será acrescentada
print(dados)

dados2 = dict(dados)  # copia & cola um dicionário
print(dados2)

dados.popitem()  # elimina o último item do dicionário
print(dados)

dados.pop("carro")  # elimina a chave solicitada
print(dados)

del dados["cachorro"]  # também elemina a chave solicitada
print(dados)

dados.clear()  # apaga todos os itens
print(dados)

print(50*"-")

tupla = ("item1", "item2", "item3")
dic = dict.fromkeys(tupla)
print(dic)  # copia uma tupla e adiciona a cópia em um dicionário
