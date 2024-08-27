"""
Created on Wed Aug 21 21:29:37 2024

Crie um script em Python que solicite o nome, altura e peso
de uma pessoa e mostre a seguinte mensagem: “João tem 90
kilos e altura de 1.78 e portanto o IMC é de 28.4”.

@author: mauricio
"""

############################################################

name = str(input("Nome: "))
height = float(input("Altura: "))
weight = float(input("Peso: "))

print(f"{name} tem {weight} kilos e altura de {height} e portanto o IMC é de {weight/(height**2):.2f} ")

############################################################

