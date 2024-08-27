"""
Created on Mon Aug 26 17:03:28 2024

Faça um programa que leia duas listas e que gere uma terceira com
os elementos das duas primeiras.

@author: mauricio
"""

############################################################

list1 = []
list2 = []

for i in range(3):
    
    n1 = int(input(f"List1: Digite o {i+1}º Numero: "))
    n2 = int(input(f"List2: Digite o {i+1}º Numero: "))
    
    list1.append(n1)
    list2.append(n2)
    
list3 = list1[:]
list3.extend(list2)

############################################################
