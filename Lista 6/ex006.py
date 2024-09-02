"""
Created on Tue Aug 27 20:04:32 2024

Implemente uma função chamada "soma_recursiva" que
recebe um número inteiro positivo como parâmetro e
retorna a soma de todos os números inteiros de 1 até esse
número, utilizando recursividade.

@author: mauricio
"""

############################################################

def soma_recursiva(n):
    if n > 1:
        return n + soma_recursiva(n -1)
    else:
        return 1
    
s = soma_recursiva(5)
    
############################################################

