"""
Created on Mon Aug 26 16:51:49 2024

Faça um Programa que leia uma lista de 10 números reais e mostre-
os na ordem inversa.

@author: mauricio
"""

############################################################

nlist = []

for i in range(3):
    n = int(input(f"{i+1}º Numero: "))
    nlist.append(n)
    
print("Ordem inversa: ")
    
for j in range(len(nlist) -1, -1, -1):
    print(nlist[j])

############################################################
