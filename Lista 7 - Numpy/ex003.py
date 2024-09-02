"""
Created on Tue Aug 27 23:36:37 2024

Crie um array unidimensional com valores aleatórios e calcule a
diferença entre cada elemento e o próximo elemento.

@author: mauricio
"""
#Imports:
import numpy as np

############################################################

m = np.random.randint(0,9,(4))

diferenca= np.diff(m)

print(diferenca)

############################################################

