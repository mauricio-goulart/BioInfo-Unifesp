"""
Created on Mon Aug 26 22:00:50 2024

Escreva um programa que leia duas strings e gere uma terceira com os
caracteres comuns às duas strings lidas.
1a string: AAACTBF
2a string: CBT

@author: mauricio
"""

############################################################

p1  = "AAACTBF"
p2 = "CBT"
lista = []


for letra in p1:
    if letra in p2 and letra not in lista:
        lista.append(letra)
        
p3 = "".join(lista)
        
############################################################

