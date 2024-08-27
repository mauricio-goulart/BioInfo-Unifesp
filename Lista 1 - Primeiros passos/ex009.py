"""
Created on Wed Aug 21 22:46:58 2024

A resistência combinada de três resistores R1, R2 e R3,Crie três variáveis com três valores de resistências e calcule a
resistência resultante.

@author: mauricio
"""

############################################################

r1 = int(input("Resistencia 1: "))
r2 = int(input("Resistencia 2: "))
r3 = int(input("Resistencia 3: "))

totr = 1/(1/r1 + 1/r2 + 1/r3)

print(f"Resistencia resultante: {totr:.2f}")

############################################################

