"""
Created on Mon Aug 26 16:17:09 2024

Escreva um programa que determine se um número é primo
ou não.

@author: mauricio
"""

############################################################

n1 = int(input("Num: "))
primo = True

for n in range(2, n1, 1):
    
    if (n1 % n == 0):
        primo = False
        
if primo:
    print("Numero Primo")
    
else:
    print("Não é primo")
        

############################################################

