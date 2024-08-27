"""
Created on Mon Aug 26 17:37:20 2024

Escreva uma rotina que recebe uma lista de números e retorna a
soma dos quadrados dos números.

@author: mauricio
"""

############################################################

list1 = []
soma = 0

for i in range(3):
    n = int(input(f"Digite o {i + 1}º Numero: "))
    
    list1.append(n)
    
for i in list1:
    
    soma = soma + i**2
    
print(soma)

############################################################