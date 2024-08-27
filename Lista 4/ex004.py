"""
Created on Mon Aug 26 22:20:23 2024

Escreva um programa que leia três strings. Imprima o resultado da
substituição na primeira, dos caracteres da segunda pelos da terceira. 1a string:
AATTCGAA 2a string: TG 3a string: AC

@author: mauricio
"""

############################################################

p1 = input("Digite uma palavra: ")
p2 = input("Digite o que voce quer trocar: ")
p3 = input("Digite pelo o que: ")

p4 = p1.replace(p2, p3)

print(p4)

############################################################
