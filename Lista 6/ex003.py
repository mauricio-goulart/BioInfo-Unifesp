"""
Created on Tue Aug 27 19:54:51 2024

Escreva uma função que receba dois números e retorne
True se o primeiro número for múltiplo do segundo.

@author: mauricio
"""

############################################################

def mult(a, b):
    if (a % b == 0):
        return True
    
    else:
        return False
    
a = mult(4, 2)

print(a)

############################################################
