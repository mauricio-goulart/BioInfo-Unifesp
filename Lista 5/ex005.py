"""
Created on Tue Aug 27 19:05:10 2024

Escreva um programa para agrupar uma lista de dicionários por
uma chave específica

@author: mauricio
"""

############################################################

pessoas = [{"Nome" : "Mauricio", "Idade" : 19, "Cidade" : "São José dos Campos"},
           {"Nome" : "Maria", "Idade" : 17, "Cidade" : "Rio de Janeiro"},
           {"Nome" : "Rodrigo", "Idade" : 18, "Cidade" : "São José dos Campos"},
           {"Nome" : "Mauricio2", "Idade" : 19, "Cidade" : "Rio de Janeiro"}]


chave = "Cidade"

resultado = {}
lista = []

for dicionario in pessoas:
    valor_da_chave = dicionario[chave]
    
    if valor_da_chave not in resultado:
        resultado[valor_da_chave] = []
    
        resultado[valor_da_chave].append(dicionario)


############################################################

