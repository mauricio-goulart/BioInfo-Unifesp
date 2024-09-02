"""
Created on Tue Aug 27 23:41:23 2024

Crie uma matriz de zeros de tamanho 10x10 e adicione uma borda de
valor 1.

@author: mauricio
"""
#Imports:
import numpy as np    
    
############################################################

m = np.zeros((10,10))

m_bordada = np.pad(m, pad_width=1, mode='constant', constant_values=1)


print(m_bordada)

############################################################

