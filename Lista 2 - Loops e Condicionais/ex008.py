"""
Created on Mon Aug 26 16:33:28 2024

Crie um programa que calcule o IMC (Índice de Massa
Corporal) de uma pessoa e forneça uma classificação com base
no resultado.

@author: mauricio
"""

############################################################

p = float(input("Peso: "))
a = float(input("Altura: "))

imc = p / (a*a)

if (imc < 16.9):
    print("Muito abaixo do peso")
    
elif (imc < 18.4):
    print("Abaixo do peso")
    
elif (imc < 24.9):
    print("Normal")
    
else:
    print("Obeso")
    
############################################################

