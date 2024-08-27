"""
Created on Mon Aug 26 17:17:44 2024

Faça um Programa que leia 20 números inteiros e armazene-os num
lista. Armazene os números pares na lista PAR e os números
IMPARES na lista impar. Imprima os três vetores.

@author: mauricio
"""

############################################################

nlist = []
plist = []
ilist = []

for i in range(5):
    n1 = int(input(f"Digite o {i+1}º Numero: "))
    
    nlist.append(n1)
    
for num in nlist:
    
    if (num % 2 == 0):
        plist.append(num)
        
    else:
        ilist.append(num)

############################################################

