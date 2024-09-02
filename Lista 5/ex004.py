"""
Created on Tue Aug 27 18:33:19 2024

Crie um programa que leia nome, sexo, peso e altura de várias
pessoas. guarde os dados de cada pessoa num dicionário
individual e acrescente o IMC da pessoa. Organize todos os
dicionários em uma lista. No final mostre
a. Quantas pessoas foram cadastradas
b. Qual é o peso médio das pessoas
c. Qual é a altura média das pessoas
d. Qual é IMC médio das pessoas

@author: mauricio
"""

############################################################

p = int(input("Quantidade de pessoas: "))
i = 0
pessoas = []


while(i < p):
    
    print(f"{i + 1}º Pessoa")
    
    laudo = {}
    laudo["nome"] = input("Nome: ")
    laudo["sexo"] = input("Sexo: ")
    laudo["peso"] = float(input("Peso: "))
    laudo["altura"] = float(input("Altura: "))
    laudo["imc"] = laudo["peso"] / (laudo["altura"] ** 2)
    
    pessoas.append(laudo)
    
    i = i + 1


pmedio = sum(laudo["peso"] for laudo in pessoas) / len(pessoas) 
amedio = sum(laudo["altura"] for laudo in pessoas) / len(pessoas)
imedio = sum(laudo["imc"] for laudo in pessoas) / len(pessoas)
    
print(f"\nPessoas cadastradas = [{len(pessoas)}]")
print(f"Peso medio = {pmedio}")
print(f"Altura media = {amedio}")
print(f"Imc medio = {imedio:.2f}")
    
############################################################

