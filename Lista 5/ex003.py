"""
Created on Tue Aug 27 18:25:09 2024

Faça um programa que leia o nome RA e média final de uma aluno.
Armazene todas as informações num dicionário. No final programa
deve imprimir as informações do dicionário e situação do aluno
(reprovado, exame ou aprovado). Utilize as regras da UNIFESP
para definir a situação do aluno.

@author: mauricio
"""

############################################################

nome = input("Nome: ")
ra = int(input("Ra: "))
media = float(input("Media: "))

aluno = {"nome" : nome, "ra" : ra, "media" : media}

if (aluno["media"] < 3):
    aluno["sit"] = "Reprovado"

elif (aluno["media"] >= 3 and aluno["media"] <= 6):
    aluno["sit"] = "Aprovado"
    
else:
    aluno["sit"] = "Aprovado"
    
for k, v in aluno.items():
    print(f"{k} = {v}")


############################################################

