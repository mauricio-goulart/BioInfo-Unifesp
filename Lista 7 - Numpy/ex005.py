"""
Created on Tue Aug 27 23:47:06 2024

Crie um array unidimensional com valores aleatórios e encontre o
índice do valor mais próximo de um valor fornecido

@author: mauricio
"""
#Imports:
import numpy as np

############################################################

m = np.random.randint(0, 100, 10)

valor_procurado = 50

m_d = np.abs(m - valor_procurado)

indice_mais_proximo = np.argmin(m_d)

print("Array Original:", m)
print("Valor Procurado:", valor_procurado)
print("Índice do Valor Mais Próximo:", indice_mais_proximo)
print("Valor Mais Próximo:", m[indice_mais_proximo])

############################################################
