"""
Created on Tue Aug 27 19:21:52 2024

Escreva um programa para verificar se uma chave específica existe
no dicionário ou não.

@author: mauricio
"""

############################################################

chave = "altura"
pessoas = {"nome" : "Mauricio", "idade" : 19, "Ra" : 169024}
listak = list(pessoas.keys())

    
    
if chave in pessoas:
    print("Existe")
    
else:
    print("Não existe")

############################################################

