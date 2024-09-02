"""
Created on Tue Aug 27 19:49:23 2024

Escreva uma função chamada fatorial para calcular o
fatorial de um número inteiro.

@author: mauricio
"""

############################################################

def fat(a):
    s = 1
    for i in range(1, a + 1):
        s = s * i
        
    return s
    
    
a = fat(32)

print(a)

############################################################

