"""
Created on Wed Aug 21 23:17:18 2024

Crie um programa que imprima a sequência de Fibonacci até o
décimo termo usando um loop for.

@author: mauricio
"""

############################################################

a = 0
b = 1
s = 0

for i in range(10):
    print(s)
    
    a = b
    b = s
    
    s = a + b
############################################################

