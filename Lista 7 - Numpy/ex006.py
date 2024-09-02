"""
Created on Wed Aug 28 00:04:10 2024

Crie um array unidimensional com valores aleatórios e encontre os
valores únicos e suas contagens.

@author: mauricio
"""
#Imports:
import numpy as np
############################################################

array = np.random.randint(0, 5, 15)  

valores_unicos, contagens = np.unique(array, return_counts=True)

print("Array Original:", array)

print("Valores Únicos:", valores_unicos)
print("Contagens:", contagens)

############################################################