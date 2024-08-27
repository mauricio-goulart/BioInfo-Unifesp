"""
Created on Mon Aug 26 15:54:29 2024

Escreva um programa que encontre e imprima todos os números
primos entre 1 e 100.

@author: mauricio
"""

############################################################

for num in range(2, 101):
    
    for i in range(2, num):
        
        if num % i == 0:
            break
        
    else: 
        print(num)
            
############################################################

