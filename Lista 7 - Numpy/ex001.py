"""
Created on Tue Aug 27 22:02:26 2024

Crie um array unidimensional com valores aleatórios e imprima o
valor médio e a mediana.

@author: mauricio
"""
#Imports:
import numpy as np

############################################################

m = np.random.randint(0, 9, (3,3))

print(f"Valor medio = {m.mean():.2f}")
print(f"Valor mediana = {np.median(m)}")

############################################################

